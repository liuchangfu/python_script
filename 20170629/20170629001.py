import  sys,os


print(os.path.abspath(__file__))

print(os.path.dirname(os.path.abspath(__file__)))

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))