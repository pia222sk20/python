print( [  i for i in range(5) if i%2==0  ] )


list_1 = [1,2,3,1,2,3,5,4,8]
# 값 2에 해당하는 인덱스를 찾아서 리스트로 반환
# [1,4]
print( [ idx for idx,value in enumerate(list_1) if value == 2] )

age = 20


if age >=18:
    result = '성인'
else:
    result = '미성년'

result = '성인' if age >=18 else '미성년'

list_1 = [10,20,10,50,30,20,10,54]
print( [ '성인' if i>=18 else '미성년'  for i in list_1] )