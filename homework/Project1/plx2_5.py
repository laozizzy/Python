import datetime
sName = str(input("请输入您的姓名："))
birthday = int(input("请输入您的出生年份："))
age = datetime.date.today().year - birthday
print("您好！{0}。您{1}岁。".format(sName, age))
# print(f"您好！{sName}。您{age}岁。")    3.10.1版本中，f-string支持，但是考虑到教学环境为3.7，故注释起来
# print(str.format("您好！{0}。您{1}岁。", sName, age))  该方法同样适用
