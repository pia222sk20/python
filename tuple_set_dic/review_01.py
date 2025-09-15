# 딕셔너리
    # .items()  .keys()  .values()
dict_1 = {
    '국어' : 100,
    '영어' : 80,
    '수학' : 88
}
print(dict_1)
# 정렬  .items()
    # sorted()
print(dict_1.items())    
print(dict(sorted(dict_1.items(), key=lambda data: data[1])    ))
print(dict(sorted(dict_1.items(), key=lambda data: data[1],reverse=True)))
# max()
    # max()
# enumerate()
    # 순환문에서 리스트를 감싸면 (인덱스,리스트의값)
# zip()
    # 여러개의 iterable 들을 각 원소를 쌍으로 하는 집합
    # (1,2), ('사과','배')
    # [ (1,'사과'), (2,'배')  ]
# map()
    # iterable한 객체의 각 요소에 특정 함수를 적용
    # map(int, ['1','2'])  -> [1,2]

# import collections
# datas = [1,1,1,1,2,1,3,4,1,2,4,1]
# print(collections.Counter(datas))

print(type(dict_1.items()))
print(dict_1.items())
print(list(dict_1.items()))
print(list(dict_1.items())[0] )

print(type(range(100)))
print(list(range(100)))