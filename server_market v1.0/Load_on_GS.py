import json
from datetime import datetime, timedelta
import io
import time

import requests
import gspread

limit = 100000
dateto = datetime.date(datetime.today())
dateFrom = dateto - timedelta(30)

def get_API(dateto, dateFrom, rrdid, apiKeyWB):
    print(dateto, dateFrom, rrdid, apiKeyWB)
    while True:
        try:
            global key
            global API_table
            global text

            url = f'https://suppliers-stats.wildberries.ru/api/v1/supplier/reportDetailByPeriod?dateFrom={dateFrom}&key={apiKeyWB}&limit={limit}&rrdid={rrdid}&dateto={dateto}'
            print(url)
            response = requests.get(url)
            print(response)
            text = response.text
            # print(text)
            API_table = json.loads(text)
            key = len(API_table)
        except:
            if text == 'null':
                key = 0
                "данных нет"
                break

            else:
                print('сбой АПИ')
                time.sleep(10)
        else:
            if str(response) == '<Response [429]>':
                time.sleep(20)
                continue
            else:
                break

"чтение json с таблицами"
with io.open("tables.json", encoding='utf-8', mode='r') as json_file:
    tables = json.load(json_file)
    gc = gspread.service_account(filename="credentials.json")

with io.open("client.json", encoding='utf-8', mode='r') as json_file:
    client = json.load(json_file)

for l in client:
    l = str(l)
    print(l)
    All_tables = client[l]["tables"]
    All_tables = All_tables.split(',')
    print(All_tables)
    sheet_id = client[l]["id"]
    url = client[l]["url"]

    values = []
    for n in All_tables:

        try:

            ## получение переменных
            i = str(int(n) - 1001)
            apiKeyWB = tables[i]["apiKeyWB"]
            name = tables[i]["name"]
            print(name)
            print(url)
            print(apiKeyWB)
            # получение переменных

            sh = gc.open_by_key(sheet_id)
            try:
                worksheet = sh.worksheet("Реализации (исх.)")
            except:
                worksheet = sh.worksheet("Отчет реализации")
            # получение данных из АПИ ВБ
            rrdid = 0
            get_API(dateto, dateFrom, rrdid, apiKeyWB)
            # print(API_table)
            while key > 0:
                y = 0
                while y < key:
                    # print(y)
                    # print(API_table[y])
                    list_data = API_table[y]

                    # print('ок list_data', y, "in table ", i)

                    # try:
                    #     realizationreport_id = list_data['realizationreport_id']
                    # except:
                    #     realizationreport_id = ""
                    #
                    #
                    # try:
                    #     suppliercontract_code = list_data['suppliercontract_code']
                    # except:
                    #     suppliercontract_code = ""
                    #
                    # try:
                    #     rrd_id = list_data['rrd_id']
                    # except:
                    #     rrd_id = ""
                    #
                    # try:
                    #     gi_id = list_data['gi_id']
                    # except:
                    #     gi_id = ""
                    #
                    # try:
                    #     subject_name = list_data['subject_name']
                    # except:
                    #     subject_name = ""
                    #
                    # try:
                    #     nm_id = list_data['nm_id']
                    # except:
                    #     nm_id = ""
                    #
                    # try:
                    #     brand_name = list_data['brand_name']
                    # except:
                    #     brand_name =""
                    #
                    # try:
                    #     sa_name = list_data['sa_name']
                    # except:
                    #     sa_name = ""
                    #
                    # try:
                    #     ts_name = list_data['ts_name']
                    #
                    # except:
                    #     ts_name = ""
                    #
                    # try:
                    #     barcode = list_data['barcode']
                    #
                    # except:
                    #     barcode = ""
                    #
                    # try:
                    #     doc_type_name = list_data['doc_type_name']
                    # except:
                    #     doc_type_name = ""
                    #
                    # try:
                    #     quantity = list_data['quantity']
                    # except:
                    #     quantity = ""
                    #
                    # try:
                    #     retail_price = list_data['retail_price']
                    # except:
                    #     retail_price = ""
                    #
                    # try:
                    #     retail_amount = list_data['retail_amount']
                    # except:
                    #     retail_amount = ""
                    #
                    # try:
                    #     sale_percent = list_data['sale_percent']
                    # except:
                    #     sale_percent = ""
                    #
                    # try:
                    #     commission_percent = list_data['commission_percent']
                    # except:
                    #     commission_percent = ""
                    #
                    # try:
                    #     office_name = list_data['office_name']
                    # except:
                    #     office_name = ""
                    #
                    # try:
                    #     supplier_oper_name = list_data['supplier_oper_name']
                    # except:
                    #     supplier_oper_name = ""
                    #
                    # try:
                    #     order_dt = list_data['order_dt']
                    # except:
                    #     order_dt = ""
                    #
                    # try:
                    #     sale_dt = list_data['sale_dt']
                    # except:
                    #     sale_dt = ""
                    #
                    # try:
                    #     rr_dt = list_data['rr_dt']
                    # except:
                    #     rr_dt = ""
                    #
                    # try:
                    #     shk_id = list_data['shk_id']
                    # except:
                    #     shk_id = ""
                    #
                    # try:
                    #     retail_price_withdisc_rub = list_data['retail_price_withdisc_rub']
                    # except:
                    #     retail_price_withdisc_rub = ""
                    #
                    # try:
                    #     delivery_amount = list_data['delivery_amount']
                    # except:
                    #     delivery_amount = ""
                    #
                    # try:
                    #     return_amount = list_data['return_amount']
                    # except:
                    #     return_amount = ""
                    #
                    # try:
                    #     delivery_rub = list_data['delivery_rub']
                    # except:
                    #     delivery_rub = ""
                    #
                    # try:
                    #     gi_box_type_name = list_data['gi_box_type_name']
                    # except:
                    #     gi_box_type_name = ""
                    #
                    # try:
                    #     product_discount_for_report=list_data['product_discount_for_report']
                    # except:
                    #     product_discount_for_report= ""
                    #
                    # try:
                    #     supplier_promo=list_data['supplier_promo']
                    # except:
                    #     supplier_promo = ""
                    #
                    # try:
                    #     rid=list_data['rid']
                    # except:
                    #     rid= ""
                    #
                    # try:
                    #     ppvz_spp_prc=list_data['ppvz_spp_prc']
                    # except:
                    #     ppvz_spp_prc= ""
                    #
                    # try:
                    #     ppvz_kvw_prc_base=list_data['ppvz_kvw_prc_base']
                    # except:
                    #     ppvz_kvw_prc_base= ""
                    #
                    # try:
                    #     ppvz_kvw_prc=list_data['ppvz_kvw_prc']
                    # except:
                    #     ppvz_kvw_prc= ""
                    #
                    # try:
                    #     ppvz_sales_commission=list_data['ppvz_sales_commission']
                    # except:
                    #     ppvz_sales_commission= ""
                    #
                    # try:
                    #     ppvz_for_pay=list_data['ppvz_for_pay']
                    # except:
                    #     ppvz_for_pay= ""
                    #
                    # try:
                    #     ppvz_reward=list_data['ppvz_reward']
                    # except:
                    #     ppvz_reward= ""
                    #
                    # try:
                    #     ppvz_vw=list_data['ppvz_vw']
                    # except:
                    #     ppvz_vw= ""
                    #
                    #
                    # try:
                    #     ppvz_vw_nds=list_data['ppvz_vw_nds']
                    # except:
                    #     ppvz_vw_nds= ""
                    #
                    # try:
                    #     ppvz_office_id= list_data['ppvz_office_id']
                    # except:
                    #     ppvz_office_id= ""
                    #
                    try:
                        ppvz_office_name = list_data['ppvz_office_name']
                    except:
                        ppvz_office_name = ""
                    #
                    # try:
                    #     ppvz_supplier_id=list_data['ppvz_supplier_id']
                    # except:
                    #     ppvz_supplier_id= ""
                    #
                    # try:
                    #     ppvz_supplier_name=list_data['ppvz_supplier_name']
                    # except:
                    #     ppvz_supplier_name= ""
                    #
                    # try:
                    #     ppvz_inn=list_data['ppvz_inn']
                    # except:
                    #     ppvz_inn= ""
                    #
                    # try:
                    #     srid=list_data['srid']
                    # except:
                    #     srid= ""

                    try:
                        acquiring_fee = list_data['acquiring_fee']
                    except:
                        acquiring_fee = ""

                    try:
                        acquiring_bank = list_data['acquiring_bank']
                    except:
                        acquiring_bank = ""



                    # print('ок var', y, "in table ", i)

                    new_values = [list_data['realizationreport_id'], list_data['suppliercontract_code'],
                                  list_data['rrd_id'],
                                  list_data['gi_id'], list_data['subject_name'], list_data['nm_id'],
                                  list_data['brand_name'],
                                  list_data['sa_name'], list_data['ts_name'], list_data['barcode'],
                                  list_data['doc_type_name'],
                                  list_data['quantity'], list_data['retail_price'], list_data['retail_amount'],
                                  list_data['sale_percent'],
                                  list_data['commission_percent'], list_data['office_name'],
                                  list_data['supplier_oper_name'],
                                  list_data['order_dt'], list_data['sale_dt'], list_data['rr_dt'], list_data['shk_id'],
                                  list_data['retail_price_withdisc_rub'], list_data['delivery_amount'],
                                  list_data['return_amount'],
                                  list_data['delivery_rub'], list_data['gi_box_type_name'],
                                  list_data['product_discount_for_report'],
                                  list_data['supplier_promo'], list_data['rid'], list_data['ppvz_spp_prc'],
                                  list_data['ppvz_kvw_prc_base'],
                                  list_data['ppvz_kvw_prc'], list_data['ppvz_sales_commission'], list_data['ppvz_for_pay'],
                                  list_data['ppvz_reward'], list_data['ppvz_vw'], list_data['ppvz_vw_nds'],
                                  list_data['ppvz_office_id'],
                                  ppvz_office_name, list_data['ppvz_supplier_id'], list_data['ppvz_supplier_name'],
                                  list_data['ppvz_inn'], list_data['srid'], acquiring_fee, acquiring_bank, list_data['penalty']]

                    # print('ок data', y, "in table ", i)
                    y += 1
                    values += [new_values]
                    # print(new_values)
                rrdid = list_data['rrd_id']
                get_API(dateto, dateFrom, rrdid, apiKeyWB)
            print('data table ', i)
            print(type(values))


            print(list_data['rrd_id'])

            # форматирование
            # requests = []
            #
            # requests.append({
            #     "insertDimension": {
            #         "range": {
            #             "sheetId": "Реализации (исх.)",
            #             "dimension": "COLUMNS",
            #             "startIndex": 46,
            #             "endIndex": 48
            #         },
            #         "inheritFromBefore": True
            #     }
            # })
            #
            # body = {
            #     'requests': requests
            # }
            # sh.batch_update(body)
            # worksheet.update('AU1', 'penalty')
            # worksheet.format("AU2:AU", {"numberFormat": {"type": "NUMBER"}})
            # print("обновление формата")

        except Exception as ex:
            print(ex)
            print('id error tables', i)


    # elfktyb
    len_values = len(values)
    print('len', len_values)
    # Удаление старых данных
    j = 1
    while True:
        try:
            worksheet.batch_clear(["A2:AU1000002"])
            print('data clear')

        except:
            print("неуспешная попытка удаления ", j)
            j += 1

        else:
            break

    # worksheet.format("AS2:AS", {"numberFormat": {"type": "NUMBER"}})

    # внесение данных
    worksheet.update(f'A2:AU{len_values + 1}', values)
    print("data upgrage")

    # запись даты обновления
    worksheet = sh.worksheet("обновление таблиц")
    worksheet.update(f'B9', str(datetime.today()))
