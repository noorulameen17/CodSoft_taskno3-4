import random
while True:
    print("Enter Any 1 Choice Given Below : \n \n  \t 1 - Rock \n \t2 - Paper \n \t 3 - Scissors\n  ")
    choice = int(input("Enter Your Choice : "))
    while choice>3 or choice<1:
        choice = int(input("Enter A Valid Choice Please : "))
    if choice == 1:
        choice_name = ' \t \tROCK'
    elif choice == 2:
        choice_name = ' \t \tPAPER'
    else:
        choice_name = ' \t \tSCISSORS'
    print(' \n \t  Your Choice Is \n',choice_name)
    print(' \n ..!!!!.. Now It`s Bot`s Turn  ..!!!!.. ')
    bot_choice = random.randint(1,3)
    while bot_choice == choice:
        bot_choice = random.randint(1,3)

    if bot_choice == 1:
        bot_choice_name = '\t  rock'
    elif bot_choice == 2:
        bot_choice_name = '\t  paper'
    else:
        bot_choice_name = '\t scissors'
    print(" \n\t Bot Choice Is  \n",bot_choice_name)
    print('\n',choice_name,'   VS',bot_choice_name)

    if choice == bot_choice:
        print('\nIt`s A Draw',end=" ")
        result = 'DRAW'

    if (choice == 1 and bot_choice == 2):
        print('\nPaper Wins =>',end=" ")
        result = 'paper'
    elif (choice == 2 and bot_choice == 1):
        print('\nPaper Wins =>',end=" ")
        result = 'PAPER'
    
    if (choice == 1 and bot_choice == 3):    
        print('\nRock Wins =>',end=" ")
        result = 'ROCK'
    elif (choice == 3 and bot_choice == 1):    
        print('\nRock Wins =>',end=" ")
        result = 'rock'

    if (choice == 2 and bot_choice == 3):    
        print('\nScissors Wins =>',end=" ")
        result = 'scissors'
    elif (choice == 3 and bot_choice == 2):    
        print('\nScissors Wins =>',end=" ")
        result = 'SCISSORS'

    play_again = input("\n \t\tDo You Want To Play Again! (Y/N):").upper()
    if play_again == "N":
        print("\n \t\t\tThanks For Playing")
        print("\n \t\t\tSee You Again!")
        break
