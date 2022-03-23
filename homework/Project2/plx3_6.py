import random
a = random.randint(0, 100)
b = random.randint(0, 100)
sum = a*b

print("整数1 = {0}，整数2 = {1}".format(a, b))

if(a < b):
    a, b = b, a

while(a % b != 0):
    a, b = b, a % b

print("最大公约数：{0}，最小公倍数：{1:0.0f}".format(b, sum/b))
