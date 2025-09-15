# 랜덤 라이브러리 가져오기
import random

# range(100)  0 ~ 99 범위에서 중복되지 않은 랜덤한 5개 추출
random_numbers =  random.sample(range(100),5)

# 0~10 사이중에서 랜덤하게 한개 추출
random_int = random.randint(0,10)

random_numbers.append(random_int)

# 50 이 있는지
print(50 in random_numbers)
print(random_numbers)

print('-'*50)

# 삭제
del random_numbers[0]
print(random_numbers)

removed_number = random_numbers.pop(0)
print(random_numbers)
print(removed_number)