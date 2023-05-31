import schedule
import time
from datetime import datetime
text = 0
print('start program')
def job():
    start_time = str(datetime.today())
    # import delete_old_data
    # import Load_on_GS
    # import nomeclature
    # import load_on_server
    print('start program at ', start_time)
    try:
        exec(open('delete_old_data.py', encoding='utf-8').read())
        exec(open('load_on_server.py', encoding='utf-8').read())
        print('данные на сервере обновлены', datetime.today())
    except Exception as ex:
        print(ex)
        print('сбой обновления данных на сервере', datetime.today())

    try:
        exec(open('nomeclature.py', encoding='utf-8').read())
    except Exception as ex:
        print(ex)
        print('данные о номенклатуре обновлены', datetime.today())

    # try:
    #     exec(open('Load_on_GS.py', encoding='utf-8').read())
    # except Exception as ex:
    #     print(ex)
    #     print('сбой обновления данных в гугл', datetime.today())

    try:
        exec(open('self-redemption.py', encoding='utf-8').read())
    except Exception as ex:
        print(ex)
        print('сбой обновления самовыкупов', datetime.today())

    try:
        exec(open('finance_transaction_list_ozon.py', encoding='utf-8').read())
    except Exception as ex:
        print(ex)
        print('сбой обновления finance_transaction_list_ozon', datetime.today())

    try:
        exec(open('stocks_ozon.py', encoding='utf-8').read())
    except Exception as ex:
        print(ex)
        print('сбой обновления stocks_ozon', datetime.today())

    try:
        exec(open('stocks_ozon2 .py', encoding='utf-8').read())
    except Exception as ex:
        print(ex)
        print('сбой обновления stocks_ozon2', datetime.today())

    try:
        exec(open('posting_fbo_list.py', encoding='utf-8').read())
    except Exception as ex:
        print(ex)
        print('сбой обновления posting_fbo_list', datetime.today())

    try:
        exec(open('posting_fbs_list.py', encoding='utf-8').read())
    except Exception as ex:
        print(ex)
        print('сбой обновления posting_fbo_list', datetime.today())
        
    try:
        exec(open('report_product.py', encoding='utf-8').read())
    except Exception as ex:
        print(ex)
        print('сбой обновления products_ozon', datetime.today())

    # ozon self-redemption
    # schedule.every(10).minutes.do(job)
    end_time = str(datetime.today())
    print('end program at ', end_time)
# schedule.every().hour.do(job)
schedule.every().day.at("05:00").do(job)
schedule.every().day.at("18:00").do(job)
schedule.every().day.at("22:00").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every(2).hours.at("07:30").do(job)
job()
while True:
    schedule.run_pending()
    time.sleep(1)