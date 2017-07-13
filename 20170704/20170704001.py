class Dog:
    def __init__(self,name):
         self.name= name

    def bulk(self):
        print('%s,wangwangwnag!!!' % self.name)

d1=Dog('AAAA')
d1.bulk()

d2 = Dog('BBB')
d2.bulk()


