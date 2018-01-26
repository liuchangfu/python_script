import requests
import unittest
import json

class Topics_latest(unittest.TestCase):

    def setUp(self):
        self.url= "https://www.v2ex.com/api/topics/latest.json"

    def test_title(self):

        title_list =["一台屏幕有竖线的 P2414H 能出多少？",
                     '之前有位老哥卖有锁无锁 iPhone 那个帖子找不到',
                     '从零开始用 Express+Nuxt+Mysql+Nginx 写一个 SSR 博客',
                     '有谁认识华科在校的计算机学院的研究生？',
                     '2 年程序开发经验,25 岁,对自己的语言未来不看好，看好 Python ，现在想转 Python ，已经自学入门，写过几个小爬虫。能找到 Python 工作吗？',
                     '有这样一个业务设计上的问题，需要大伙帮忙出出主意。详情见内', 'aria2 零速度. 有人和我一样吗?',
                     '[360] 坐标北京, 大数据中心, 机器学习平台研发,前端', '骗子智商捉急，诈骗程序员被套路反撸！[骗子中出了一个不及格的！]',
                     '大型 React 项目的所有数据源都需要用 Redux 管理吗', '大家 早饭 一般吃啥 如何解决啊？',
                     '[杭州] 阿里巴巴信息平台体验部技术中台招前端',
                     '请问什么软件可以在 windows 右下角的时间上显示农历日期和阳历日期以及星期几？',
                     '寻找中国最牛 pm 活动，进入倒计时第 58 天']
        re = requests.get(self.url)

        re_json = re.json()
        self.assertEqual(re.status_code,200)
        # for i in range(0,13):
        #     title_list.append(re_json[i]["title"])
        # print(title_list)
        for i in range(0,13):
            self.assertEqual(re_json[i]["title"],title_list[i])


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()