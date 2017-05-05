def discounts(price,rate):
    fin_price = price * rate
    return fin_price

old_price = float(input("请输入原价:"))
rate = float(input("请输入折扣:"))
new_price= discounts(old_price,rate)
print("打折后的价格是:",new_price)