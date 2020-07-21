BROKER_URL = 'redis://127.0.0.1' # 使用Redis作为消息代理

from kombu import Exchange,Queue
CELERY_QUEUES = (
    Queue("default",Exchange("default"),routing_key="default"),
    Queue("for_task_ADD",Exchange("for_task_ADD"),routing_key="add"),
)
#
# CELERY_ROUTES = {
#     'tasks.add':{"queue":"for_task_ADD","routing_key":"add"},
#  }

ENABLE_UTC=True
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_CONCURRENCY = 5    # 并发worker数
CELERYD_MAX_TASKS_PER_CHILD = 40 # 每个worker执行了多少任务就会死掉
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0' # 把任务结果存在了Redis
CELERY_TASK_SERIALIZER = 'msgpack' # 任务序列化和反序列化使用msgpack方案
CELERY_RESULT_SERIALIZER = 'json' # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任务过期时间
CELERY_ACCEPT_CONTENT = ['json', 'msgpack'] # 指定接受的内容类型
