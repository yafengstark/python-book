# -*- coding: utf-8 -*-
# __author__ = 'yafengstark'

# 这是中文注释

import random


# print(random.randint(12, 20))


# 01
# 02
# ..
# 99

import string

for j in range(100):
    a = ""
    for i in range(6):
        s = string.ascii_letters
        r = random.choice(s)
        a = a + str(random.randint(1,9))

    if j <= 9:
        print(a +"0" +str(j))
    else:
        print(a + str(j))
