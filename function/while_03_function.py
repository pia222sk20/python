import time
def display_second(count):           
    count += 1
    print(f'{count}초')
    time.sleep(1)   # 1초간 지연
    return count

def is_user_continue(count):
    # 5초단위로 사용자한테 계속 할건지 물어본다.. "To be Continue(Y/y)"
    if count % 5 == 0:
        user_input =  input('To be Continue(Y/y)').upper()
        if not user_input == 'Y':        
            return False                
    return True

count = 0
is_continue = True
count = 0  
while is_continue:      
    count = display_second(count)  # 1간격으로 출력
    is_continue = is_user_continue(count) # 5초단위로 진행여부 판단