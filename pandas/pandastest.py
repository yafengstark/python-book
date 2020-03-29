import pandas as pd


data = [
    [1, 1, 1],
    [2, 3, 6]
]
students = pd.DataFrame(data,  columns=['math', 'english', 'python'])
# index=['tom', 'jerry'],
print(students)

df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))


df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
print(df.append(df2))

print(df)


# 三个部分
# print(students.values)
# print(students.index)
# print(students.columns)

# 获取部分数据，简历新的DataFrame obj[行索引，列索引]
# 获取series
# 某列
# print(students['math'])

# 某行某列
# print(students.loc['tom', 'math'])

# 位置序号获取
# print(students.iloc[1,2])


# 条件筛选

# series
# height= pd.Series({'13':187,'14':190,'7':185,'2':178,'9':185})
# print(height[height.values > 180])