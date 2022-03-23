import random
a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)
print(str.format("原始值：a={0}，b={1}，c={2}", a, b, c))
# 法1
if(a > b):
    a, b = b, a
if(a > c):
    a, c = c, a
if(b > c):
    b, c = c, b
print(str.format("（方法一）升序值：a={0}，b={1}，c={2}", a, b, c))
# 法2
max = max(a, b, c)
min = min(a, b, c)
med = sum([a, b, c]) - min - max
print(str.format("（方法二）升序值：a={0}，b={1}，c={2}", min, med, max))
