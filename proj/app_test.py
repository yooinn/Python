from celery import Celery

app = Celery('proj', include=['proj.tasks'])
app.config_from_object('proj.celeryconfig')

'''
调用命令
celery -A proj.app_test worker -l info -P eventlet
'''

if __name__ == '__main__':
    app.start()