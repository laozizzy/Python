x = float(input("请输入操作数x:"))
y = float(input("请输入操作数y:"))
f = input("请输入操作符：")
if(y == 0 and (f == '/' or f == '%')):
    print("分母=0，零除异常！")
else:

    if(f == "+"):
        sum = x+y
        print(f"{x:0.1f} + {y:0.1f} = {sum:0.1f}")
    elif(f == "-"):
        sub = x-y
        print(f"{x:0.1f} - {y:0.1f} = {sub:0.1f}")
    elif(f == "/"):
        div = x/y
        print(f"{x:0.1f} / {y:0.1f} = {div:0.1f}")
    elif(f == "*"):
        mul = x*y
        print(f"{x:0.1f} * {y:0.1f} = {mul:0.1f}")
    elif(f == "%"):
        rem = x % y
        print(f"{x:0.1f} - {y:0.1f} = {rem:0.1f}")
