class Animal(object):

    def eat(self):
        print('%s吃'% (self.name))

    def drink(self):
        print('%s喝' % (self.name))

    def shit(self):
        print('%s拉' % (self.name))

    def pee(self):
        print('%s撒' % (self.name))

    def sleep(self):
        print('%s睡' %(self.name))

class Cat(Animal):
    def __init__(self,name):
        self.name = name

    def cry(self):
        print('瞄瞄瞄!!!')

class Dog(Animal):
    def __init__(self,name):
        self.name = name

    def cry(self):
        print('旺旺旺!!')


c1 = Cat('小白家的小黑猫')
c1.eat()

c2 = Cat('小黑的小白猫')
c2.drink()

d1 = Dog('胖子家的小瘦狗')
d1.shit()

d2 = Dog('苍进空的哈士奇')
d2.pee()

d3 =Dog('武腾兰的金毛')
d3.sleep()

c1.cry()

d1.cry()