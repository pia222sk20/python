# 다양한 매개변수
    # 기본매개변수  default parameter

def myAdd(num1=0, num2=0, num3=0):
    return num1 + num2 + num3

result1 = myAdd()
result2 = myAdd(1)
result3 = myAdd(1,2)
result4 = myAdd(1,2,3)
print(result1,result2,result3,result4)