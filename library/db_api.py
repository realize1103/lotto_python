# -*- coding: utf-8 -*-
#
from library.logging_pack import *
from sqlalchemy import create_engine, event, Text, Float
from sqlalchemy.pool import Pool
import pymysql
import re
import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from library.alert_api import *
import json
import pandas as pd
from pandas import DataFrame
import numpy as np
from library.constants import *
from pytz import timezone
from datetime import datetime

pymysql.install_as_MySQLdb()


def escape_percentage(conn, clauseelement, multiparams, params):
    # execute로 실행한 sql문이 들어왔을 때 %를 %%로 replace
    if isinstance(clauseelement, str) and '%' in clauseelement and multiparams is not None:
        while True:
            replaced = re.sub(r'([^%])%([^%s])', r'\1%%\2', clauseelement)
            if replaced == clauseelement:
                break
            clauseelement = replaced

    return clauseelement, multiparams, params


def setup_sql_mod(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("SET sql_mode = ''")


event.listen(Pool, 'connect', setup_sql_mod)
event.listen(Pool, 'first_connect', setup_sql_mod)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)

        return cls._instances[cls]


class Db_api(metaclass=Singleton):
    def __init__(self):

        self.alert_api = Alert_api()

        self.conn = None
        self.cur = None
        self.methodName = ""

        with open('config.json', 'r') as f:
            config = json.load(f)

        self.db = config['DEFAULT']['DB']
        self.db_ip = config[self.db]['IP']
        self.db_port = config[self.db]['PORT']
        self.db_id = config[self.db]['ID']
        self.db_pass = config[self.db]['PASS']
        self.db_name = config['DEFAULT']['DB_NAME']
        self.db_name_simul = config['DEFAULT']['DB_NAME_SIMULATION']


        self.system = config['DEFAULT']['SYSTEM']
        # self.db_amazon = 'DB_AMAZON'
        # self.db_ip_amazon = config[self.db_amazon]['IP']
        # self.db_port_amazon = config[self.db_amazon]['PORT']
        # self.db_id_amazon = config[self.db_amazon]['ID']
        # self.db_pass_amazon = config[self.db_amazon]['PASS']

        print(self.db, self.db_ip, self.db_port, self.db_id)
        self.db_name_setting(self.db_name, self.db_name_simul)

        self.table_list = []

        self.constants = Constants()

        KST = timezone("Asia/Seoul")

        self.now = datetime.now(KST)
        self.today = self.now
        self.hours = self.now.hour
        # self.week_day = time.localtime().tm_wday
        self.indate = datetime.strftime(self.today, "%Y-%m-%d")
        self.indate_ymd = datetime.strftime(self.today, "%Y%m%d")

    def create_database(self, cursor):
        db_list = [self.db_name, self.db_name_simul]
        for db_name in db_list:
            logger.debug("create_database!!! {}".format(db_name))
            sql = 'CREATE DATABASE {}'
            cursor.execute(sql.format(db_name))

    # 봇 데이터 베이스 존재 여부 확인 함수
    def is_database_exist(self, cursor):
        db_list = [self.db_name, self.db_name_simul]
        for db_name in db_list:
            sql = "SELECT 1 FROM Information_schema.SCHEMATA WHERE SCHEMA_NAME = '{}'"
            if cursor.execute(sql.format(db_name)):
                logger.debug("%s 데이터 베이스가 존재한다! ", db_name)
                return True
            else:
                logger.debug("%s 데이터 베이스가 존재하지 않는다! ", db_name)
                return False

    def is_table_exist(self, table_name: str, is_simulation:bool = False) -> bool:
        sql = "SELECT 1 FROM Information_schema.tables WHERE table_schema = '%s' and table_name = '%s'"

        db_name, db_engine = self.is_simulation(is_simulation)

        with db_engine.connect() as conn:
            rows = conn.execute(sql % (db_name, table_name)).fetchall()

            if len(rows) == 1:
                logger.debug("%s Table exist! ", table_name)
                return True
            elif len(rows) == 0:
                logger.debug("%s Table doesn't exist!! ", table_name)
                return False

    def create_simulate_tables(self, simulate_id):
        table_name = f'simulate_{simulate_id}'
        if not self.is_table_exist(table_name, True):
            dict_info = self.constants.setting_basic_data('simulate')
            self.create_table(table_name, dict_info, True)

    def create_tables(self, table_name):
        if not self.is_table_exist(table_name):
            dict_info = self.constants.setting_basic_data(table_name.replace('_heikin_ashi', ''))
            self.create_table(table_name, dict_info)

    def is_simulation(self, is_simulation:bool = False):
        if is_simulation:
            db_name = self.db_name_simul
            db_engine = self.engine_simul_DB
        else:
            db_name = self.db_name
            db_engine = self.engine_DB
        return db_name, db_engine

    def create_table(self, table_name, dict_info, is_simulation:bool = False):
        db_name, db_engine = self.is_simulation(is_simulation)

        dict_columns_type: dict = dict_info['dict_columns_type']
        list_index_columns: list = dict_info['list_index_columns']
        list_primary_key_columns: list = dict_info['list_primary_key_columns']

        list_columns = []
        for key in dict_columns_type.keys():
            list_columns.append(key)
        df: DataFrame = DataFrame(columns=list_columns)

        df.to_sql(name=table_name, con=db_engine, if_exists='replace', dtype=dict_columns_type, index=False, method='multi')

        str_key = f'ALTER TABLE `{table_name}` add CONSTRAINT `primary_{table_name}_key` PRIMARY KEY ('
        for index in range(len(list_primary_key_columns)):
            if index != 0:
                str_key += ','
            str_key += '`' + str(list_primary_key_columns[index]) + '`'
        str_key += ')'

        commands: list = [
            str_key
        ]

        for index in range(len(list_index_columns)):
            str_index = f'ALTER TABLE `{table_name}` add index `{table_name}_{str(list_index_columns[index])}_IDX`  ('
            str_index += '`' + str(list_index_columns[index]) + '`'
            str_index += ')'
            commands.append(str_index)

        for com in commands:
            db_engine.execute(com)

    # db 세팅 함수
    def db_name_setting(self, db_name, db_name_simul):
        self.db_name = db_name
        self.db_name_simul = db_name_simul

        logger.debug("db name !!! : %s", self.db_name)
        conn = pymysql.connect(
            host=self.db_ip,
            port=int(self.db_port),
            user=self.db_id,
            password=self.db_pass,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn.cursor() as cursor:
            if not self.is_database_exist(cursor):
                self.create_database(cursor)

            self.engine_DB = create_engine(f'mysql+pymysql://{self.db_id}:{self.db_pass}@{self.db_ip}:{self.db_port}/{db_name}?charset=utf8mb4')
            self.engine_simul_DB = create_engine(f'mysql+pymysql://{self.db_id}:{self.db_pass}@{self.db_ip}:{self.db_port}/{db_name_simul}?charset=utf8mb4')

            # self.engine_DB = create_engine("mysql+pymysql://" + self.db_id + "://" + self.db_pass + "@" + self.db_ip + ":" + self.db_port + "/" + db_name, encoding='utf-8')

        conn.commit()
        conn.close()

        # self.engine_DB_amazon = create_engine("mysql+mysqldb://" + self.db_id_amazon + ":" + self.db_pass_amazon + "@" + self.db_ip_amazon + ":" + self.db_port_amazon + "/" + db_name, encoding='utf-8')

        # self.engine_craw = create_engine("mysql+mysqldb://" + self.db_id + ":" + self.db_pass + "@" + self.db_ip + ":" + self.db_port + "/min_craw", encoding='utf-8')
        #
        # event.listen(self.engine_craw, 'before_execute', escape_percentage, retval=True)

    def data_upsert(self, df, dbcon, tb_name, dict_info):
        try:

            if_exists = dict_info['if_exists'] if 'if_exists' in dict_info else 'replace'

            df = df.fillna('')

            cols = [column for column in list(df.columns)]
            # print("cols : ", cols)
            str_query = ""
            if if_exists == 'fail':
                str_query += "INSERT INTO %s (" % tb_name
            elif if_exists == 'replace':
                str_query += "REPLACE INTO %s (" % tb_name
            elif if_exists == "update":
                str_query += "UPDATE %s " % tb_name
            else:
                str_query += "INSERT IGNORE INTO %s (" % tb_name

            if if_exists == "update":
                columns = dict_info['columns']
                where = dict_info['where']
                str_query += " SET "
                for col in columns:
                    str_query += "`" + col + "` =  %s ,"
                str_query = str_query[:-1]

                str_query += " WHERE "
                for col in where:
                    str_query += "`" + col + "` =  %s AND "
                str_query = str_query[:-4]

                df = df[columns + where]


            else:
                for col in cols:
                    str_query += "`" + col + "`,"
                str_query = str_query[:-1]
                str_query += ")"

            # rows_val = []
            # for index in df.index:
            #     rowval = []
            #     for column in df.columns:
            #         rowval.append(df.loc[index, column])
            #     rows_val.append(rowval)

                str_query += " values ("

                for col in cols:
                    str_query += "%s,"
                str_query = str_query[:-1]
                str_query += ")"

            # print(str_query)

            data = [tuple(x) for x in df.to_numpy()]

            cursor = dbcon.cursor()
            cursor.executemany(str_query, data)
            # logger.info("apply row cnt:%d", cnt)
            cursor.close()

        except Exception as ex:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error("data_upsert -> exception! %s  : %s %d" % (str(ex), fname, exc_tb.tb_lineno))

    def update_data_to_db(self, table_name: str, df: DataFrame, dict_info: dict = {}, is_simulation:bool = False) -> object:
        if self.system == 'WORK':
            print('Work !!')
            return
        # print('update_data_to_db in ', table_name)

        db_name, db_engine = self.is_simulation(is_simulation)

        if dict_info == None:
            dict_info = {}

        before_commands: list = dict_info['before_commands'] if 'before_commands' in dict_info else []
        remain_columns: list = dict_info['remain_columns'] if 'remain_columns' in dict_info else []
        anal_columns: list = dict_info['anal_columns'] if 'anal_columns' in dict_info else []
        remain_join_columns: str = dict_info['remain_join_columns'] if 'remain_join_columns' in dict_info else ''

        # df = df.where(pd.notnull(df), None)

        b_exist_table = False
        # print(self.table_list)
        if table_name in self.table_list:
            b_exist_table = True
        elif self.is_table_exist(table_name, is_simulation):
            b_exist_table = True
            self.table_list.append(table_name)

        if b_exist_table:

            if len(remain_columns) > 0:
                str_sql = 'SELECT '
                str_sql += remain_join_columns
                for index in range(len(remain_columns)):
                    str_sql += ',' + str(remain_columns[index]) + ''
                str_sql += f' FROM `{table_name}`'
                df_remain_data = pd.read_sql_query(str_sql, con=db_engine)

                if len(df_remain_data) > 0:
                    # print(df_remain_data)
                    df = pd.merge(left=df, right=df_remain_data,
                                  how="left", on=remain_join_columns)
                    # print(df)

                else:
                    for index in range(len(remain_columns)):
                        # print(remain_columns[index])
                        df.insert(len(df.columns), remain_columns[index], '')

            for com in before_commands:
                db_engine.execute(com)

            connection = db_engine.raw_connection()
            self.data_upsert(df, connection, table_name, dict_info)
            connection.commit()

        else:
            dict_info = self.constants.setting_basic_data(table_name)
            dict_columns_type: dict = dict_info['dict_columns_type']
            list_index_columns: list = dict_info['list_index_columns']
            list_primary_key_columns: list = dict_info['list_primary_key_columns']

            if len(remain_columns) > 0:
                for index in range(len(remain_columns)):
                    print(remain_columns[index],
                          dict_columns_type[remain_columns[index]])
                    if "CHAR" in str(dict_columns_type[remain_columns[index]]):
                        print("문자열")
                        df.insert(len(df.columns), remain_columns[index], '')
                    else:
                        print("숫자")
                        df.insert(len(df.columns), remain_columns[index], 0)

            if len(anal_columns) > 0:
                for index in range(len(anal_columns)):
                    print(anal_columns[index],
                          dict_columns_type[anal_columns[index]])
                    if "CHAR" in str(dict_columns_type[anal_columns[index]]):
                        print("문자열")
                        df.insert(len(df.columns), anal_columns[index], '')
                    else:
                        print("숫자")
                        df.insert(len(df.columns), anal_columns[index], 0)

            df.to_sql(name=table_name, con=self.engine_DB, if_exists='replace', dtype=dict_columns_type, index=False, method='multi')
            str_key = f'ALTER TABLE `{table_name}` add CONSTRAINT `primary_{table_name}_key` PRIMARY KEY ('
            for index in range(len(list_primary_key_columns)):
                if index != 0:
                    str_key += ','
                str_key += '`' + str(list_primary_key_columns[index]) + '`'
            str_key += ')'

            str_index = f'ALTER TABLE `{table_name}` add index `ix_{table_name}_index`  ('
            for index in range(len(list_index_columns)):
                if index != 0:
                    str_index += ','
                str_index += '`' + str(list_index_columns[index]) + '`'
            str_index += ')'

            # print(str_key+str_column)

            commands = [
                str_key,
                str_index
            ]
            for com in commands:
                self.engine_DB.execute(com)

    def insert_common_code(self, type_value, name, sub_type_0_value, sub_type_1_value, value):
        sql = "INSERT INTO COMMON_CODE"
        sql += " (TYPE, NAME, SUB_TYPE_0, SUB_TYPE_1, VALUE) values ("
        sql += f" '{type_value}', '{name}', '{sub_type_0_value}', '{sub_type_1_value}', '{value}'"
        sql += ")"
        self.engine_DB.execute(sql)

    def delete_common_code(self, type_value, sub_type_0_value, sub_type_1_value):
        sql = "DELETE FROM COMMON_CODE"
        sql += f" WHERE  TYPE = '{type_value}' and SUB_TYPE_0 = '{sub_type_0_value}'"
        sql += f" and SUB_TYPE_1 = '{sub_type_1_value}'"
        self.engine_DB.execute(sql)

    def update_common_code(self, type_value, sub_type_0_value, sub_type_1_value, value):
        if self.system == 'WORK':
            print('Work !!')
            return
        sql = "UPDATE COMMON_CODE"
        sql += f" SET VALUE = '{value}'"
        sql += f" WHERE  TYPE = '{type_value}' and SUB_TYPE_0 = '{sub_type_0_value}'"
        sql += f" and SUB_TYPE_1 = '{sub_type_1_value}'"
        self.engine_DB.execute(sql)

    def update_theme_stock_info(self, theme, stock_code):
        sql = "UPDATE STOCK_INFO"
        sql += f" SET THEME = concat(THEME, '{theme},') "
        sql += f" WHERE  STOCK_CODE = 'A{stock_code}'"
        self.engine_DB.execute(sql)

    def update_theme_init_stock_info(self):
        sql = "UPDATE STOCK_INFO"
        sql += f" SET THEME = '' "
        self.engine_DB.execute(sql)

    def select_common_code(self, type_value, sub_type_0_value, sub_type_1_value):
        sql = """
            SELECT TYPE, SUB_TYPE_0, SUB_TYPE_1, NAME, VALUE"""
        sql += f" FROM {self.db_name}.COMMON_CODE"
        sql += f" WHERE  TYPE = '{type_value}' and SUB_TYPE_0 = '{sub_type_0_value}'"
        sql += f" and SUB_TYPE_1 = '{sub_type_1_value}'"
        # print(sql)
        output = self.engine_DB.execute(sql).fetchall()

        if len(output) > 0:
            return output
        else:
            return None

    def update_sql(self, sql):
        self.engine_DB.execute(sql)

    def delete_table(self, table_name):
        sql = f"DELETE FROM {table_name}"
        self.engine_DB.execute(sql)

    def execute_select_sql(self, sql):
        output = self.engine_DB.execute(sql).fetchall()

        # connection = self.engine_DB.raw_connection()
        # cursor = connection.cursor(pymysql.cursors.DictCursor)
        # cursor.execute(sql)
        # data = cursor.fetchall()
        # # df = pd.DataFrame(data)
        # cursor.close()
        # connection.commit()

        if len(output) > 0:
            return output
        else:
            return None


    def execute_select_sql_df(self, sql):
        connection = self.engine_DB.raw_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        data = cursor.fetchall()
        df = pd.DataFrame(data)
        # print(df)
        cursor.close()
        connection.commit()
        return df

    def common_data(self, common_type, name, sub_type_0, sub_type_1, default_value):
        # print(common_type, name, sub_type_0, sub_type_1, default_value)
        common_data_value = self.select_common_code(common_type, sub_type_0, sub_type_1)
        if None == common_data_value:
            self.insert_common_code(common_type, name, sub_type_0, sub_type_1, default_value)
            return default_value

        df = pd.DataFrame(common_data_value, columns=['TYPE', 'SUB_TYPE_0', 'SUB_TYPE_1', 'NAME', 'VALUE'])

        return (df['VALUE'].values.tolist())[0]

    def _get_stock_item_all(self):
        sql = """
        SELECT stock_code, Name"""
        # SELECT SUBSTRING(STOCK_CODE,2,6) as STOCK_CODE"""
        sql += f" FROM {self.db_name}.stock_info_kr"
        sql += " WHERE Stock_status = '0'"

        self._stock_item_all = self.engine_DB.execute(sql).fetchall()

        df_stock_list = pd.DataFrame(self._stock_item_all, columns=['stock_code', 'Name'])
        return df_stock_list
'''

SELECT *,A.INVEST_BUDGET_REAL - (B.PURCHASE_AMOUNT) ,
CASE WHEN A.INVEST_BUDGET_REAL - (B.PURCHASE_AMOUNT) < C.CLOSE_VALUE
		THEN A.INVEST_BUDGET_REAL + 300000
		ELSE A.INVEST_BUDGET_REAL
		END 

FROM STOCK_INFO A
LEFT JOIN ACCOUNT_INFO_MAX_INDATE_VIEW B
ON A.STOCK_ID = B.STOCK_CODE
LEFT JOIN (SELECT STOCK_ID,CLOSE_VALUE FROM STOCK_HISTORY BASIC_DATE = (SELECT MAX(MAX_DATE) FROM STOCK_INFO_VIEW) C
ON A.STOCK_ID = C.STOCK_ID
WHERE A.PROD = 'Y'
AND A.TRADE_STR IN ('LT')
'''
