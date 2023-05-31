import json
from datetime import datetime, timedelta
import pandas as pd
from sqlalchemy import create_engine, select
import numpy as np
import io
import gspread
import psycopg2
from psycopg2 import Error

"чтение json с таблицами"
with io.open("tables.json", encoding='utf-8', mode='r') as json_file:
    tables = json.load(json_file)
    gc = gspread.service_account(filename="credentials.json")
with io.open("client_self-redemption.json", encoding='utf-8', mode='r') as json_file:
    client = json.load(json_file)

engine = create_engine('postgresql://postgres:TrW34Uq@localhost:5432/dashboard')

for l in client:
    l = str(l)
    # print(l)
    All_tables = client[l]["tables"]
    All_tables = All_tables.split(',')
    # print(All_tables)
    sheet_id = client[l]["id"]
    url = client[l]["url"]


    # получить данные srid из гугла
    gc = gspread.service_account(filename="credentials.json")
    sh = gc.open_by_key(sheet_id)
    worksheet = sh.worksheet("Самовыкупы")
    ws_values = worksheet.get_all_values()
    df_GS = pd.DataFrame.from_records(ws_values[1:], columns=ws_values[0])
    df_GS = df_GS.iloc[:, 0:13]
    # print(df_GS.dtypes)
    df_GS.columns = ['srid','srid2', 'barcode', 'nm_id', 'sa_name', 'ts_name', 'retail_amount', 'order_dt', 'sale_rfs', 'sale_dt', 'count', 'realizationreport_id']

    index_df_GS = len(df_GS)


    df = pd.DataFrame({
        "srid": [],
        # "barcode": [],
        # "nm_id": [],
        # "sa_name": [],
        # "ts_name": [],
        # "retail_amount": [],
        # "order_dt": [],
        # "sale_rfs": [],
        # "sale_dt": [],
        # "count": []
    })
    df["srid"] = df_GS[['srid']]
    df_new = pd.DataFrame({})
    df_srid_sales = pd.DataFrame({})
    df_srid_order = pd.DataFrame({})
    for n in All_tables:
        i = 0
        sql = f"select reportdetailbyperiod_wb.realizationreport_id, reportdetailbyperiod_wb.srid, reportdetailbyperiod_wb.barcode, reportdetailbyperiod_wb.nm_id, reportdetailbyperiod_wb.sa_name, reportdetailbyperiod_wb.ts_name, reportdetailbyperiod_wb.retail_amount, date(reportdetailbyperiod_wb.sale_dt) as sale_dt FROM reportdetailbyperiod_wb WHERE doc_type_name = 'Продажа' and reportdetailbyperiod_wb.user_id = '{n}' and retail_amount != 0"
        interim = pd.read_sql(sql, con=engine)
        df_new = pd.concat([df_new, interim], sort=False,axis=0)
        # print(df_new)
        # print(df_new)


        sql = f"select srid, barcode, \"nmId\" as nm_id, \"supplierArticle\" as sa_name, \"techSize\" as ts_name, \"totalPrice\", \"discountPercent\", date(date) as sale_rfs FROM sales_wb WHERE sales_wb.user_id = '{n}'"
        interim = pd.read_sql(sql, con=engine)
        df_srid_sales = pd.concat([df_srid_sales, interim], sort=False,axis=0)


        sql = f"select srid, barcode, \"nmId\" as nm_id, \"supplierArticle\" as sa_name, \"techSize\" as ts_name, \"totalPrice\", \"discountPercent\", date(orders_wb.date) as order_dt FROM orders_wb WHERE orders_wb.user_id = '{n}'"
        interim = pd.read_sql(sql, con=engine)
        df_srid_order = pd.concat([df_srid_order, interim], sort=False,axis=0)


    df_srid_sales['retail_amount'] = df_srid_sales['totalPrice'] - (
                df_srid_sales['totalPrice'] * df_srid_sales['discountPercent'] * 0.01)
    df_srid_order['retail_amount'] = df_srid_order['totalPrice'] - (
                df_srid_order['totalPrice'] * df_srid_order['discountPercent'] * 0.01)

    df_new = df.merge(df_new, left_on='srid', right_on='srid', how='left')
    df_srid_order = df.merge(df_srid_order, left_on='srid', right_on='srid', how='left')
    df_srid_sales = df.merge(df_srid_sales, left_on='srid', right_on='srid',how='left')
    print(df_srid_order[['retail_amount', 'totalPrice']])

    df = pd.DataFrame({
        "srid": [],
        "barcode": [],
        "nm_id": [],
        "sa_name": [],
        "ts_name": [],
        "retail_amount": [],
        "order_dt": [],
        "sale_rfs": [],
        "sale_dt": [],
        "count": [],
        "realizationreport_id": []
    })
    df["srid"] = df_GS[['srid']]
    df = df.fillna(value=df_new)
    df = df.fillna(value=df_srid_sales)
    df = df.fillna(value=df_srid_order)
    df['count'] = 1
    # print(104,df)
    df = df[['srid', 'barcode', 'nm_id', 'sa_name', 'ts_name','retail_amount','order_dt','sale_rfs','sale_dt', "count", 'realizationreport_id']]
    # print(106, df)
    # df.to_csv('1.csv')
    # print(df)

    index = len(df)
    cycle = 0
    df['order_dt'] = df['order_dt'].values.astype('str')
    df['sale_dt'] = df['sale_dt'].values.astype('str')
    df['sale_rfs'] = df['sale_rfs'].values.astype('str')
    df = df.fillna('')
    df = df.replace(['nan'], '')

    values = df.values
    values = values.tolist()
    len_values = len(values)
    worksheet = sh.worksheet("Самовыкупы")
    worksheet.batch_clear(["B2:L100000"])
    worksheet.update(f'B2:L{len_values + 1}', values)
