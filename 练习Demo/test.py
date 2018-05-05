class Dog(object):

    def __init__(self, name, dog_type):
        self.name = name
        self.type = dog_type

    def sayhi(self):
        print("hello,I am a dog, my name is ", self.name)


d = Dog('LiChuang', "京巴")
d.sayhi()

