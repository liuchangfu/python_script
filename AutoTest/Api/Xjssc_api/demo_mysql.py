import pymysql
import requests


def get_sql():
    #  打开数据库，参数分别名数据库服务器，用户名，密码和数据库名称
    db = pymysql.connect('192.168.10.16', 'root', 'etlx29_st4x6su', 'siteportal_vip')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = 'select period,numbers from l_xjssc_winning_number limit 1'
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录（元组类型）
        res = cursor.fetchall()
        for row in res:
            period = row[0]
            numbers = row[1]
            # 打印结果
            # print('period:', period, 'numbers:', numbers)
            print("预期结果:", numbers)
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()
    return numbers


def get_interface():
    # 请求接口
    url = requests.get('https://mo.1394x.com/xjssc/GetAwardData?version=3000')
    url_json = url.json()
    act_number = url_json['items']['current']['result']
    print('接口返回的数据:', url_json)
    print("实际结果：", act_number)
    # 调用get_sql函数，并返回结果山给numbers字段
    numbers = get_sql()
    if numbers == act_number:
        print('实际结果与预期结果一致，测试通过!!')
    else:
        print('实际结果与预期结果不一致，测试不通过!!!')


if __name__ == '__main__':
    get_interface()
