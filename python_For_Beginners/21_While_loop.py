# list1 = ["你好","哈皮","凶","猫"]

# for i in range(len(list1)):
#     print(list1[i])

# i = 0
# while i < len(list1):
#     print(list1[i])
#     i = i + 1

##################################

# list2 = [input("输入求平均的数字:")]
# print(list2)
# i = 0
# while i < len(list2):
#     X1 = list2[i] +
#     print(X1)
#     i = i + 1
##################################
print("哈喽呀~我是一个求平均值的小程序~。")
user_input = input("请输入要求平均的数字（输入q终止程序）：")
total = 0
c2ount = 0
while user_input != "q":
    num = float(user_input)
    total += num
    c2ount += 1
    user_input = input("请输入要求平均的数字（输入q终止程序）：")
if c2ount == 0:
    result = 0
else:
    result = total / c2ount
print("您输入的数字平均值为："+ str(result) )
