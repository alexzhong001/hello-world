# 这是一个注释
Tempstr = input("我要获得一个当前的重量数值")
if Tempstr [-2] in ['GT', 'gt']:
    KG = (eval(Tempstr[0:-1]) * 1000)
    print("转换后的重量是{:.2f}KG".format(KG))
elif Tempstr [-2] in ['XT','xt']:
    KG = (eval(Tempstr[0:-1]) / 1000)
    print("转换后的重量是{:.2f}KG".format(KG))
else:
    print ("输入重量数值有误")
