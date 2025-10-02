# 정렬
# list_a = [ ('국어',100),('영어',95),('수학',88)   ]
# # key는 정렬 기준으로 정하는 역활
# # 람다에서 매개변수 data는 list_a의 데이터
# print( sorted(list_a , key = lambda data: data[1])   )

dict_1 = {'국어':100,'영어':956,'수학':88}
print(dict(sorted(dict_1.items(), key=lambda data : data[1]  )))