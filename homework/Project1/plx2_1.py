pp = input("请输入本金：")
aR = input("请输入年利率：")
year = input("请输入年数：")
ppRAll = float(pp)*(1+float(aR)/100)**int(year)
print(str.format("本金利率和为：{0:2.2f}",ppRAll))