salary = float(input("请输入有固定工资收入的党员的月工资："))
if salary <= 400:
    dues = salary*0.005
elif salary <= 600:
    dues = salary*0.01
elif salary <= 800:
    dues = salary*0.15
elif salary <= 1500:
    dues = salary*0.02
else:
    dues = salary*0.03

print(str.format("月工资 = {0:0.0f}，交纳党费 = {1:0.1f}", salary, dues))
