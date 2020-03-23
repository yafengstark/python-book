import datetime

year = int(input('请输入年:'))
month = int(input('请输入月:'))
day = int(input('请输入日：'))

d1 = datetime.datetime(year,month,day)   # 第一个日期
# print(d1.month)

today = datetime.datetime.now()
year_today = datetime.date.today().year
month_today = datetime.date.today().month
day_today = datetime.date.today().day

if month > month_today:
    print(year_today - year)
elif month < month_today:
    print(year_today - year-1)
else:
    # 月份相等
    if day >= day_today:
        print(year_today - year)
    else:
        print(year_today - year)




