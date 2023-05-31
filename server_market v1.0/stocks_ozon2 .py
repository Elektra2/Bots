import requests
import json
import pandas as pd
import io
import gspread
from sqlalchemy import create_engine
from datetime import datetime
import time
import numpy as np
from urllib.parse import quote_plus
engine = create_engine('postgresql://postgres:TrW34Uq@localhost:5432/dashboard')

with io.open("tables.json", encoding='utf-8', mode='r') as json_file:
  tables = json.load(json_file)
gc = gspread.service_account(filename="credentials.json")
with io.open("client.json", encoding='utf-8', mode='r') as json_file:
    client = json.load(json_file)

for l in client:
    try:
        l = str(int(l))
        # print(l)
        All_tables = client[l]["tables"]
        All_tables = All_tables.split(',')
        print(All_tables)
        sheet_id = client[l]["id"]
        url = client[l]["url"]
        sku = []
        warehouse_name = []
        item_code = []
        item_name = []
        promised_amount = []
        free_to_sell_amount = []
        reserved_amount = []
        user_id_all = []





        for t in All_tables:
            try:
                # конвектирование user_id в id json
                t = str(int(t) - 1001)
                user_id = tables[t]["table"]
                print(user_id)
                clientId = tables[t]["Client_ID"]
                apiKey = tables[t]["Api_OZON"]

                headers = {
                  'Client-Id': clientId,
                  'Api-Key': apiKey
                };
                body = {
                "limit": 1000,
                "offset": 0,
                "warehouse_type": "ALL"
                };



                body = json.dumps(body)
                print(18)


                response = requests.post("https://api-seller.ozon.ru/v2/analytics/stock_on_warehouses", headers=headers, data=body)

                response = response.text
                response = response
                response = json.loads(response)
                # print(response)
                response = response['result']["rows"]
                # print(response)
                df = pd.DataFrame({})
                for i in response:
                    sku += [i['sku']]
                    warehouse_name += [i['warehouse_name']]
                    item_code += [i['item_code']]
                    item_name += [i['item_name']]
                    promised_amount += [i['promised_amount']]
                    free_to_sell_amount += [i['free_to_sell_amount']]
                    reserved_amount += [i['reserved_amount']]
                    user_id_all += [user_id]



            except Exception as ex:
                print(ex)
                print('error ',user_id)

        df = pd.DataFrame({
            'sku':sku,
            'warehouse_name':warehouse_name,
            'item_code':item_code,
            'item_name':item_name,
            'promised_amount':promised_amount,
            'free_to_sell_amount':free_to_sell_amount,
            'reserved_amount':reserved_amount,
            'user_id': user_id_all
        })
        df['date_load'] = str(datetime.today())

        df.to_sql('analytics_stock_on_warehouses_ozon2', engine, if_exists='append')
        df.to_sql('analytics_stock_on_warehouses_ozon2_all', engine, if_exists='append')
        df_agr = df.drop(columns=['warehouse_name', 'promised_amount', 'reserved_amount', 'free_to_sell_amount'])
        df_agr = df_agr.drop_duplicates()

        df_agr["promised_amount"] = [df.loc[df["item_name"] == v, "promised_amount"].sum() for v in df_agr["item_name"]]
        df_agr["free_to_sell_amount"] = [df.loc[df["item_name"] == v, "free_to_sell_amount"].sum() for v in df_agr["item_name"]]
        df_agr["reserved_amount"] = [df.loc[df["item_name"] == v, "reserved_amount"].sum() for v in df_agr["item_name"]]
        df_agr['warehouse_name'] = 'all_warehouse'
        df = pd.concat([df, df_agr], sort=False,axis=0)
        df.to_sql('analytics_stock_on_warehouses_ozon2', engine, if_exists='append')
        df.to_sql('analytics_stock_on_warehouses_ozon2_all', engine, if_exists='append')


    except Exception as ex:
        print(ex)
        print('error ', l)

