import random as f
class Fish:
    def __init__(self):
        self.x = f.randint(0,10)
        self.y = f.randint(0,10)

    def move(self):
        self.x -= 1
        print('我的位置是:',self.x,self.y)
        
class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有得吃!')
            self.hungry =False
        else:
            print('太撑了,吃不下！！')




print('——————————————————打印结果——————————————')
fish = Fish()

fish.move()

goldfish =Goldfish()

goldfish.move()

shark = Shark()

shark.move()
print('————————————————————————————————------')