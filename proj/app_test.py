from celery import Celery

app = Celery('proj', include=['proj.tasks'])
app.config_from_object('proj.celeryconfig')
from celery.schedules import crontab
# 定时任务
app.conf.beat_schedule = {
    "each10s_task": {
        "task": "proj.tasks.add",
        "schedule": 5,
        "args": (2, 5)
    },
    "each1m_task": {
        "task": "proj.tasks.time_teller",
        "schedule": crontab(minute="*/1")
    }
}
'''
例子:
    crontab()每分钟执行一次。
    crontab(minute=0, hour=0)每天午夜执行。
    
    crontab(minute=0, hour='*/3')每三个小时执行一次：午夜，3am，6am，9am，中午，3pm，6pm，9pm。
    
    crontab(minute=0,
    hour='0,3,6,9,12,15,18,21')同上。
    
    crontab(minute='*/15')每15分钟执行一次。
    
    crontab(day_of_week='sunday')周日_每分钟执行一次!
    
    crontab(minute='*',
    hour='*', day_of_week='sun')同上。
    
    crontab(minute='*/10',
    hour='3,17,22', day_of_week='thu,fri')每十分钟执行一次，但仅在周四或周五的凌晨3-4点，下午5-6点以及晚上10-11点之间执行。
    
    crontab(minute=0, hour='*/2,*/3')每隔一小时执行一次，每一小时被三整除。这意味着：每小时除外：1 am、5am、7am、11am、1pm、5pm、7pm、11pm
    
    crontab(minute=0, hour='*/5')执行小时可被5整除。这意味着它在下午3点而不是下午5点触发（因为3pm等于24小时时钟值“ 15”，可被5整除）。
    
    crontab(minute=0, hour='*/3,8-17')每小时执行一次可除以3的操作，并在办公时间内（上午8点至下午5点）每小时执行一次。
    
    crontab(0, 0, day_of_month='2')在每个月的第二天执行。
    
    crontab(0, 0,
    day_of_month='2-30/2')在每个偶数天执行。
    
    crontab(0, 0,
    day_of_month='1-7,15-21')在每月的第一和第三周执行。
    
    crontab(0, 0, day_of_month='11',
    month_of_year='5')每年5月11日执行。
    
    crontab(0, 0,
    month_of_year='*/3')在每个季度的第一个月每天执行一次。
'''
app.conf.timezone = 'Asia/Shanghai'
'''
调用命令
celery -A proj.app_test worker -l info -P eventlet  #celery  service
celery beat -A proj.app_test #start celery beat service
celery -A proj.app_test flower #start_visualization_service  need_to_install_flower

'''

if __name__ == '__main__':
    app.start()