# -*- coding: utf-8 -*-
# __author__ = 'yafengstark'
import math
zoom = 18
sum = 0
for i in range(zoom):
    sum = sum + math.pow(4, i+1)
    pass
print(sum)

print("需要处理的月数：")
print(sum / 3600/24/30 )
