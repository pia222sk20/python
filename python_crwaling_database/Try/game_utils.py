def get_data(start,end,input_str='입력'):
    while True:
        try:
            h_num = int(input(f'{input_str}({start}~{end}) '))
            if not start <= h_num <= end:
                raise ValueError(f'{start} ~ {end} 범위 초과')        
        except Exception as e:
            print(f'오류 : {e}')        
        else:
            return h_num

def check_winner( human, computer,game_history,count):
    #게임
    if human > computer:
        print('크다')
        game_history.append( (human,'크다' )  )
    elif human < computer:
        print('작다')
        game_history.append( (human,'작다' )  )
    else:
        print(f'정답 횟수 : {count}')
        for guess_value, state in game_history:
            print(f'{guess_value} - {state}')
        return True
    return False