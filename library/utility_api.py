import pandas as pd


class UtilityApi:

    @staticmethod
    def str_to_bool(str_value):
        return str_value.lower() in ("yes", "true", "t", "1")

    @staticmethod
    def print_df(df):
        msg = ''
        for key in df.keys():
            msg += str(key) + '   '
        print(msg)

        print("=========")

        for index, row in df.iterrows():
            # if index > 10:
            #     break
            msg = ''
            for key in df.keys():
                msg += str(row[str(key)]) + '   '
            print(msg)


    @staticmethod
    def msg_df(df):
        msg_header = ''
        for key in df.keys():
            msg_header += str(key) + '   '
        msg_header += '\n'

        print(msg_header)
        print("=========")

        msg = ''
        for index, row in df.iterrows():
            # if index > 10:
            #     break
            for key in df.keys():
                msg += str(row[str(key)]) + '   '
            msg += '\n'

        print(msg)
        if msg != '':
            msg = msg_header + msg
        return msg

    @staticmethod
    def calc_ratio(a, b):
        if a == 0 or b == 0:
            return 0
        return round((float(a) - float(b)) / float(b) * 100,2)

    @staticmethod
    def convert_df(candles):

        df = pd.DataFrame(candles)
        df.rename(columns={"opening_price": "open"}, inplace=True)
        df.rename(columns={"high_price": "high"}, inplace=True)
        df.rename(columns={"low_price": "low"}, inplace=True)
        df.rename(columns={"trade_price": "close"}, inplace=True)
        return df

    @staticmethod
    def set_index(df, column_name):
        print(df)
        print(df.set_index(column_name))
        print(df.reset_index())
        # print(df.reset_index()
        print(df.set_index(column_name, inplace=True))
        return df.set_index(column_name, inplace=True)

    @staticmethod
    def calc_ma(candles_for_day):

        if candles_for_day is not None and len(candles_for_day) > 1:
            df = pd.DataFrame(candles_for_day)
            # print(df.head())

            df.rename(columns={"opening_price": "open"}, inplace=True)
            df.rename(columns={"high_price": "high"}, inplace=True)
            df.rename(columns={"low_price": "low"}, inplace=True)
            df.rename(columns={"trade_price": "close"}, inplace=True)

            # mid = round(((float(df.loc[0]['open'])+ float(df.loc[0]['low']))/2),2)
            # print(mid)
            # df.loc[0]['close'] = mid
            # print(df.loc[0]['clos)
            # print(df.head())
            df = df.sort_index(ascending=False).reset_index()
            # print(df.head())

            df['ma5'] = df['close'].rolling(window=5).mean()
            df['ma10'] = df['close'].rolling(window=10).mean()
            df['ma15'] = df['close'].rolling(window=15).mean()
            df['ma50'] = df['close'].rolling(window=50).mean()
            df['ma120'] = df['close'].rolling(window=120).mean()

            df = df.fillna(0)
            # print(df)
            return df

    @staticmethod
    def fix_price(price):
        _unit = {
            10: 0.01,
            10 ** 1: 0.1,
            10 ** 2: 1,
            10 ** 3: 5,
            10 ** 4: 10,
            5 * 10 ** 4: 50,
            10 ** 5: 100,
            10 ** 6: 500,
            2 * 10 ** 6: 1000
        }

        for p in _unit:
            if price > p:
                price = (price // _unit[p]) * _unit[p]
        return price

    @staticmethod
    def list_split(lst, n):
        return [lst[i:i + n] for i in range(0, len(lst), n)]
