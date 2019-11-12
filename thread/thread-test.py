# -*- coding: utf-8 -*-
# __author__ = 'yafengstark'

# 这是中文注释

import _thread as thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(
        "%s: %s" % (threadName, time.ctime(time.time())))


# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print(
    "Error: unable to start thread")

while 1:
    pass