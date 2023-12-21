from tinkoff.invest import Client, InstrumentStatus, SharesResponse, InstrumentIdType
import pandas as pd
import openpyxl

TOKEN = 't.YmCIDJulB7UdqB1syVFXrh8Xh8kiChe1MVn2IDXUnIyJyIbMaxJkK0ceiVAZmdpHntD5yZX6LQjvlbkALT4rWg'


def iam_get_favourites():

    favourites_table = pd.DataFrame(columns=['figi',
                                             'ticker',
                                             'class_code',
                                             'isin',
                                             'instrument_type',
                                             'otc_flag',
                                             'api_trade_available_flag',
                                             'instrument_kind'])
    favourites_table_list = [None] * 8

    with Client(TOKEN) as client:
        my_favourites = client.instruments.get_favorites()
        for i in my_favourites.favorite_instruments:
            favourites_table_list[0] = (i.figi)
            favourites_table_list[1] = (i.ticker)
            favourites_table_list[2] = (i.class_code)
            favourites_table_list[3] = (i.isin)
            favourites_table_list[4] = (i.instrument_type)
            favourites_table_list[5] = (i.otc_flag)
            favourites_table_list[6] = (i.api_trade_available_flag)
            favourites_table_list[7] = (i.instrument_kind)

            if i.instrument_type == 'bond':
                favourites_table.loc[len(favourites_table)] = favourites_table_list

    favourites_table.to_excel('favourites.xlsx', engine='openpyxl', index=False)

def iam_get_bonds(figi,class_code,isin,instrument_type ):
    with (Client(TOKEN) as client):
        bond_price = client.market_data.get_last_prices(figi=figi)

        bonds_info = client.instruments.bond_by(id_type = InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI,
                                                class_code = class_code, id = figi)
        # print(bonds_info.instrument.currency)
        for i in bond_price.last_prices:
            print(i.figi)
            print(i.price.units)
            print(i.price.nano)
            print(i.time)
            print(i.instrument_uid)
        # print(bond_price.last_prices.figi)
        # print(bond_price.last_prices.price.units)
        # print(bond_price.last_prices.price.currency)
        # print(bond_price.last_prices.time)
        # print(bond_price.last_prices.instrument_uid)




    pass
if __name__ == "__main__":
    # iam_get_favourites()
    iam_get_bonds('TCS00A1074Q1', 'TQCB', 'RU000A1074Q1', 'bond')

