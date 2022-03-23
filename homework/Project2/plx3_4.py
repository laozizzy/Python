import math
a = float(input("请输入系数a："))
b = float(input("请输入系数b："))
c = float(input("请输入系数c："))

delta = b*b - 4*a*c

if(a == 0):
    if(b == 0):
        print("此方程无解！")
    else:
        print("此方程的解为：", -1*c/b)
elif(delta == 0):
    print("此方程有两个相等实根：", (-1*b)/(2*a))
elif(delta > 0):
    print("此方程有两个不等实根：{0} 和 {1}".format
          ((-1*b + math.sqrt(delta))/2*a, (-1*b - math.sqrt(delta))/2*a))
elif(delta < 0):
    print(str.format("此方程有两个不等虚根：{0} + {1}i 和 {2} - {3}i", (-1*b)/(2*a), math.sqrt(
        delta*-1)/(2*a), (-1*b)/(2*a), math.sqrt(delta*-1)/(2*a)))
