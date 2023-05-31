import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(
    user="postgres",
    # пароль, который указали при установке PostgreSQL
    password="TrW34Uq",
    host="localhost",
    port="5432",
    database="dashboard")

try:
    cursor = connection.cursor()
    cursor.execute('TRUNCATE orders_wb, stocks_wb, sales_wb, nomenclature_wb, finance_transaction_list_ozon, posting_fbo_list_ozon, posting_fbs_list_ozon, analytics_stock_on_warehouses_ozon, analytics_stock_on_warehouses_ozon2, products_ozon')
    # cursor.execute(
    #     'TRUNCATE orders_wb, sales_wb, nomenclature_wb')
    connection.commit()
    print("orders_wb, sales_wb очищено")
except Exception as ex:
    print(ex)
    print('ошибка очистки orders_wb, sales_wb')

