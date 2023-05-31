import requests
import json
import pandas as pd
import io
import time
import gspread
from sqlalchemy import create_engine
from datetime import datetime
import numpy as np
from urllib.parse import quote_plus

engine = create_engine('postgresql://postgres:TrW34Uq@localhost:5432/dashboard')

with io.open("tables.json", encoding='utf-8', mode='r') as json_file:
  tables = json.load(json_file)
gc = gspread.service_account(filename="credentials.json")
with io.open("client.json", encoding='utf-8', mode='r') as json_file:
    client = json.load(json_file)
print(22)
k = 0
for l in client:
    l = str(l)
    # print(l)
    All_tables = client[l]["tables"]
    All_tables = All_tables.split(',')
    print(All_tables)
    sheet_id = client[l]["id"]
    url = client[l]["url"]

    sql = f"SELECT * from analytics_stock_on_warehouses_ozon WHERE user_id in ({All_tables})"
    print(sql)
    try:
        sql = f"SELECT * from analytics_stock_on_warehouses_ozon WHERE user_id in ({str(All_tables)[1:-1]})"
        data = pd.read_sql(sql, con=engine)
    except:
        sql = f'SELECT * from analytics_stock_on_warehouses_ozon WHERE user_id = "{All_tables[0]}"'
        data = pd.read_sql(sql, con=engine)

    data.drop(columns=data.columns[0], axis= 1 , inplace= True )
    
    # загрузка в гугл док
    sh = gc.open_by_key(sheet_id)


    worksheet = sh.worksheet("Склад (исх.) (ОЗОН)")
    # ws_values = worksheet.get_all_values()
    # print(ws_values)
    # df = pd.DataFrame.from_records(ws_values[1:], columns=ws_values[0])
    # df = df[["skus", "cost_price"]]
    # df['skus'] = df['skus'].values.astype('object')
    # data["cost_price"] = 0
    # data['skus'] = data['skus'].values.astype('object')
    print(126)
    # index = len(data)

    #try:
    #    data = data.merge(df, how='left', on='skus')
    #except:
    #    data
    # смена типа данных
    
    #data['skus'] = data['skus'].values.astype('object')
    # data['cost_price'] = data['cost_price'].values.astype('number')
    data = data.fillna('')
    # print(153)
    values = data.values
    values = values.tolist()
    print(data)
    # print(type(values))
    len_values = len(values)
    print('len_values', len_values)



    if len_values != 0:
        cycle = 0
        while cycle < 3:
            try:
                cycle += 1
                worksheet.batch_clear(["A2:S20000"])
                worksheet.update(f'A2:S{len_values + 1}', values)

                print("data upgrage")

               # запись даты обновления
                # worksheet = sh.worksheet("обновление таблиц")
                # worksheet.update(f'B10', date_now)
    
            except Exception as ex:
                print(ex)
                time.sleep(10)
            else:
                #break loop
                break
    

    
