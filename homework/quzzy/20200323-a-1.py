import math

x = int(input('请输入x:'))
y = int(input('请输入y:'))
z = int(input('请输入z:'))

sum = x ** 2 + y ** 2 + z ** 2
if sum > 1000:
    print("千位以上数字:" + sum / 1000)
else:
    print("三数之和", x + y + z)
