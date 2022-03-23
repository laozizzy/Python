from math import sqrt
x = (10+sqrt(10*10-4*16))/2
y = (10-sqrt(10*10-4*16))/2
print(str.format("方程x*x-10*x+16=0的解为：{0:0.1f} {1:0.1f}", x, y))
