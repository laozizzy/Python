# 1 方法一
for y in range(2000, 3001):
    if((y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0)):
        print(y, end=' ')
# # 2 方法二
for y in range(2000, 3001):
    if(y % 400 == 0):
        print(y, end=' ')
    else:
        if(y % 4 == 0):
            if(y % 100 != 0):
                print(y, end=' ')
# 3 方法三
for y in range(2000, 3001):
    if(y % 400 == 0):
        print(y, end=' ')
    elif(y % 4 != 0):
        continue
    elif(y % 100 == 0):
        continue
    else:
        print(y, end=' ')
# 4 方法四
import calendar
for y in range(2000, 3001):
    if(calendar.isleap(y)):
        print(y, end=' ')
   
