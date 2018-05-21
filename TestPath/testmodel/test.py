# _*_ coding:utf-8 _*_
import sys
sys.path.append("..")
from model1 import student
from model1 import new_student
from model2 import animal
from model2 import new_animal


if __name__ == '__main__':
    print(student.get_name())
    print(new_student.get_student_name())
    print(animal.get_name())
    print(new_animal.get_student_name())