# 判断用户输入的年份是否为闰年，闰年条件是能被4整除但不能被100整除，或者能被400整除

year = int(input('请输入年份:'))

if (year % 4 ==0 and year % 100 != 0) or (year % 400 ==0):
    print('{0}年是闰年'.format(year))
else:
    print('{0}年是闰年'.format(year))
