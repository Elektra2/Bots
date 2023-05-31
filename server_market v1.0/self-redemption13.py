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
with io.open("client.json", encoding='utf-8', mode='r') as json_file:
    client = json.load(json_file)

engine = create_engine('postgresql://postgres:TrW34Uq@localhost:5432/dashboard')


# получить данные srid из гугла
gc = gspread.service_account(filename="credentials.json")
sh = gc.open_by_key('1X6d3EaZZSW6sIWidYB2Wp3KFHDhVy9m9TfoAV_SLIlc')
worksheet = sh.worksheet("Самовыкупы")
ws_values = worksheet.get_all_values()
df_GS = pd.DataFrame.from_records(ws_values[1:], columns=ws_values[0])

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
df["srid"] = df_GS[['ID заказа']]

i = 0
sql = f"select reportdetailbyperiod_wb.srid, reportdetailbyperiod_wb.barcode, reportdetailbyperiod_wb.nm_id, reportdetailbyperiod_wb.sa_name, reportdetailbyperiod_wb.ts_name, reportdetailbyperiod_wb.retail_amount, date(reportdetailbyperiod_wb.sale_dt) as sale_dt FROM reportdetailbyperiod_wb WHERE doc_type_name = 'Продажа' and reportdetailbyperiod_wb.user_id = '1001' and retail_amount != 0"
df_new = pd.read_sql(sql, con=engine)


sql = f"select srid, barcode, \"nmId\" as nm_id, \"supplierArticle\" as sa_name, \"techSize\" as ts_name, \"totalPrice\" as retail_amount, date(date) as sale_rfs FROM sales_wb WHERE sales_wb.user_id = '1001'"
df_srid_sales = pd.read_sql(sql, con=engine)

sql = f"select srid, barcode, \"nmId\" as nm_id, \"supplierArticle\" as sa_name, \"techSize\" as ts_name, \"totalPrice\" as retail_amount, date(orders_wb.date) as order_dt FROM orders_wb WHERE orders_wb.user_id = '1001'"
df_srid_order = pd.read_sql(sql, con=engine)

df_new = df.merge(df_new, left_on='srid', right_on='srid', how='left')

df_srid_sales = df.merge(df_srid_sales, left_on='srid', right_on='srid',how='left')
df_srid_order = df.merge(df_srid_order, left_on='srid', right_on='srid',how='left')
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
    "count": []
})
df["srid"] = df_GS[['ID заказа']]
df = df.fillna(value=df_new)
df = df.fillna(value=df_srid_sales)
df = df.fillna(value=df_srid_order)
df['count'] = 1
df = df[['srid', 'barcode', 'nm_id', 'sa_name', 'ts_name','retail_amount','order_dt','sale_rfs','sale_dt', "count"]]

df.to_csv('1.csv')
# print(df)

index = len(df)
cycle = 0
df['order_dt'] = df['order_dt'].values.astype('str')
df['sale_dt'] = df['sale_dt'].values.astype('str')
df['sale_rfs'] = df['sale_rfs'].values.astype('str')
df = df.fillna('')

values = df.values
values = values.tolist()
len_values = len(values)
worksheet = sh.worksheet("Самовыкупы")
worksheet.batch_clear(["B2:L100000"])
worksheet.update(f'B2:L{len_values + 1}', values)
