import schedule
import time
import views

def do_smth():
    print('running')
    schedule.every(5).seconds.do(views.post_aboitiz)

    while True:
        schedule.run_pending()
        time.sleep(1)

do_smth()
# import views
# # import requests


# def job():
#     print("I'm working...")

# job()

#     # schedule.every(10).minutes.do(job)
#     # schedule.every().hour.do(job)
#     # schedule.every().day.at("10:30").do(job)

#     # while 1:
#     #     schedule.run_pending()
#     #     time.sleep(1)





