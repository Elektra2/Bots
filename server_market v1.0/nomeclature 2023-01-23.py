import requests
import json
import pandas as pd
import io
import gspread
from datetime import datetime
import numpy as np
from sqlalchemy import create_engine
import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(
    user="postgres",
    # пароль, который указали при установке PostgreSQL
    password="TrW34Uq",
    host="localhost",
    port="5432",
    database="dashboard")

engine = create_engine('postgresql://postgres:TrW34Uq@localhost:5432/dashboard')
body = {
  "sort": {
    "cursor": {
        "limit": 1000},
    "filter": {
    "withPhoto": -1}
    }
}

body = json.dumps(body)
print(18)
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

    teshSize = []
    skus = []
    mediaFiles = []
    colors = []
    updateAt = []
    vendorCode = []
    brand = []
    Object = []
    nmID = []
    user_id = []
    date_load = []

    for n in All_tables:


      try:
        date_now = str(datetime.today())
        k += 1
        # номер ид пользователя
        user_id_n = n
        m = str(int(n) - 1001)
        print('nomeclature')
        print(m)
        print(sheet_id)
        apiKeyWB_post = tables[m]["apiKeyWB_post"]
        name = tables[m]["name"]

        print(56,name)
        print(url)

        headers = {"Authorization": f"{apiKeyWB_post}"}

        response = requests.post("https://suppliers-api.wildberries.ru/content/v1/cards/cursor/list", headers=headers, data=body)
        # print(62, headers)
        response = response.text
        # print(64, response)
        response = response
        # print(66, response)
        response = json.loads(response)
        # print(42)
        response = response['data']['cards']
        len_responce = len(response)
        print(69)
        if len_responce != 0:
            j = 1
            k = 0
            for i in response:
              sizes = len(i['sizes'])
              k += 1
              t = 0
              while t < sizes:

                teshSize += [i['sizes'][t]['techSize']]

                if len(i['sizes'][t]['skus']) != 1:
                    print("skus",i['sizes'][t]['skus'])
                    skus += [i['sizes'][t]['skus'][0]]
                    print(i['sizes'][t]['skus'][0])
                else:
                    skus += i['sizes'][t]['skus']
                # print(skus)
                t += 1
                # print(len(i['mediaFiles']))
                # print(i['mediaFiles'])
                if len(i['mediaFiles']) != 0:
                  n = 0
                  for j in i['mediaFiles']:
                    # print(j)
                    # print(j[-6:])

                    if j[-6:] == '-1.jpg':
                      # print(j)
                      n = 1
                      mediaFiles += [j]

                  if n == 0:
                    # print('n == 0',j)
                    mediaFiles += [j]

                else: mediaFiles += ['no']

                # print(len(i['colors']))
                if len(i['colors']) != 0:
                  colors += [str(i['colors'])]
                else: colors += ['no']

                updateAt += [i['updateAt']]
                vendorCode += [i['vendorCode']]
                brand += [i['brand']]
                Object += [i['object']]
                nmID += [i['nmID']]
                user_id += [user_id_n]
                # print(129,user_id_n)
                date_load += [date_now]
            print(81)
        else:
            n = len(All_tables) + 1



        # data.to_csv(f"name_file table{name} {date_now}.csv")

        # загрузка в гугл докс



      except Exception as ex:
        print(ex)
        print('id error tables', m)

    # qwe
    print(151, len(teshSize))
    print(152, len(skus))
    print(152, len(mediaFiles))
    print(152, len(colors))
    print(152, len(updateAt))
    print(152, len(vendorCode))
    print(152, len(brand))
    print(152, len(Object))
    print(152, len(nmID))
    print(152, len(user_id))
    print(152, len(date_load))

    data = pd.DataFrame({
      "techSize": teshSize,
      "skus": skus,
      "mediaFiles": mediaFiles,
      "colors": colors,
      "updateAt": updateAt,
      "vendorCode": vendorCode,
      "brand": brand,
      "object": Object,
      "nmID": nmID,
      'user_id': user_id,
      'date_load': date_load
    })
    # удаление данных в таблице sql, тут чтобы убедится что данные прогружаются из АПИ, ели первфй цыкл, то удаление

    if l == str(0):
        try:
            cursor = connection.cursor()
            cursor.execute('TRUNCATE nomenclature_wb')
            connection.commit()
            print("sql очищено")
        except Exception as ex:
            print(ex)
            print('ошибка очистки')
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

    # Загрузка в sql
    data.to_sql('nomenclature_wb', engine, if_exists='append')

    # загрузка в гугл док
    sh = gc.open_by_key(sheet_id)

    worksheet = sh.worksheet("Номенклатура")
    ws_values = worksheet.get_all_values()
    df = pd.DataFrame.from_records(ws_values[1:], columns=ws_values[0])
    df = df[["skus", "cost_price"]]
    data["cost_price"] = 0
    # print(126)
    index = len(data)
    i = 0
    # print(129)
    while i < index:
      skus = data.at[i, 'skus']
      if skus != '':
        try:
          # print(i)
          # print(index)

          # TS = data.at[i, '№ ТС']
          # print(date)
          cost_price = df[(df['skus'] == skus)].cost_price
          # print(cost_price.values)
          # cost_price = df.at[i_cost_price, 'skus']
          # print(cost_price)
          data.loc[i, 'cost_price'] = int(cost_price.values)
        except:
          skus
          # print("0")
          # data.loc[i, 'cost_price'] = 'Баркод повторяется'
      else:
        data.at[i, 'skus'] = 0

      i += 1
    # смена типа данных
    # print(151)
    data['skus'] = data['skus'].values.astype('object')
    # print(153)
    values = data.values
    values = values.tolist()
    # print(values)
    # print(type(values))
    len_values = len(values)
    print(len_values)

    if len_values != 0:
        worksheet.batch_clear(["B2:M20000"])
        worksheet.update(f'B2:M{len_values + 1}', values)
        # print(df.dtypes)
        print("data upgrage")
        # print(vals)

        # запись даты обновления
        worksheet = sh.worksheet("обновление таблиц")
        worksheet.update(f'B10', date_now)
