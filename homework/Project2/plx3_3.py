import math
# 一句单分支语句：
x = float(input("请输入x："))
if(x < 0):
    y = math.log(-5*x) + 6 * math.sqrt(abs(x) + math.exp(4)) - pow(x+1, 3)
print("方法一：x = {0},y = {1}".format(x, y))
# 两句单分支语句：
if(x >= 0):
    y = (x*x - 3*x)/(x+1) + 2*math.pi + math.sin(x)
if(x < 0):
    y = math.log(-5*x) + 6 * math.sqrt(abs(x) + math.exp(4)) - pow(x+1, 3)
print("方法二：x = {0},y = {1}".format(x, y))

# 双分支语句：
if(x >= 0):
    y = (x*x - 3*x)/(x+1) + 2*math.pi + math.sin(x)
else:
    y = math.log(-5*x) + 6 * math.sqrt(abs(x) + math.exp(4)) - pow(x+1, 3)
print("方法三：x = {0},y = {1}".format(x, y))

# 条件运算语句：
y = ((x*x - 3*x)/(x+1) + 2*math.pi + math.sin(x)) if(x >= 0) \
    else (math.log(-5*x) + 6 * math.sqrt(abs(x) + math.exp(4)) - pow(x+1, 3))
print("方法四：x = {0},y = {1}".format(x, y))
