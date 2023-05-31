import sys
import requests
import json
import pandas as pd
import io
import gspread
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import numpy as np
from urllib.parse import quote_plus

dateTo = datetime.date(datetime.today())
dateFrom = dateTo - timedelta(days=21)
with io.open("tables.json", encoding='utf-8', mode='r') as json_file:
  tables = json.load(json_file)

for t in tables:
  sheet_id = tables[t]["table"]
  clientId = tables[t]["Client_ID"]
  apiKey = tables[t]["Api_OZON"]
  headers = {
    'Client-Id': clientId,
    'Api-Key': apiKey
  };
  
  page = 1
  body = {
      "filter": {
          "date": {
              "from": f"{dateFrom}T00:00:00.000Z",
              "to": f"{dateTo}T23:59:59.999Z"
          },
          "operation_type": [],
          "posting_number": "",
          "transaction_type": "all"
      },
      "page": page,
      "page_size": 1000
    };
  # Параметры запроса

  # options = {
  #   "method": "POST",
  #   "headers": headers,
  #   "contentType": "application/json",
  #   "payload": JSON.stringify(body)
  # };

  body = json.dumps(body)
  print(18)
  
  operation_id = []
  operation_type = []
  operation_date = []
  operation_type_name = []
  delivery_charge = []
  return_delivery_charge = []
  accruals_for_sale = []
  sale_commission = []
  amount = []
  type_ = []
  posting_delivery_schema = []
  posting_order_date = []
  posting_posting_number = []
  posting_warehouse_id = []
  items_0_name = []
  items_0_sku = []
  items_length = []
  service_0_name = []
  service_0_price = []
  service_1_name = []
  service_1_price = []
  service_2_name = []
  service_2_price = []
  service_3_name = []
  service_3_price = []

  while True:
  
      response = requests.post("https://api-seller.ozon.ru/v3/finance/transaction/list", headers=headers, data=body)
      #print(response)

      #print(response)
      
      try:
        response = response.text
      # print(response)
        response = response
      # print(response)
        response = json.loads(response)
        response = response['result']
        response = response['operations']
        len_response = len(response)
      except:
        print('error responce')
        print(response)
        #print(requests.post("https://api-seller.ozon.ru/v2/posting/fbo/list", headers=headers, data=body))
        len_response = 0
      #
      #
      # sys.exit()
      

      j = 1
      # k = 0
      try:
          for list_data in response:
            operation_id += [list_data['operation_id']]
            operation_type += [list_data['operation_type']]
            operation_date += [list_data['operation_date']]
            operation_type_name += [list_data['operation_type_name']]
            delivery_charge += [list_data['delivery_charge']]
            return_delivery_charge += [list_data['return_delivery_charge']]
            accruals_for_sale += [list_data['accruals_for_sale']]
            sale_commission += [list_data['sale_commission']]
            amount += [list_data['amount']]
            type_ += [list_data['type']]
            posting_delivery_schema += [list_data['posting']['delivery_schema']]
            posting_order_date += [list_data['posting']['order_date']]
            posting_posting_number += [list_data['posting']['posting_number']]
            posting_warehouse_id += [list_data['posting']['warehouse_id']]


            try:
              service_0_name += [list_data['services'][0]['name']]
            except:
              service_0_name += [0]


            try:
              service_0_price += [list_data['services'][0]['price']]
            except:
              service_0_price += [0]


            try:
              service_1_name += [list_data['services'][1]['name']]
            except:
              service_1_name += [0]


            try:
              service_1_price += [list_data['services'][1]['price']]
            except:
              service_1_price += [0]


            try:
              service_2_name += [list_data['services'][2]['name']]
            except:
              service_2_name += [0]


            try:
              service_2_price += [list_data['services'][2]['price']]
            except:
              service_2_price += [0]


            try:
              service_3_name += [list_data['services'][3]['name']]
            except:
              service_3_name += [0]


            try:
              service_3_price += [list_data['services'][3]['price']]
            except:
              service_3_price += [0]


            try:
              items_0_name += [list_data['items'][0]['name']]
            except:
              items_0_name += [0]


            try:
              items_0_sku += [list_data['items'][0]['sku']]
            except:
              items_0_sku += [0]


            try:
              items_length += [list_data['items'].length]
            except:
              items_length += [0]
            
      except:
        page
        
      page += 1
      body = {
      "filter": {
      "date": {
          "from": f"{dateFrom}T00:00:00.000Z",
          "to": f"{dateTo}T23:59:59.999Z"
      },
      "operation_type": [],
      "posting_number": "",
      "transaction_type": "all"
      },
      "page": page,
      "page_size": 1000
      };
      
      print(len_response)
      print(page)
      print(body)
      print(len(items_length))
      if len_response == 0:
        break
  # Параметры запроса

  # options = {
  #   "method": "POST",
  #   "headers": headers,
  #   "contentType": "application/json",
  #   "payload": JSON.stringify(body)
  # };

      body = json.dumps(body)
  



  data = pd.DataFrame({
    'operation_id': operation_id,
    'operation_type': operation_type,
    'operation_date': operation_date,
    'operation_type_name': operation_type_name,
    'delivery_charge': delivery_charge,
    'return_delivery_charge': return_delivery_charge,
    'accruals_for_sale': accruals_for_sale,
    'sale_commission': sale_commission,
    'amount': amount,
    'type': type_,
    'posting_delivery_schema': posting_delivery_schema,
    'posting_order_date': posting_order_date,
    'posting_posting_number': posting_posting_number,
    'posting_warehouse_id': posting_warehouse_id,
    'items_0_name': items_0_name,
    'items_0_sku': items_0_sku,
    'items_length': items_length,
    'service_0_name': service_0_name,
    'service_0_price': service_0_price,
    'service_1_name': service_1_name,
    'service_1_price': service_1_price,
    'service_2_name': service_2_name,
    'service_2_price': service_2_price,
    'service_3_name': service_3_name,
    'service_3_price': service_3_price
  })
  #
  data['user_id'] = sheet_id
  data['date_load'] = str(datetime.today())
  # data['barcode'] = data['barcode'].values.astype(np.int64)
  #print(data)
  # data.to_csv(f"name_file table.csv")

  # запись в бд
  engine = create_engine('postgresql://postgres:TrW34Uq@localhost:5432/dashboard')

  data.to_sql('finance_transaction_list_ozon', engine, if_exists='append')
  data.to_sql('finance_transaction_list_ozon_all', engine, if_exists='append')
  print('ok', sheet_id)

#input('Нажмите Enter для выхода\n')


