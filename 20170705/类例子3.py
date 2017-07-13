'''
1、创建三个游戏人物，分别是：

    苍井井，女，18，初始战斗力1000
    东尼木木，男，20，初始战斗力1800
    波多多，女，19，初始战斗力2500

2、游戏场景，分别：

    草丛战斗，消耗200战斗力
    自我修炼，增长100战斗力
    多人游戏，消耗500战斗力

'''

class Game(object):
    def __init__(self,name,gender,age,fight):
        self.name = name
        self.gender = gender
        self.age = age
        self.fight= fight

    def caocong(self):
        #草丛战斗
        self.fight = self.fight-200

    def xiulian(self):
        #自我修炼
        self.fight = self.fight+100

    def game(self):
        # 多人游戏
        self.fight = self.fight+500

    def detail(self):
        #注释：当前对象的详细情况
        print('姓名：%s,性别:%s,年龄:%s,战斗力:%s' % (self.name,self.gender,self.age,self.fight))


cang = Game('仓井空','女',19,1000)

dong = Game('东尼大木','男',20,1500)

bobo = Game('樱井利亚','女',19,2000)

cang.caocong()

dong.xiulian()

bobo.game()

cang.detail()

dong.detail()

bobo.detail()