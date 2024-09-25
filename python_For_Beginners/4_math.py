import math

a = -1
b = -2
c = 3
delta = b ** 2 - 4 * a * c
X1 = ((-b + math.sqrt(delta)) / (2 * a))
X2 = ((-b - math.sqrt(delta)) / (2 * a))
print(X1)
print(X2)
# # 测试数学计算~~

def sum3(num_list):
    result = 0
    for num in num_list:
        result += num
    return  result
XXX = sum3([1,2,3,4])
print(XXX)

BBB = sum([1,2,3,4])
print(BBB)