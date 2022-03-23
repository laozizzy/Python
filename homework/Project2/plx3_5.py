for i in range(0, 3):
    n = int(input("请输入非负整数n："))
    if(n >= 0):
        break
    else:
        continue
if(n == 0):
    total = 1
if(n > 0):
    total = 1
    for i in range(n, 0, -1):
        total *= i
print("for循环: {0}! = {1}".format(n, total))
# while循环
n1 = n
if(n == 0):
    total = 1
if(n > 0):
    total = 1
    while(n >= 1):
        total *= n
        n -= 1
print("while循环: {0}! = {1}".format(n1, total))
