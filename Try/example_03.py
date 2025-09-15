import game_utils as gu
import random as rd
start, end = 1, 100

computer = rd.randint(start,end)

count = 0
game_history = []
while True:
    count += 1
    human = gu.get_data(start,end)    
    #  승자선택 로직
    if gu.check_winner(human, computer,game_history,count):
        break