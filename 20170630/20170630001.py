#打印日期格式为’2017-06-30 11:34:18 星期五‘
import time,datetime

def get_week_day(date):
      week_day_dict = {
        0 : '星期一',
        1 : '星期二',
        2 : '星期三',
        3 : '星期四',
        4 : '星期五',
        5 : '星期六',
        6 : '星期天',
      }
      day = date.weekday()
      print(day)
      return week_day_dict[day]

week = get_week_day(datetime.datetime.now())
print(week)
#打印当前时间，时间格式为年-月-日 小时-分钟-秒 星期
print('今天是:',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),week)

#打印当前时间戳
print('当前时间戳：',time.mktime(time.localtime()))

