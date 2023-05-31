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
dateFrom = dateTo - timedelta(days=60)

with io.open("tables.json", encoding='utf-8', mode='r') as json_file:
  tables = json.load(json_file)

for t in tables:
  offset = 0

  order_id = []
  order_number = []
  posting_number = []
  status = []
  cancel_reason_id = []
  created_at = []
  in_process_at = []
  products_0_sku = []
  products_0_name = []
  products_0_quantity = []
  products_0_offer_id = []
  products_0_price = []
  products_0_digital_codes = []
  analytics_data_region = []
  analytics_data_city = []
  analytics_data_delivery_type = []
  analytics_data_is_premium = []
  analytics_data_payment_type_group_name = []
  analytics_data_warehouse_id = []
  analytics_data_warehouse_name = []
  analytics_data_is_legal = []
  commission_amount = []
  commission_percent = []
  payout = []
  product_id = []
  old_price = []
  price = []
  total_discount_value = []
  total_discount_percent = []
  actions = []
  picking = []
  quantity = []
  client_price = []
  item_services_marketplace_service_item_fulfillment = []
  item_services_marketplace_service_item_pickup = []
  item_services_marketplace_service_item_dropoff_pvz = []
  item_services_marketplace_service_item_dropoff_sc = []
  item_services_marketplace_service_item_dropoff_ff = []
  item_services_marketplace_service_item_direct_flow_trans = []
  item_services_marketplace_service_item_return_flow_trans = []
  item_services_marketplace_service_item_deliv_to_customer = []
  item_services_marketplace_service_item_return_not_deliv_to_customer = []
  item_services_marketplace_service_item_return_part_goods_customer = []
  item_services_marketplace_service_item_return_after_deliv_to_customer = []

  while True:

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
      "dir": "desc",
      "filter": {
        "since": f"{dateFrom}T00:00:00.000Z",
        "status": "",
        "to": f"{dateTo}T23:59:59.000Z"
        },
        "limit": 1000,
        "offset": offset,
        "translit": True,
        "with": {
          "analytics_data": True,
          "financial_data": True
        }
        }
      # Параметры запроса
      print(body)
      # options = {
      #   "method": "POST",
      #   "headers": headers,
      #   "contentType": "application/json",
      #   "payload": JSON.stringify(body)
      # };

      body = json.dumps(body)
      print(18)

      offset += 1000

      response = requests.post("https://api-seller.ozon.ru/v2/posting/fbo/list", headers=headers, data=body)

      response = response.text
      # print(response)
      response = response
      # print(response)
      response = json.loads(response)
      #print(response)
      response = response['result']
      if len(response) == 0:
        break
      #
      #
      # sys.exit()


      j = 1
      # k = 0
      print('len', len(response))
      for list_data in response:
        order_id += [list_data['order_id']]
        order_number += [list_data['order_number']]
        posting_number += [list_data['posting_number']]
        status += [list_data['status']]
        cancel_reason_id += [list_data['cancel_reason_id']]
        created_at += [list_data['created_at']]
        in_process_at += [list_data['in_process_at']]
        products_0_sku += [list_data['products'][0]["sku"]]
        products_0_name += [list_data['products'][0]["name"]]
        products_0_quantity += [list_data['products'][0]["quantity"]]
        products_0_offer_id += [list_data['products'][0]["offer_id"]]
        products_0_price += [list_data['products'][0]["price"]]
        products_0_digital_codes += [list_data['products'][0]["digital_codes"]]
        analytics_data_region += [list_data['analytics_data']['region']]
        analytics_data_city += [list_data['analytics_data']['city']]
        analytics_data_delivery_type += [list_data['analytics_data']['delivery_type']]
        analytics_data_is_premium += [list_data['analytics_data']['is_premium']]
        analytics_data_payment_type_group_name += [list_data['analytics_data']['payment_type_group_name']]
        analytics_data_warehouse_id += [list_data['analytics_data']['warehouse_id']]
        analytics_data_warehouse_name += [list_data['analytics_data']['warehouse_name']]
        analytics_data_is_legal += [list_data['analytics_data']['is_legal']]
        commission_amount += [list_data['financial_data']["products"][0]['commission_amount']]
        commission_percent += [list_data['financial_data']["products"][0]['commission_percent']]
        payout += [list_data['financial_data']["products"][0]['payout']]
        product_id += [list_data['financial_data']["products"][0]['product_id']]
        old_price += [list_data['financial_data']["products"][0]['old_price']]
        price += [list_data['financial_data']["products"][0]['price']]
        total_discount_value += [list_data['financial_data']["products"][0]['total_discount_value']]
        total_discount_percent += [list_data['financial_data']["products"][0]['total_discount_percent']]
        actions += [list_data['financial_data']["products"][0]['actions']]
        picking += [list_data['financial_data']["products"][0]['picking']]
        quantity += [list_data['financial_data']["products"][0]['quantity']]
        client_price += [list_data['financial_data']["products"][0]['client_price']]
        item_services_marketplace_service_item_fulfillment += [list_data['financial_data']["products"][0]['item_services']['marketplace_service_item_fulfillment']]
        item_services_marketplace_service_item_pickup += [list_data['financial_data']["products"][0]['item_services']['marketplace_service_item_pickup']]
        item_services_marketplace_service_item_dropoff_pvz += [list_data['financial_data']["products"][0]['item_services']['marketplace_service_item_dropoff_pvz']]
        item_services_marketplace_service_item_dropoff_sc += [list_data['financial_data']["products"][0]['item_services']['marketplace_service_item_dropoff_sc']]
        item_services_marketplace_service_item_dropoff_ff += [list_data['financial_data']["products"][0]['item_services']['marketplace_service_item_dropoff_ff']]
        item_services_marketplace_service_item_direct_flow_trans += [list_data['financial_data']["products"][0]['item_services']['marketplace_service_item_direct_flow_trans']]
        item_services_marketplace_service_item_return_flow_trans += [list_data['financial_data']["products"][0]['item_services']['marketplace_service_item_return_flow_trans']]
        item_services_marketplace_service_item_deliv_to_customer += [list_data['financial_data']["products"][0]['item_services']['marketplace_service_item_deliv_to_customer']]
        item_services_marketplace_service_item_return_not_deliv_to_customer += [list_data['financial_data']["products"][0]['item_services']['marketplace_service_item_return_not_deliv_to_customer']]
        item_services_marketplace_service_item_return_part_goods_customer += [list_data['financial_data']["products"][0]['item_services']['marketplace_service_item_return_part_goods_customer']]
        item_services_marketplace_service_item_return_after_deliv_to_customer += [list_data['financial_data']["products"][0]['item_services']['marketplace_service_item_return_after_deliv_to_customer']]

      data = pd.DataFrame({
        'order_id':order_id,
        'order_number':order_number,
        'posting_number':posting_number,
        'status':status,
        'cancel_reason_id':cancel_reason_id,
        'created_at':created_at,
        'in_process_at':in_process_at,
        'products_0_sku':products_0_sku,
        'products_0_name':products_0_name,
        'products_0_quantity':products_0_quantity,
        'products_0_offer_id':products_0_offer_id,
        'products_0_price':products_0_price,
        'products_0_digital_codes':products_0_digital_codes,
        'analytics_data_region':analytics_data_region,
        'analytics_data_city':analytics_data_city,
        'analytics_data_delivery_type':analytics_data_delivery_type,
        'analytics_data_is_premium':analytics_data_is_premium,
        'analytics_data_payment_type_group_name':analytics_data_payment_type_group_name,
        'analytics_data_warehouse_id':analytics_data_warehouse_id,
        'analytics_data_warehouse_name':analytics_data_warehouse_name,
        'analytics_data_is_legal':analytics_data_is_legal,
        'commission_amount':commission_amount,
        'commission_percent':commission_percent,
        'payout':payout,
        'product_id':product_id,
        'old_price':old_price,
        'price':price,
        'total_discount_value':total_discount_value,
        'total_discount_percent':total_discount_percent,
        'actions':actions,
        'picking':picking,
        'quantity':quantity,
        'client_price':client_price,
        'item_services_marketplace_service_item_fulfillment':item_services_marketplace_service_item_fulfillment,
        'item_services_marketplace_service_item_pickup':item_services_marketplace_service_item_pickup,
        'item_services_marketplace_service_item_dropoff_pvz':item_services_marketplace_service_item_dropoff_pvz,
        'item_services_marketplace_service_item_dropoff_sc':item_services_marketplace_service_item_dropoff_sc,
        'item_services_marketplace_service_item_dropoff_ff':item_services_marketplace_service_item_dropoff_ff,
        'item_services_marketplace_service_item_direct_flow_trans':item_services_marketplace_service_item_direct_flow_trans,
        'item_services_marketplace_service_item_return_flow_trans':item_services_marketplace_service_item_return_flow_trans,
        'item_services_marketplace_service_item_deliv_to_customer':item_services_marketplace_service_item_deliv_to_customer,
        'item_services_marketplace_service_item_return_not_deliv_to_customer':item_services_marketplace_service_item_return_not_deliv_to_customer,
        'item_services_marketplace_service_item_return_part_goods_customer':item_services_marketplace_service_item_return_part_goods_customer,
        'item_services_marketplace_service_item_return_after_deliv_to_customer':item_services_marketplace_service_item_return_after_deliv_to_customer,
      })
      #
      data['user_id'] = sheet_id
      data['date_load'] = str(datetime.date(datetime.today()))
      # data['barcode'] = data['barcode'].values.astype(np.int64)
      #print(data)
      # data.to_csv(f"name_file table.csv")
    except Exception as ex:
      print(ex)
      print('error ', sheet_id)
      break

  if data.at[0, 'user_id'] == sheet_id:

    # убрать лишние []
    data = data.replace(['[', ']'],['', ''])
    data = data.fillna('')
    # запись в бд
    #engine = create_engine('mysql+mysqldb://root2:%s@135.181.141.99:3306/dashboard' % quote_plus('KaneevDen!@#mysql'))
    engine = create_engine('postgresql://postgres:TrW34Uq@localhost:5432/dashboard')

    data.to_sql('posting_fbo_list_ozon', engine, if_exists='append')
    data.to_sql('posting_fbo_list_ozon_all', engine, if_exists='append')
    print('обновлено ', t, " всего позиций ",len(data))
    # data.to_csv('fbo.csv')
    # worksheet.batch_clear(["A2:AU50099"])
    # worksheet.update(f'A2:AU{len_values+1}', values)
    # break




