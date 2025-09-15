# 선거시스템
# 유권자  들은 기호로 투표를 진행 결과를 리스트에 저장
#  ex 1,2,3
# 투표는 순환문은 이용해서 유권자가 10이라면 10번순환하면서 후보자(1~5)선택
# [1,1,2,3,4,1,5,1]
# 리스트에있는 각 번호의 횟수를 구해서 당선자를 출력
cadidate = ['홍길동','이순신','강감찬','율곡','신사임당']
vote = []
counts = 10  # 유권자
result = {}  # 투표카운트 
# for _ in counts:
#     vote.append(int(input('투표를 하세요(1~5) : ')))
vote = [1,2,3,4,2,2,1,2,2,4]
print(f'vote = {vote}')
# dict 기능을 이용
for i in vote:
    if i in result: 
        result[i] += 1
    else:
        result[i] = 1
print(f'result = {result}')

# 키의 값을 가져올때..  딕셔너리변수['키값']  없으면 에러
# 딕셔너리변수.get('키값')  없으면 None
max_key =  max(result, key=result.get )
# 당선자  key - 1

print(f'당선자 : {cadidate[max_key-1]} 득표수 : {result[max_key]}')