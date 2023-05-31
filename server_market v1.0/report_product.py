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
        temporary = pd.DataFrame({})
        for t in All_tables:
            try:
                # конвектирование user_id в id json
                  t = str(int(t) - 1001)
                  user_id = tables[t]["table"]
                  print(user_id)
                  clientId = tables[t]["Client_ID"]
                  apiKey = tables[t]["Api_OZON"]
                  print(clientId)
                  print(apiKey)
                  headers = {
                    'Client-Id': clientId,
                    'Api-Key': apiKey
                  };
                  body = {
                    "language": "DEFAULT",
                    "offer_id": [ ],
                    "search": "",
                    "sku": [ ],
                    "visibility": "ALL"
                    }

                  body = json.dumps(body)
                  print(18)


                  response = requests.post("https://api-seller.ozon.ru/v1/report/products/create", headers=headers, data=body)

                  response = response.text
                  response = response
                  response = json.loads(response)
                  # print(body)

                  code = response['result']['code']
                  body = {
                      "code": code
                  }
                  body = json.dumps(body)


                  time.sleep(20)


                  response = requests.post("https://api-seller.ozon.ru/v1/report/info", headers=headers, data=body)

                  response = response.text
                  response = response
                  response = json.loads(response)
                  print(response)
                  file = response['result']['file']
                  df = pd.read_csv(file, delimiter=';')
                  df['user_id'] = user_id
                  df['date_load'] = str(datetime.date(datetime.today()))
                  temporary = pd.concat([temporary, df], sort=False,axis=0)
                  # df.to_csv(f'df {user_id}.csv')
                  df.to_sql('products_ozon', engine, if_exists='append')








            except Exception as ex:
                print(ex)
                print('error ',user_id)

        sh = gc.open_by_key(sheet_id)
        try:
            worksheet = sh.worksheet("Номенклатура ОЗОН")
        except:
            # добавление листа
            worksheet = sh.add_worksheet(title="Номенклатура ОЗОН", rows=100, cols=20)
            row = [["Артикул", "Ozon Product ID", "FBO OZON SKU ID", "FBS OZON SKU ID", "Наименование товара", "Текущая цена с учетом скидки, руб.", "Цена до скидки (перечеркнутая цена), руб.", "user_id", "cost_price"]]
            worksheet.update('A1:I1', row)
        ws_values = worksheet.get_all_values()
        # print(ws_values)
        data = pd.DataFrame.from_records(ws_values[1:], columns=ws_values[0])
        data = data[["Артикул", "cost_price"]]
        # print(df.dtypes)
        df = temporary
        df = df.merge(data, how='left', on='Артикул')
        df.to_sql('products_ozon', engine, if_exists='append')
        df = df[["Артикул", "Ozon Product ID", "FBO OZON SKU ID", "FBS OZON SKU ID", "Наименование товара", "Текущая цена с учетом скидки, руб.", "Цена до скидки (перечеркнутая цена), руб.", "user_id"]]

        df = df.fillna('')
        # print(153)
        df = df.drop_duplicates()
        df = df.values
        values = df.tolist()

        len_values = len(values)

        worksheet.batch_clear(["A2:I20000"])
        worksheet.update(f'A2:I{len_values + 1}', values)

        print("data upgrage")

    except Exception as ex:
        print(ex)
        print('error ', l)

