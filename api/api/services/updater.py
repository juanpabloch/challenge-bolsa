from apscheduler.schedulers.background import BackgroundScheduler
from api.services.jobs import update_products

def start():
    schedule = BackgroundScheduler()
    schedule.add_job(update_products, 'interval', seconds=60)
    schedule.start()
    