#DayDayUpQ3.py
dayup = 1.0
dayfdfactor = 0.01
dayfbfactor = -0.01
for i in range (365):
    if i % 7 in [6,0]:
        dayup = dayup*(1+dayfbfactor)
    else:
        dayup = dayup*(1+dayfdfactor)
print("工作日的力量：{:.2f}".format(dayup))
 