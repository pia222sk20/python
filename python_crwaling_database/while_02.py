import time

count = 0
while True:    
    count += 1
    print(f'{count}초')
    time.sleep(1)   # 1초간 지연
    
    # 5초단위로 사용자한테 계속 할건지 물어본다.. "To be Continue(Y/y)"
    if count % 5 == 0:
        is_continue =  input('To be Continue(Y/y)')
        is_continue = is_continue.upper()
        if not is_continue == 'Y':
        # if is_continue == 'Y' or is_continue == 'y':
            break