import math

# 单分支
x = int(input('请输入数'))

result = math.pow(x, 0.5) if x%2==1 else math.pow(x, 1/3)

print(result)
