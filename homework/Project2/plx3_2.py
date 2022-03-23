import math
a = float(input("请输入三角形的边长A："))
b = float(input("请输入三角形的边长B："))
c = float(input("请输入三角形的边长C："))
if(a < b):
    a, b = b, a
elif(a < c):
    a, c = c, a
elif(b < c):
    b, c = c, b
if(a < 0 or b < 0 or c < 0 or b+c <= a):
    print("无法构成三角形！")
else:
    h = (a+b+c)/2
    area = math.sqrt(h*(h-a)*(h-b)*(h-c))
    print("三角形三边分别为：a=%.1f, b=%.1f, c=%.1f" % (a, b, c))
    print("三角形的周长={0}，面积={1}".format(a+b+c, area))
