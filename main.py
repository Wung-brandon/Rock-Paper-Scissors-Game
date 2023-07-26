import random






#computer = random.randint(len(chose),2+1)

while True:

    user_choice = input("Enter a choice (rock, paper or scissors):\n")
    possible_choices=['rock','paper','scissors']
    computer_choice = random.choice(possible_choices)
    
    if user_choice == computer_choice:
        print(f"Both player selected {computer_choice}. So its a tie!")
    elif user_choice == 'rock' and computer_choice == 'paper' or user_choice=='paper' and computer_choice =='scissors' or user_choice == 'scissors' and computer_choice == 'rock':
        print(f"You choosed {user_choice} and Computer choosed {computer_choice}. So Computer wins!")
    elif user_choice not in possible_choices:
        print('Invalid user choice')
        break
    elif user_choice == 'rock' and computer_choice == 'scissors' or user_choice=='scissors' and computer_choice =='paper' or user_choice == 'paper' and computer_choice == 'rock':
        print(f"You choosed {user_choice} and Computer choosed {computer_choice}. So you win!")
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        break
    

    
    
""" 
if user_choice == 'rock' and choose == 'paper':
    print('computer wins')
elif user_choice == 'paper' and choose == 'paper':
    print('draw')
elif user_choice == 'rock' and choose == 'rock':
    print('draw')
elif user_choice == 'scissors' and choose == 'scissors':
    print('draw')
elif user_choice == 'rock' and choose == 'scissors':
    print('user player wins')
elif user_choice == 'scissors' and choose == 'rock':
    print('computer wins')
elif user_choice == 'paper' and choose == 'rock':
    print('user player wins')   
elif user_choice == 'scissors' and choose == 'paper':
    print('user player wins')
elif user_choice == 'paper' and choose == 'scissors':
    print('computer wins')
else:
    print('interesting')
print(choose) """
#print(choose)


   