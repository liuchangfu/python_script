"""
功能描述：为指定成绩加分，直到分数大于等于 60 为止，输出加分前和加分后的成绩，并统计加分的次数 
"""""

score  = 50
count = 0
print("加分前的成绩为:",score)

while score < 60:
    score = score+1
    count = count+1

print("加分后的成绩为:",score)
print("一共加了",count,"次")
print("一共加了%d次" %(count))
