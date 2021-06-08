import random


human_choice = input()
computer_choice =  ('rock', 'paper', 'scissors')
computer_choice = random.choice(computer_choice)

COMPUTER_SCORE = 0
HUMAN_SCORE= 0



#def choice_result():
#global COMPUTER_SCORE
#global HUMAN_SCORE
    
if human_choice == 'rock' and computer_choice == 'paper':
    COMPUTER_SCORE = COMPUTER_SCORE + 1
    print('You Lose Score ='COMPUTER_SCOREHUMAN_SCORE )
if human_choice == 'scissors' and computer_choice=='rock':
    COMPUTER_SCORE = COMPUTER_SCORE+1
elif human_choice == 'paper' and computer_choice =='scissors':
    COMPUTER_SCORE = COMPUTER_SCORE+1
    #HUMAN LOSING....
elif human_choice == 'paper' and computer_choice=='rock':
    HUMAN_SCORE = HUMAN_SCORE + 1
elif human_choice == 'rock' and computer_choice =='scissors':
    HUMAN_SCORE = HUMAN_SCORE + 1
elif human_choice =='scissors' and computer_choice =='paper':
    HUMAN_SCORE = HUMAN_SCORE + 1
if HUMAN_SCORE > COMPUTER_SCORE:
    print(HUMAN_SCORE)
elif COMPUTER_SCORE > HUMAN_SCORE:
    print(COMPUTER_SCORE)
