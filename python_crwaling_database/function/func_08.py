# 간단한 함수
#  함수내의 로직인 한줄로 표현 가능한 함수들
def my_add(a,b):
    return a+b

# 람다 함수 - 한줄로 표현한 함수  lambda 키워드 사용
# 간단한 함수를 즉석에서 만들때 유용
# 무조건 값을 리턴하는 함수  return  키워드 사용 안함
test =  lambda a,b: a+b

a,b = 10,20
print(f'{a}+{b} = {test(a,b)}')

