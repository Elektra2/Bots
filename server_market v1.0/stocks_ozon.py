import requests
import json
import pandas as pd
import io
import gspread
from sqlalchemy import create_engine
from datetime import datetime
import numpy as np
from urllib.parse import quote_plus

with io.open("tables.json", encoding='utf-8', mode='r') as json_file:
  tables = json.load(json_file)


for t in tables:
    try:
          sheet_id = tables[t]["table"]
          print(sheet_id)
          clientId = tables[t]["Client_ID"]
          apiKey = tables[t]["Api_OZON"]

          headers = {
            'Client-Id': clientId,
            'Api-Key': apiKey
          };
          body = {
          "limit": 1000,
          "offset": 0
          };



          body = json.dumps(body)
          print(18)


          response = requests.post("https://api-seller.ozon.ru/v1/analytics/stock_on_warehouses", headers=headers, data=body)

          response = response.text
          response = response
          response = json.loads(response)
          print(body)
          response = response['total_items']
          #
          #
          offer_id = []
          sku = []
          title = []
          category = []
          discounted = []
          barcode = []
          length = []
          width = []
          height = []
          volume = []
          weight = []
          not_for_sale = []
          loss = []
          for_sale = []
          between_warehouses = []
          shipped = []

          j = 1
          # k = 0
          for i in response:
            try:
              barcode_l = i['barcode'].split(';')
              for j in barcode_l:
                # print(type(barcode_l))
                # print(barcode_l)
                offer_id += [i['offer_id']]
                sku += [i['sku']]
                title += [i['title']]
                category += [i['category']]
                discounted += [i['discounted']]
                barcode += [j]
                length += [i['length']]
                width += [i['width']]
                height += [i['height']]
                volume += [i['volume']]
                weight += [i['weight']]
                not_for_sale += [i['stock']['not_for_sale']]
                loss += [i['stock']['loss']]
                for_sale += [i['stock']['for_sale']]
                between_warehouses += [i['stock']['between_warehouses']]
                shipped += [i['stock']['shipped']]
            except:
              offer_id += [i['offer_id']]
              sku += [i['sku']]
              title += [i['title']]
              category += [i['category']]
              discounted += [i['discounted']]
              barcode += [i['barcode']]
              length += [i['length']]
              width += [i['width']]
              height += [i['height']]
              volume += [i['volume']]
              weight += [i['weight']]
              not_for_sale += [i['stock']['not_for_sale']]
              loss += [i['stock']['loss']]
              for_sale += [i['stock']['for_sale']]
              between_warehouses += [i['stock']['between_warehouses']]
              shipped += [i['stock']['shipped']]

          data = pd.DataFrame({
            "offer_id": offer_id,
            "sku": sku,
            "title": title,
            "category": category,
            "discounted": discounted,
            "barcode": barcode,
            "length": length,
            "width": width,
            "height": height,
            "volume": volume,
            "weight": weight,
            "not_for_sale": not_for_sale,
            "loss": loss,
            "for_sale": for_sale,
            "between_warehouses": between_warehouses,
            "shipped": shipped
          })
          #
          data['user_id'] = sheet_id
          data['date_load'] = str(datetime.today())
          # data['barcode'] = data['barcode'].values.astype(np.int64)
          # print(data)
          # data.to_csv(f"name_file table.csv")

          print("data upgrage")
          # print(vals)

          # запись в бд
          engine = create_engine('postgresql://postgres:TrW34Uq@localhost:5432/dashboard')
          
          data.to_sql('analytics_stock_on_warehouses_ozon',engine, if_exists='append')
          data.to_sql('analytics_stock_on_warehouses_ozon_all', engine, if_exists='append')
          print('обновлено ', t)
    except Exception as ex:
        print(ex)
        print('error ',sheet_id)

