from pandas import DataFrame
from sqlalchemy import types, Column

class Constants:

    def setting_basic_data(self, type_data: str):
        case_name = 'case_' + str(type_data)
        print(case_name)
        case = getattr(self, case_name, lambda: 'default')
        dict_columns_type, list_index_columns, list_primary_key_columns = case()

        dict_data = {}

        # dict_data["df_data"] = df_data
        dict_data["dict_columns_type"] = dict_columns_type
        dict_data["list_index_columns"] = list_index_columns
        dict_data["list_primary_key_columns"] = list_primary_key_columns
        return dict_data

    def case_common_code(self):
        dict_columns_type = {
            "type": types.VARCHAR(50),
            "sub_type_0": types.VARCHAR(100),
            "sub_type_1": types.VARCHAR(100),
            "name": types.VARCHAR(100),
            "value": types.VARCHAR(100),
        }
        list_index_columns = ["type", "sub_type_0", "sub_type_1"]
        list_primary_key_columns = ["type", "sub_type_0", "sub_type_1"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_stock_info_kr(self):
        # stock_status : 1 normal 2:del 3:administrative
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "Name": types.VARCHAR(200),
            "Market": types.VARCHAR(10),
            "Sector": types.VARCHAR(200),
            "Industry": types.VARCHAR(300),
            "ListingDate": types.VARCHAR(8),
            "SettleMonth": types.VARCHAR(5),
            "Stock_status": types.VARCHAR(1),
        }
        list_index_columns = ["stock_code", "NAME"]
        list_primary_key_columns = ["stock_code"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_STOCK_MIN_CHART(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "time": types.VARCHAR(4),
            "open": types.INTEGER(),
            "high": types.INTEGER(),
            "low": types.INTEGER(),
            "close": types.INTEGER(),
            "diff": types.INTEGER(),
            "d1_diff_rate": types.FLOAT(precision=2),
            "volume": types.BIGINT(),
            "transtn_amt": types.BIGINT(),
            "clo5": types.INTEGER(),
            "clo10": types.INTEGER(),
            "clo20": types.INTEGER(),
            "clo40": types.INTEGER(),
            "clo60": types.INTEGER(),
            "clo80": types.INTEGER(),
            "clo100": types.INTEGER(),
            "clo120": types.INTEGER(),
            "clo240": types.INTEGER(),
            "yes_clo": types.INTEGER(),
            "yes_clo5": types.INTEGER(),
            "yes_clo10": types.INTEGER(),
            "yes_clo20": types.INTEGER(),
            "yes_clo40": types.INTEGER(),
            "yes_clo60": types.INTEGER(),
            "yes_clo80": types.INTEGER(),
            "yes_clo100": types.INTEGER(),
            "yes_clo120": types.INTEGER(),
            "yes_clo240": types.INTEGER(),
            "vol5": types.INTEGER(),
            "vol10": types.INTEGER(),
            "vol20": types.INTEGER(),
            "vol40": types.INTEGER(),
            "vol60": types.INTEGER(),
            "vol80": types.INTEGER(),
            "vol100": types.INTEGER(),
            "vol120": types.INTEGER(),
            "vol240": types.INTEGER(),
            "clo5_diff_rate": types.FLOAT(precision=2),
            "clo10_diff_rate": types.FLOAT(precision=2),
            "clo20_diff_rate": types.FLOAT(precision=2),
            "clo40_diff_rate": types.FLOAT(precision=2),
            "clo60_diff_rate": types.FLOAT(precision=2),
            "clo80_diff_rate": types.FLOAT(precision=2),
            "clo100_diff_rate": types.FLOAT(precision=2),
            "clo120_diff_rate": types.FLOAT(precision=2),
            "clo240_diff_rate": types.FLOAT(precision=2),
            "vol5_diff_rate": types.FLOAT(precision=2),
        }
        list_index_columns = ["stock_code", "close", "date"]
        list_primary_key_columns = ["stock_code", "date"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_STOCK_DAILY_CHART(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "time": types.VARCHAR(4),
            "open": types.INTEGER(),
            "high": types.INTEGER(),
            "low": types.INTEGER(),
            "close": types.INTEGER(),
            "diff": types.INTEGER(),
            "d1_diff_rate": types.FLOAT(precision=2),
            "volume": types.BIGINT(),
            "transtn_amt": types.BIGINT(),
            "foreigner": types.BIGINT(),
            "government": types.BIGINT(),
            "foreign_ownership_ratio": types.FLOAT(precision=2),
            "highest_of_52weeks": types.INTEGER(),
            "lowest_of_52weeks": types.INTEGER(),
            "clo5": types.INTEGER(),
            "clo10": types.INTEGER(),
            "clo20": types.INTEGER(),
            "clo40": types.INTEGER(),
            "clo60": types.INTEGER(),
            "clo80": types.INTEGER(),
            "clo100": types.INTEGER(),
            "clo120": types.INTEGER(),
            "clo240": types.INTEGER(),
            "yes_clo": types.INTEGER(),
            "yes_clo5": types.INTEGER(),
            "yes_clo10": types.INTEGER(),
            "yes_clo20": types.INTEGER(),
            "yes_clo40": types.INTEGER(),
            "yes_clo60": types.INTEGER(),
            "yes_clo80": types.INTEGER(),
            "yes_clo100": types.INTEGER(),
            "yes_clo120": types.INTEGER(),
            "yes_clo240": types.INTEGER(),
            "vol5": types.INTEGER(),
            "vol10": types.INTEGER(),
            "vol20": types.INTEGER(),
            "vol40": types.INTEGER(),
            "vol60": types.INTEGER(),
            "vol80": types.INTEGER(),
            "vol100": types.INTEGER(),
            "vol120": types.INTEGER(),
            "vol240": types.INTEGER(),
            "clo5_diff_rate": types.FLOAT(precision=2),
            "clo10_diff_rate": types.FLOAT(precision=2),
            "clo20_diff_rate": types.FLOAT(precision=2),
            "clo40_diff_rate": types.FLOAT(precision=2),
            "clo60_diff_rate": types.FLOAT(precision=2),
            "clo80_diff_rate": types.FLOAT(precision=2),
            "clo100_diff_rate": types.FLOAT(precision=2),
            "clo120_diff_rate": types.FLOAT(precision=2),
            "clo240_diff_rate": types.FLOAT(precision=2),
            "vol5_diff_rate": types.FLOAT(precision=2),
            "clo5_mrdeg": types.FLOAT(precision=2),
            "clo5_degrees": types.FLOAT(precision=2),
            "clo20_mrdeg": types.FLOAT(precision=2),
            "clo20_degrees": types.FLOAT(precision=2),
            "clo120_mrdeg": types.FLOAT(precision=2),
            "clo120_degrees": types.FLOAT(precision=2),

            "UP_5": types.VARCHAR(1),
            "UP_20": types.VARCHAR(1),
            "UP_120": types.VARCHAR(1),
            "DW_5": types.VARCHAR(1),
            "DW_20": types.VARCHAR(1),
            "DW_120": types.VARCHAR(1),
            "GC_5_20": types.VARCHAR(1),
            "GC_5_120": types.VARCHAR(1),
            "DC_5_20": types.VARCHAR(1),
            "DC_5_120": types.VARCHAR(1),
            "ARR_S": types.VARCHAR(1),
            "ARR_R": types.VARCHAR(1),
            "BE_ARR_S": types.VARCHAR(1),
            "BE_ARR_R": types.VARCHAR(1),
            "PNT": types.INTEGER(),
        }
        list_index_columns = ["stock_code", "close", "date"]
        list_primary_key_columns = ["stock_code", "date"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_STOCK_WEEKLY_CHART(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "time": types.VARCHAR(4),
            "open": types.INTEGER(),
            "high": types.INTEGER(),
            "low": types.INTEGER(),
            "close": types.INTEGER(),
            "diff": types.INTEGER(),
            "d1_diff_rate": types.FLOAT(precision=2),
            "volume": types.BIGINT(),
            "transtn_amt": types.BIGINT(),
            "clo5": types.INTEGER(),
            "clo10": types.INTEGER(),
            "clo20": types.INTEGER(),
            "clo40": types.INTEGER(),
            "clo60": types.INTEGER(),
            "clo80": types.INTEGER(),
            "clo100": types.INTEGER(),
            "clo120": types.INTEGER(),
            "clo240": types.INTEGER(),
            "yes_clo": types.INTEGER(),
            "yes_clo5": types.INTEGER(),
            "yes_clo10": types.INTEGER(),
            "yes_clo20": types.INTEGER(),
            "yes_clo40": types.INTEGER(),
            "yes_clo60": types.INTEGER(),
            "yes_clo80": types.INTEGER(),
            "yes_clo100": types.INTEGER(),
            "yes_clo120": types.INTEGER(),
            "YES_CLO240": types.INTEGER(),
            "vol5": types.INTEGER(),
            "vol10": types.INTEGER(),
            "vol20": types.INTEGER(),
            "vol40": types.INTEGER(),
            "vol60": types.INTEGER(),
            "vol80": types.INTEGER(),
            "vol100": types.INTEGER(),
            "vol120": types.INTEGER(),
            "vol240": types.INTEGER(),
            "clo5_diff_rate": types.FLOAT(precision=2),
            "clo10_diff_rate": types.FLOAT(precision=2),
            "clo20_diff_rate": types.FLOAT(precision=2),
            "clo40_diff_rate": types.FLOAT(precision=2),
            "clo60_diff_rate": types.FLOAT(precision=2),
            "clo80_diff_rate": types.FLOAT(precision=2),
            "clo100_diff_rate": types.FLOAT(precision=2),
            "clo120_diff_rate": types.FLOAT(precision=2),
            "clo240_diff_rate": types.FLOAT(precision=2),
            "UP_5": types.VARCHAR(1),
            "UP_10": types.VARCHAR(1),
            "DW_5": types.VARCHAR(1),
            "DW_10": types.VARCHAR(1),
            "GC_5_10": types.VARCHAR(1),
            "DC_5_10": types.VARCHAR(1),
            "ARR_S": types.VARCHAR(1),
            "ARR_R": types.VARCHAR(1),
            "BE_ARR_S": types.VARCHAR(1),
            "BE_ARR_R": types.VARCHAR(1),
            "PNT": types.INTEGER(),
        }
        list_index_columns = ["stock_code", "close", "date"]
        list_primary_key_columns = ["stock_code", "date"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_STOCK_MONTHLY_CHART(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "time": types.VARCHAR(4),
            "open": types.INTEGER(),
            "high": types.INTEGER(),
            "low": types.INTEGER(),
            "close": types.INTEGER(),
            "diff": types.INTEGER(),
            "d1_diff_rate": types.FLOAT(precision=2),
            "volume": types.BIGINT(),
            "transtn_amt": types.BIGINT(),
            "clo5": types.INTEGER(),
            "clo10": types.INTEGER(),
            "clo20": types.INTEGER(),
            "clo40": types.INTEGER(),
            "clo60": types.INTEGER(),
            "clo80": types.INTEGER(),
            "clo100": types.INTEGER(),
            "clo120": types.INTEGER(),
            "clo240": types.INTEGER(),
            "yes_clo": types.INTEGER(),
            "yes_clo5": types.INTEGER(),
            "yes_clo10": types.INTEGER(),
            "yes_clo20": types.INTEGER(),
            "yes_clo40": types.INTEGER(),
            "yes_clo60": types.INTEGER(),
            "yes_clo80": types.INTEGER(),
            "yes_clo100": types.INTEGER(),
            "yes_clo120": types.INTEGER(),
            "YES_CLO240": types.INTEGER(),
            "vol5": types.INTEGER(),
            "vol10": types.INTEGER(),
            "vol20": types.INTEGER(),
            "vol40": types.INTEGER(),
            "vol60": types.INTEGER(),
            "vol80": types.INTEGER(),
            "vol100": types.INTEGER(),
            "vol120": types.INTEGER(),
            "vol240": types.INTEGER(),
            "clo5_diff_rate": types.FLOAT(precision=2),
            "clo10_diff_rate": types.FLOAT(precision=2),
            "clo20_diff_rate": types.FLOAT(precision=2),
            "clo40_diff_rate": types.FLOAT(precision=2),
            "clo60_diff_rate": types.FLOAT(precision=2),
            "clo80_diff_rate": types.FLOAT(precision=2),
            "clo100_diff_rate": types.FLOAT(precision=2),
            "clo120_diff_rate": types.FLOAT(precision=2),
            "clo240_diff_rate": types.FLOAT(precision=2),
            "UP_5": types.VARCHAR(1),
            "UP_10": types.VARCHAR(1),
            "DW_5": types.VARCHAR(1),
            "DW_10": types.VARCHAR(1),
            "GC_5_10": types.VARCHAR(1),
            "DC_5_10": types.VARCHAR(1),
            "ARR_S": types.VARCHAR(1),
            "ARR_R": types.VARCHAR(1),
            "BE_ARR_S": types.VARCHAR(1),
            "BE_ARR_R": types.VARCHAR(1),
            "PNT": types.INTEGER(),
        }
        list_index_columns = ["stock_code", "close", "date"]
        list_primary_key_columns = ["stock_code", "date"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_INDEX_DATA(self):
        dict_columns_type = {
            "date": types.VARCHAR(10),
            "index_code": types.VARCHAR(10),
            "index_name": types.VARCHAR(200),
            "close": types.FLOAT(precision=2),
            "open": types.FLOAT(precision=2),
            "high": types.FLOAT(precision=2),
            "low": types.FLOAT(precision=2),
            "volume": types.FLOAT(precision=2),
            "change": types.FLOAT(precision=2)
        }
        list_index_columns = ["date", "INDEX_CODE"]
        list_primary_key_columns = ["date", "INDEX_CODE"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_QUANT_STOCKS_RESULT(self):
        dict_columns_type = {"years": types.VARCHAR(8), "STOCK_CODE": types.VARCHAR(7), "STOCK_NAME": types.VARCHAR(200), "OVER_PROFIT": types.FLOAT(precision=3), "thstrm_amount": types.BIGINT
            , "calc_ROE": types.FLOAT(precision=3), "ROE": types.FLOAT(precision=3), "ROE_1": types.FLOAT(precision=3), "ROE_2": types.FLOAT(precision=3), "TOTAL_NUMBER_LISTED_STOCKS": types.BIGINT
            , "PBR": types.FLOAT(precision=3), "PER": types.FLOAT(precision=3), "PBR": types.FLOAT(precision=3), "자산총계": types.INTEGER, "GPA": types.FLOAT(precision=3), "매출액": types.BIGINT, "PSR": types.FLOAT(precision=3)
            , "부채비율" : types.FLOAT(precision=3)
            , "FARE_VALUE_OF_COMPANY_F": types.FLOAT(precision=3), "FARE_VALUE_F": types.INTEGER, "FARE_VALUE_OF_COMPANY_MINUS_10": types.FLOAT(precision=3), "FARE_VALUE_MINUS_10": types.INTEGER
            , "FARE_VALUE_OF_COMPANY_MINUS_20": types.FLOAT(precision=3), "FARE_VALUE_MINUS_20": types.INTEGER
            , "PBR_RANK": types.INTEGER, "PER_RANK": types.INTEGER, "GPA_RANK": types.INTEGER, "PSR_RANK": types.INTEGER, "ROE_RANK": types.INTEGER, "POINT_1": types.INTEGER, "POINT_2": types.INTEGER
            , "POINT_3": types.INTEGER, "POINT_4": types.INTEGER, "POINT_5": types.INTEGER, "POINT_6": types.INTEGER, "POINT_7": types.INTEGER
                             }
        list_index_columns = ["years", "STOCK_CODE", "STOCK_NAME", "FARE_VALUE_F"]
        list_primary_key_columns = ["STOCK_CODE", "years"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_ACCOUNT_STATUS(self):
        dict_columns_type = {
            "INDATE": types.VARCHAR(8),
            "STOCK_CODE": types.VARCHAR(7),
            "STOCK_NAME": types.VARCHAR(200),
            "BUY_TYPE": types.VARCHAR(10),
            "LOAN_DATE": types.VARCHAR(10),
            "QUANTITY": types.INTEGER(),
            "AVAILABLE_QUANTITY": types.INTEGER(),
            "RECORDED_COST": types.FLOAT(precision=5),
            "GAIN_LOSS_COST": types.INTEGER(),
            "EVALUATION_AMOUNT": types.INTEGER(),
            "EVALUATION_GAIN_LOSS": types.FLOAT(precision=5),
            "EVALUATION_GAIN_LOSS_COST": types.INTEGER(),
        }
        list_index_columns = ["INDATE", "STOCK_CODE"]
        list_primary_key_columns = ["STOCK_CODE", "INDATE"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_top_30(self):
        dict_columns_type = {
            "date": types.VARCHAR(8),
            "STOCK_CODE": types.VARCHAR(7),
            "NAME": types.VARCHAR(200),
            "SECTOR": types.VARCHAR(200),
            "INDUSTRY": types.VARCHAR(200),
            "RANKING": types.INTEGER(),
            "diff_rate": types.FLOAT(precision=2),
        }
        list_index_columns = ["date", "STOCK_CODE", "NAME","RANKING"]
        list_primary_key_columns = ["date", "STOCK_CODE"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_top_30_period(self):
        dict_columns_type = {
            "date": types.VARCHAR(8),
            "STOCK_CODE": types.VARCHAR(7),
            "NAME": types.VARCHAR(200),
            "unit": types.VARCHAR(10),
            "SECTOR": types.VARCHAR(200),
            "INDUSTRY": types.VARCHAR(200),
            "CNT": types.INTEGER,
        }
        list_index_columns = ["date", "STOCK_CODE", "NAME","unit"]
        list_primary_key_columns = ["date", "STOCK_CODE","unit"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_top_10percent_investor_by_period(self):
        dict_columns_type = {
            "date": types.VARCHAR(8),
            "stock_code": types.VARCHAR(7),
            "name": types.VARCHAR(200),
            "unit": types.VARCHAR(10),
            "investor": types.VARCHAR(20),
            "sector": types.VARCHAR(200),
            "industry": types.VARCHAR(200),
            "cnt": types.INTEGER,
        }
        list_index_columns = ["date", "stock_code", "investor", "unit", "cnt"]
        list_primary_key_columns = ["date", "stock_code", "investor", "unit"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_arr_direction_cnt_by_period(self):
        dict_columns_type = {
            "date": types.VARCHAR(8),
            "stock_code": types.VARCHAR(7),
            "unit": types.VARCHAR(10),
            "cnt": types.INTEGER,
        }
        list_index_columns = ["date", "stock_code", "unit", "cnt"]
        list_primary_key_columns = ["date", "stock_code", "unit"]
        return dict_columns_type, list_index_columns, list_primary_key_columns


    def case_INCOME_STATEMENT_FN_GUIDE(self):
        dict_columns_type = {
            "STOCK_CODE": types.VARCHAR(7),
            "STOCK_NAME": types.VARCHAR(200),
            "DATE": types.VARCHAR(7),
            "TYPE_REPORT": types.VARCHAR(10),
            "매출액": types.INTEGER(),
            "매출원가": types.INTEGER(),
            "매출총이익": types.INTEGER(),
            "판매비와관리비": types.INTEGER(),
            "영업이익": types.INTEGER(),
            "영업이익(발표기준)": types.INTEGER(),
            "금융수익": types.INTEGER(),
            "금융원가": types.INTEGER(),
            "기타수익": types.INTEGER(),
            "기타비용": types.INTEGER(),
            "종속기업,공동지배기업및관계기업관련손익": types.INTEGER(),
            "세전계속사업이익": types.INTEGER(),
            "법인세비용": types.INTEGER(),
            "계속영업이익": types.INTEGER(),
            "중단영업이익": types.INTEGER(),
            "당기순이익": types.INTEGER(),
            "지배주주순이익": types.INTEGER(),
            "비지배주주순이익": types.INTEGER(),
        }
        list_index_columns = ["DATE", "STOCK_CODE", "TYPE_REPORT"]
        list_primary_key_columns = ["STOCK_CODE", "DATE", "TYPE_REPORT"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_FINANCIAL_STATUS_FN_GUIDE(self):
        dict_columns_type = {
            "STOCK_CODE": types.VARCHAR(7),
            "STOCK_NAME": types.VARCHAR(200),
            "DATE": types.VARCHAR(7),
            "TYPE_REPORT": types.VARCHAR(10),
            "자산": types.INTEGER(),
            "유동자산": types.INTEGER(),
            "비유동자산": types.INTEGER(),
            "기타금융업자산": types.INTEGER(),
            "부채": types.INTEGER(),
            "유동부채": types.INTEGER(),
            "비유동부채": types.INTEGER(),
            "기타금융업부채": types.INTEGER(),
            "자본": types.INTEGER(),
            "지배기업주주지분": types.INTEGER(),
            "비지배주주지분": types.INTEGER(),
        }
        list_index_columns = ["DATE", "STOCK_CODE", "TYPE_REPORT"]
        list_primary_key_columns = ["STOCK_CODE", "DATE", "TYPE_REPORT"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_FINANCIAL_HIGHLIGHT_FN_GUIDE(self):
        dict_columns_type = {
            "STOCK_CODE": types.VARCHAR(7),
            "STOCK_NAME": types.VARCHAR(200),
            "DATE": types.VARCHAR(7),
            "TYPE_REPORT": types.VARCHAR(10),
            "자산": types.INTEGER(),
            "유동자산": types.INTEGER(),
            "비유동자산": types.INTEGER(),
            "기타금융업자산": types.INTEGER(),
            "부채": types.INTEGER(),
            "유동부채": types.INTEGER(),
            "비유동부채": types.INTEGER(),
            "기타금융업부채": types.INTEGER(),
            "자본": types.INTEGER(),
            "지배기업주주지분": types.INTEGER(),
            "비지배주주지분": types.INTEGER(),
        }
        list_index_columns = ["DATE", "STOCK_CODE", "TYPE_REPORT"]
        list_primary_key_columns = ["STOCK_CODE", "DATE", "TYPE_REPORT"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_STOCK_DAILY_CHART_heikin_ashi(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "open": types.FLOAT(precision=3),
            "high": types.FLOAT(precision=3),
            "low": types.FLOAT(precision=3),
            "close": types.FLOAT(precision=3),
        }

        list_index_columns = ["stock_code", "date", "close"]
        list_primary_key_columns = ["stock_code","date"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_STOCK_WEEKLY_CHART_heikin_ashi(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "open": types.FLOAT(precision=3),
            "high": types.FLOAT(precision=3),
            "low": types.FLOAT(precision=3),
            "close": types.FLOAT(precision=3),
        }

        list_index_columns = ["stock_code", "date", "close"]
        list_primary_key_columns = ["stock_code","date"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_STOCK_MONTHLY_CHART_heikin_ashi(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "open": types.FLOAT(precision=3),
            "high": types.FLOAT(precision=3),
            "low": types.FLOAT(precision=3),
            "close": types.FLOAT(precision=3),
        }

        list_index_columns = ["stock_code", "date", "close"]
        list_primary_key_columns = ["stock_code","date"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_macd_12_26_9(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "unit": types.VARCHAR(10),
            "MACD_short": types.FLOAT(precision=3),
            "MACD_long": types.FLOAT(precision=3),
            "MACD": types.FLOAT(precision=3),
            "MACD_signal": types.FLOAT(precision=3),
            "MACD_oscillator": types.FLOAT(precision=3),
            "MACD_sign": types.VARCHAR(1),
        }

        list_index_columns = ["stock_code", "date", "unit"]
        list_primary_key_columns = ["stock_code", "date", "unit"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_rsi_14_150(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "unit": types.VARCHAR(10),
            "rsi": types.FLOAT(precision=3),
            "ma": types.FLOAT(precision=3),
        }

        list_index_columns = ["stock_code", "date", "unit"]
        list_primary_key_columns = ["stock_code", "date", "unit"]
        return dict_columns_type, list_index_columns, list_primary_key_columns
    def case_investor_daily(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "investor": types.VARCHAR(20),
            "sell": types.BIGINT(),
            "buy": types.BIGINT(),
            "benefit": types.BIGINT(),
        }
        list_index_columns = ["stock_code", "date", "investor"]
        list_primary_key_columns = ["stock_code", "date", "investor"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_investor_daily_ordered(self):

        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "stock_name": types.VARCHAR(100),
            "date": types.VARCHAR(8),
            "market": types.VARCHAR(8),
            "investor": types.VARCHAR(20),
            "sell": types.BIGINT(),
            "buy": types.BIGINT(),
            "sell_volume": types.BIGINT(),
            "buy_volume": types.BIGINT(),
            "benefit": types.BIGINT(),
            "benefit_volume": types.BIGINT(),
        }
        list_index_columns = ["stock_code", "date", "investor"]
        list_primary_key_columns = ["stock_code", "date", "investor"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_obv(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(19),
            "unit": types.VARCHAR(10),
            "obv": types.BIGINT(),
            "obv_ma": types.BIGINT(),
            "diff": types.BIGINT(),
            "diff-1": types.BIGINT(),
            "signal": types.VARCHAR(1),
        }

        list_index_columns = ["stock_code", "date", "unit"]
        list_primary_key_columns = ["stock_code", "date", "unit"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_obv_period(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(19),
            "unit": types.VARCHAR(10),
            "obv": types.BIGINT(),
            # "diff": types.BIGINT(),
            # "diff-1": types.BIGINT(),
            # "signal": types.VARCHAR(1),
        }

        list_index_columns = ["stock_code", "date", "unit"]
        list_primary_key_columns = ["stock_code", "date", "unit"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_cci(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(19),
            "unit": types.VARCHAR(10),
            "cci": types.FLOAT(precision=2),
            "cci-1": types.FLOAT(precision=2),
            "signal": types.VARCHAR(1),
        }

        list_index_columns = ["stock_code", "date", "unit"]
        list_primary_key_columns = ["stock_code", "date", "unit"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_back_testing_condition(self):
        dict_columns_type = {
            "id": types.INT(),
            "buy_condition": types.VARCHAR(500),
            "sell_condition": types.VARCHAR(500),
            "name": types.VARCHAR(200),
        }
        list_index_columns = ["id"]
        list_primary_key_columns = ["id"]
        return dict_columns_type, list_index_columns, list_primary_key_columns


    def case_trading_conditions(self):
        dict_columns_type = {
            "id": Column(types.INT(), primary_key=True, autoincrement=True),
            "name": types.VARCHAR(200),
            "table_name": types.VARCHAR(30),
            "trading_type": types.VARCHAR(1),
            "table_syno": types.VARCHAR(10),
            "join_type": types.VARCHAR(3),
            "condition": types.VARCHAR(200),
            "condition_ohlc": types.VARCHAR(200),
            "add_column": types.VARCHAR(100),
            "use_yn": types.VARCHAR(1),
        }
        list_index_columns = ["id","trading_type"]
        list_primary_key_columns = ["id","trading_type"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_simulate(self):
        dict_columns_type = {
            'stock_code': types.VARCHAR(7),
            "buy_date": types.VARCHAR(19),
            "buy_close": types.INT(),
            "date": types.VARCHAR(19),
            "close": types.INT(),
            "diff": types.INT(),
            "rate": types.FLOAT(precision=3),
            "acc_rate": types.FLOAT(precision=3),
            "benefit": types.FLOAT(precision=3),
            "acc_benefit": types.FLOAT(precision=3),
            "estimate_amount": types.FLOAT(precision=3),
            "acc_estimate_amount": types.FLOAT(precision=3),
        }
        list_index_columns = ["stock_code","buy_date"]
        list_primary_key_columns = ["stock_code","buy_date"]
        return dict_columns_type, list_index_columns, list_primary_key_columns


    def case_simulate_result(self):
        dict_columns_type = {
            'simulate_id':types.VARCHAR(200),
            'stock_code': types.VARCHAR(7),
            "total_cnt": types.INTEGER(),
            "total_rate": types.FLOAT(precision=3),
            "total_benefit": types.FLOAT(precision=3),
            "Y-1_cnt": types.INTEGER(),
            "Y-1_rate": types.FLOAT(precision=3),
            "Y-1_benefit": types.FLOAT(precision=3),
            "M-3_cnt": types.INTEGER(),
            "M-3_rate": types.FLOAT(precision=3),
            "M-3_benefit": types.FLOAT(precision=3),
            "M-1_cnt": types.INTEGER(),
            "M-1_rate": types.FLOAT(precision=3),
            "M-1_benefit": types.FLOAT(precision=3),
            "W-1_cnt": types.INTEGER(),
            "W-1_rate": types.FLOAT(precision=3),
            "W-1_benefit": types.FLOAT(precision=3),
        }
        list_index_columns = ["simulate_id"]
        list_primary_key_columns = ["simulate_id", "stock_code"]
        return dict_columns_type, list_index_columns, list_primary_key_columns


    def case_ohlc_daily(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "open": types.INTEGER(),
            "high": types.INTEGER(),
            "low": types.INTEGER(),
            "close": types.INTEGER(),
            "volume": types.BIGINT(),
            "transtn_amt": types.BIGINT(),
            "diff_rate": types.FLOAT(precision=2),
            "bps": types.FLOAT(precision=2),
            "per": types.FLOAT(precision=2),
            "pbr": types.FLOAT(precision=2),
            "eps": types.FLOAT(precision=2),
            "div": types.FLOAT(precision=2),
            "dps": types.FLOAT(precision=2),
            "market_cap": types.FLOAT(precision=2),
            "number_stocks": types.BIGINT(),
            "arr_d": types.VARCHAR(1),
            "weight": types.FLOAT(precision=2),
        }
        list_index_columns = ["stock_code", "close", "date"]
        list_primary_key_columns = ["stock_code", "date"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_finance_major_indicator_report(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "기업": types.VARCHAR(200),
            "연도": types.VARCHAR(4),
            "corp_code": types.VARCHAR(10),
            "자산총계": types.BIGINT(),
            "부채총계": types.BIGINT(),
            "자본총계": types.BIGINT(),
            "매출액": types.BIGINT(),
            "영업이익": types.BIGINT(),
            "당기순이익": types.BIGINT(),
            "매출총이익": types.BIGINT(),
            "부채비율": types.FLOAT(precision=2),
            "영업이익증가율": types.FLOAT(precision=2),
            "매출액증가율": types.FLOAT(precision=2),
            "당기순이익증가율": types.FLOAT(precision=2),
            "매출액_상태": types.VARCHAR(20),
            "ROA": types.FLOAT(precision=2),
            "ROE": types.FLOAT(precision=2),
        }
        list_index_columns = ["stock_code", "기업", "연도"]
        list_primary_key_columns = ["stock_code", "기업", "연도"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_ma(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "unit": types.VARCHAR(10),
            "ma5": types.FLOAT(precision=2),
            "ma20": types.FLOAT(precision=2),
            "ma60": types.FLOAT(precision=2),
            "ma120": types.FLOAT(precision=2),
            "ma240": types.FLOAT(precision=2),
        }
        list_index_columns = ["stock_code", "date", "unit"]
        list_primary_key_columns = ["stock_code", "date", "unit"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_major_value(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "unit": types.VARCHAR(10),
            "max_close": types.INTEGER(),
            "min_close": types.INTEGER(),
            "fibo_diff": types.INTEGER(),
            "fibo_lv1": types.FLOAT(precision=2),
            "fibo_lv2": types.FLOAT(precision=2),
            "fibo_lv3": types.FLOAT(precision=2),
            "fibo_lv4": types.FLOAT(precision=2),
        }
        list_index_columns = ["stock_code", "date", "unit"]
        list_primary_key_columns = ["stock_code", "date", "unit"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_ma_index(self):
        dict_columns_type = {
            "index_code": types.VARCHAR(7),
            "date": types.VARCHAR(8),
            "unit": types.VARCHAR(10),
            "ma5": types.FLOAT(precision=2),
            "ma20": types.FLOAT(precision=2),
            "ma60": types.FLOAT(precision=2),
            "ma120": types.FLOAT(precision=2),
            "ma240": types.FLOAT(precision=2),
        }
        list_index_columns = ["index_code", "date", "unit"]
        list_primary_key_columns = ["index_code", "date", "unit"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_business_major_indicator_report(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(7),
            "기업": types.VARCHAR(200),
            "연도": types.VARCHAR(4),
            "corp_code": types.VARCHAR(10),
            "구분": types.VARCHAR(100),
            "발행주식수": types.BIGINT(),
            "자기주식": types.BIGINT(),
            "유통주식수": types.BIGINT(),
        }
        list_index_columns = ["stock_code", "기업", "연도","구분"]
        list_primary_key_columns = ["stock_code", "기업", "연도","구분"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_quant_s_rim(self):
        dict_columns_type = {
            "연도": types.VARCHAR(4)
            , "stock_code": types.VARCHAR(7)
            , "stock_name": types.VARCHAR(200)
            , "OVER_PROFIT": types.FLOAT(precision=3)
            , "자본총계": types.BIGINT
            , "calc_ROE": types.FLOAT(precision=3)
            , "ROE": types.FLOAT(precision=3)
            , "ROE_1": types.FLOAT(precision=3)
            , "ROE_2": types.FLOAT(precision=3)
            , "유통주식수": types.BIGINT
            , "FARE_VALUE_OF_COMPANY_F": types.FLOAT(precision=3)
            , "FARE_VALUE_F": types.INTEGER
            , "FARE_VALUE_OF_COMPANY_MINUS_10": types.FLOAT(precision=3)
            , "FARE_VALUE_MINUS_10": types.INTEGER
            , "FARE_VALUE_OF_COMPANY_MINUS_20": types.FLOAT(precision=3)
            , "FARE_VALUE_MINUS_20": types.INTEGER
        }
        list_index_columns = ["연도", "stock_code"]
        list_primary_key_columns = ["연도", "stock_code"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_stock_info_kr_del(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(8),
            "Name": types.VARCHAR(200),
            "Market": types.VARCHAR(10),
            "SecuGroup": types.VARCHAR(300),
            "Kind": types.VARCHAR(100),
            "ListingDate": types.VARCHAR(8),
            "DelistingDate": types.VARCHAR(8),
            "Reason": types.VARCHAR(500),
        }
        list_index_columns = ["stock_code"]
        list_primary_key_columns = ["stock_code","DelistingDate"]
        return dict_columns_type, list_index_columns, list_primary_key_columns

    def case_stock_info_kr_adm(self):
        dict_columns_type = {
            "stock_code": types.VARCHAR(8),
            "Name": types.VARCHAR(200),
            "DesignationDate": types.VARCHAR(8),
            "Reason": types.VARCHAR(500),
        }
        list_index_columns = ["stock_code"]
        list_primary_key_columns = ["stock_code","DesignationDate"]
        return dict_columns_type, list_index_columns, list_primary_key_columns


    def case_stock_evaluate(self):
        dict_columns_type = {
            "date": types.VARCHAR(8),
            "stock_code": types.VARCHAR(8),
            "Indicator": types.VARCHAR(20),
            "Pnt": types.INTEGER(),
            "description": types.VARCHAR(200),
        }
        list_index_columns = ["date","stock_code","Indicator"]
        list_primary_key_columns = ["date","stock_code","Indicator"]
        return dict_columns_type, list_index_columns, list_primary_key_columns