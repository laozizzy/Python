result = 1
for i in range(8, 0, -1):
    print("第 {0} 天桃子数为：{1}".format(i, result))
    result = 2*(result+1)
    
