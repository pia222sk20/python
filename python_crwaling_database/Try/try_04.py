# raise  예외 발생하기
try:
    print("정상코드")
    print('예외 발생')
    raise "내가 발생시킨 오류"
    # raise ValueError("테스트")
except Exception as e:
    print(f'에러 : {e}   {e.__class__}   {e.__class__.__name__}'  )