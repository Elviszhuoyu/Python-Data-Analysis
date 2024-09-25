# BMI = 体重 / （身高**2）（身高平分
user_weight = float(input("请输入您的体重（单位：kg):"))
user_height = float(input("请输入您的身高（单位：m):"))
user_BMI  = user_weight / (user_height**2)
print("您的BMI值为：" + str(user_BMI))
# 对用户的BMI指标给出健康判断
if int(user_BMI) <=24:
    print("恭喜，您的BMI指标为；健康\n请继续保持哦~！")
else:
    print("抱歉，您的BMI指标为；不合格\n请再接再励，要多多锻炼哦~！")