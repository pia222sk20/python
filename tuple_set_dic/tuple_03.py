# 튜플 VS 리스트는 서로 변경이 가능하다
# 튜플 -> 리스트   리스트 -> 튜플
list_a = [1,2,3]
tuple_a = (10,20,30)
print(f'type(list_a) = {type(list_a)}')
print(f'type(tuple_a) = {type(tuple_a)}')

print(type(tuple(list_a)))
list_a = tuple(list_a)