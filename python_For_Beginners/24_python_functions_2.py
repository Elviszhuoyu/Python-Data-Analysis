"""
写一个计算BMI的函数，函数名为 calculate_BMI。
1. 可以计算任意体重和身高的BMI值
2. 执行过程中打印一句话，“您的BMI分类为：XX”
3. 返回计算出的BMI值

BMI = 体重 / （身高**2）（身高平方
# 偏瘦为 BMI < 18.5
# 正常为 BMI = 18.5-25
# 超重为 BMI = 25-30
# 肥胖为 BMI ≥ 30
"""
# user_gender = input("请输入您的性别（0=女士，1=男士）:")

def calculate_BMI(weight,height,gender):
    BMI = weight / (height ** 2)
    if BMI < 18.5:
        category = "偏瘦"
    elif BMI <= 25:
        category = "正常"
    elif BMI <= 30:
        category = "超重"
    else:
        category = "肥胖"
    if  gender > 0:
        name = "先生"
    else:
        name = "女士"
    print( f"{name}" f"，您的BMI分类为：{category}")
    return f'{float(BMI):.2f}'

User_BMI_1 = calculate_BMI(79,1.725,1)
print(User_BMI_1)

User_BMI_2 = calculate_BMI(99,1.77,0)
print(User_BMI_2)