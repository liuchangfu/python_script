#!/usr/bin/python
# _*_ coding: utf-8 _*_

h = float(input('请输入身高:'))

w = float(input('请输入体重:'))

bmi = w / h**2  # BMI公式等于体重除以身高的平方

if bmi < 18.5:
    print('您的体重过轻')

elif bmi >= 18.5 and bmi <= 25:
    print('你的体重过重')

elif bmi > 28 and bmi <= 32:
    print('厉害了我的哥，你稍微胖了，该减肥了！！')

else:
    print('严重肥胖！！！！！')