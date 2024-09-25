# 0 = 女士，1 = 男士
# BMI = 体重 / （身高**2）（身高平分
user_gender = input("请输入您的性别（0=女士，1=男士）:")
user_weight = float(input("请输入您的体重（单位：kg):"))
user_height = float(input("请输入您的身高（单位：m):"))
user_BMI  = user_weight / (user_height**2)
print("您的BMI值为：" + str(user_BMI))
# 对用户的BMI指标给出健康判断
# 偏瘦为BMI<18.5
# 正常为BMI=18.5-25
# 超重为BMI=25-30
# 肥胖为BMI≥30
if int(user_BMI) <=18.5:
    if int(user_gender) <=0:
        print("女士，您的BMI指标为；偏瘦！")
    else:
        print("先生，您的BMI指标为；偏瘦！")
elif 18.5< user_BMI <25:
    if int(user_gender) <=0:
        print("女士，您的BMI指标为；正常！")
    else:
        print("先生，您的BMI指标为；正常！")
elif 25< user_BMI <30:
    if int(user_gender) <= 0:
       print("女士，您的BMI指标为；超重！")
    else:
       print("先生，您的BMI指标为；超重！")
else:
    if int(user_gender) <= 0:
       print("女士，您的BMI指标为；肥胖！")
    else:
       print("先生，您的BMI指标为；肥胖！")