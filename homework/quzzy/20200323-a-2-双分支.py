import math

# 单分支
x = int(input('请输入数'))

if x%2 == 1:
    # 奇数
    print(math.pow(x, 0.5))
else:
    print(math.pow(x, 1/3))