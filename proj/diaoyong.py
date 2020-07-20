from proj.tasks import add

import time
t1 = time.time()


r2 = add.apply_async((3, 4), queue='for_task_ADD')
r3 = add.apply_async((5, 12), queue='for_task_ADD')
r4 = add.apply_async((12, 22), queue='for_task_ADD')
r5 = add.apply_async((32, 42), queue='for_task_ADD')
r_list = [ r2, r3, r4, r5]
for r in r_list:
    print(r.id)
    print(r.get())
    # while not r.ready():
    #     pass
    # print(r.result)

t2 = time.time()

print('共耗时：%s' % str(t2-t1))