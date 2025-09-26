import time

count = 0
is_continue = True
while is_continue:    
    count += 1
    print(f'{count}초')
    time.sleep(1)   # 1초간 지연
    
    # 5초단위로 사용자한테 계속 할건지 물어본다.. "To be Continue(Y/y)"
    if count % 5 == 0:
        user_input =  input('To be Continue(Y/y)').upper()
        if not user_input == 'Y':        
            is_continue  = False