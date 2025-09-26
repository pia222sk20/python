# 가위 바위 보 게임  (컴퓨터 VS 휴먼)
# 가위 : 1 바위 : 2 보 : 3
# 규칙 : 컴퓨터가 임의로 숫자를 선택   : Random
# 인간이 숫자를 입력                  : input
# 승패를 기록                         
# 3번마다 계속할 지 물어본다         : for

import random
# 1: 가위
# 2: 바위
# 3: 보
# 랜덤하게 선택한 컴퓨터의 값
com_choince = random.randint(1,3)
# 사용자의 값
human_choice = int(input("입력(1:가위 2:바위 3:보) :"))
# 승패 확인
# print(com_choince)   # 디버깅용.. 개발이 완료되면 삭제
if com_choince == human_choice:
    print('비겼습니다.')
else:
    if (com_choince == 1 and human_choice ==2) or \
        (com_choince == 2 and human_choice ==3) or \
        (com_choince == 3 and human_choice ==1):
        print("당신이 이겼습니다.")
    else:
        print("당신이 졌습니다.")
