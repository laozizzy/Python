def getValue(b, r, n):
    v = b*(1+r)**n
    return v


b = input("请输入本金：")
r = input("请输入年利率：")
n = input("请输入年数：")

v = getValue(float(b), float(r)/100, int(n))
print(str.format("最终收益为：{0:0.2f}", v))
