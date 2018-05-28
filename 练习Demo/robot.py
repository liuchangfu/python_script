# _*_ coding:utf-8 _*_
from urllib.robotparser import  RobotFileParser

rb = RobotFileParser()
rb.set_url("https://www.1393p.com/robots.txt")
rb.read()
print(rb.can_fetch('*','https://www.1393p.com/pk10/?utp=topbar'))
print(rb.can_fetch('*','https://www.1393p.com/pk10/kaijiang'))