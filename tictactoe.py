#Gerard Agada, 2021-08-16
#TicTacToeGame

import random



def display_board(board):
    #print('\n'*100)
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' + board[8])

def player_input():
    choice = '0'
    valid = ['X', 'O']
    while choice not in valid:
        choice = input("It's your turn, pick 'X' or 'O': ")
        if choice not in valid:
            print("Sorry, invalid choice! Please try again.")
        else:
            print(f"You have selected: {choice}")
    return choice    

def place_marker(board, marker, position):
    position = 0
    valid = str(list(range(1,10)))
    choice = '0'
    while choice not in valid:
        choice = input("Pick a position from (1-9): ")
        if choice not in valid:
            print("Sorry, invalid choice! Please try again.")
        else:
            choice = int(choice)
            board[choice - 1] = marker
            choice = str(choice)
    return board

def win_check(board, mark):
    #Brute Force -------------

    #Position 1: 3 Ways you can win
    if(board[0] == board[1]) and (board[0] == board[2]) and (board[0] == mark):
        print(f"{mark} won!")
        return True
    elif(board[0] == board[4]) and (board[0] == board[8]) and (board[0] == mark):
        print(f"{mark} won!")
        return True
    elif(board[0] == board[3]) and (board[0] == board[6]) and (board[0] == mark):
        print(f"{mark} won!")
        return True
    
    #Position 2: 2 Ways you can win
    elif(board[1] == board[4]) and (board[1] == board[7]) and (board[1] == mark):
        print(f"{mark} won!")
        return True
    elif(board[1] == board[0]) and (board[1] == board[2]) and (board[1] == mark):
        print(f"{mark} won!")
        return True
    
    #Position 3: 3 Ways you can win
    elif(board[2] == board[1]) and (board[2] == board[0]) and (board[2] == mark):
        print(f"{mark} won!")
        return True
    elif(board[2] == board[5]) and (board[2] == board[8]) and (board[2] == mark):
        print(f"{mark} won!")
        return True
    elif(board[2] == board[4]) and (board[2] == board[6]) and (board[2] == mark):
        print(f"{mark} won!")
        return True
    
    #Position 4: 2 Ways you can win
    elif(board[3] == board[0]) and (board[3] == board[6]) and (board[3] == mark):
        print(f"{mark} won!")
        return True
    elif(board[3] == board[4]) and (board[3] == board[5] and (board[3] == mark)):
        print(f"{mark} won!")
        return True
    
    #Position 5: 3 Ways you can win
    elif(board[4] == board[3]) and (board[4] == board[5]) and (board[4] == mark):
        print(f"{mark} won!")
        return True
    elif(board[4] == board[1]) and (board[4] == board[7]) and (board[4] == mark):
        print(f"{mark} won!")
        return True
    elif(board[4] == board[2]) and (board[4] == board[6]) and (board[4] == mark):
        print(f"{mark} won!")
        return True
    
    #Position 6: 2 Ways you can win
    elif(board[5] == board[2]) and (board[5] == board[8]) and (board[5] == mark):
        print(f"{mark} won!")
        return True
    elif(board[5] == board[4]) and (board[5] == board[3]) and (board[5] == mark):
        print(f"{mark} won!")
        return True
    
    #Position 7: 3 Ways you can win
    elif(board[6] == board[3]) and (board[6] == board[0]) and (board[6] == mark):
        print(f"{mark} won!")
        return True
    elif(board[6] == board[7]) and (board[6] == board[8]) and (board[6] == mark):
        print(f"{mark} won!")
        return True
    elif(board[6] == board[4]) and (board[6] == board[2]) and (board[6] == mark):
        print(f"{mark} won!")
        return True
    
    #Position 8: 2 Ways you can win
    elif(board[7] == board[6]) and (board[7] == board[8]) and (board[7] == mark):
        print(f"{mark} won!")
        return True
    elif(board[7] == board[4]) and (board[7] == board[1]) and (board[7] == mark):
        print(f"{mark} won!")
        return True
    
    #Position 9: 3 Ways you can win
    elif(board[8] == board[4]) and (board[8] == board[0]) and (board[8] == mark):
        print(f"{mark} won!")
        return True
    elif(board[8] == board[5]) and (board[8] == board[2]) and (board[8] == mark):
        print(f"{mark} won!")
        return True
    elif(board[8] == board[7]) and (board[8] == board[6]) and (board[8] == mark):
        print(f"{mark} won!")
        return True
    
    else:
        return False

def choose_first():
    result = random.randint(1,2)
    return int(result)

def space_check(board, position):
    if board[position-1] == 'X' or board[position-1] == 'O':
        return False
    else:
        return True 

def full_board_check(board):
    for num in board:
        if num.isdigit():
            return False
    return True


def player_choice(board):
    position = 0
    choice = False
    
    while position not in range(1,10):
        position = int(input("Pick the next position (1-9): "))
        
        #Check for correct range(1-9)
        if position not in range(1,10):
            print("Sorry, invalid choice! Please try again.")
        #Check if there is a free position using the space_check() function.
        elif position in range(1,10):
            choice = space_check(board, position)
            if choice == False:
                print("Sorry, this position is not free! Please try again.")
                position = 0
            else:
                print("This position is free!")
    
    return int(position)

def replay():
    choice = 'WRONG'
    while choice not in ['Y','N']:
        choice = input("Play Again? (Y or N): ")
        print(choice)
        if choice not in ['Y','N']:
            print("Sorry, invalid choice! Please select Y or N")
            
    
    if choice == 'Y':
        return True
    else:
        return False


def test():

    #To test boad display functionality.
    test_board = ['1','2','3','4','5','6','7','8','9']
    display_board(test_board)
    
    #To test place marker functionality.
    test_board = place_marker(test_board, 'X', 8)
    display_board(test_board)

    #To test the functionality of the win check.
    win_check_function = win_check(test_board, 'O')
    print(win_check_function)

    #To test the randomint function
    choose = choose_first()
    print(choose)

    #To test the wheather a space on the board is freely available
    space_bool = space_check(test_board, 2)
    print(space_bool)

    #To test weather the function checks if the board is full
    full_board_bool = full_board_check(test_board)
    print(full_board_bool)

    #To test player choice function
    position = 0
    position = player_choice(test_board)

def main():
    print('Welcome to Tic Tac Toe!')

    board = ['1','2','3','4','5','6','7','8','9']
    game_on = True
    player_1_marker =  ' '
    player_2_marker = ' ' 
    who_first = 0
    player = 0
    player_ = 0
    position = 0
    position_ =0

    while True:
        # Set the game up here
        display_board(board)
        player_1_marker = player_input()
      
        if player_1_marker == 'X':
            print(f"Player 1 is: {player_1_marker}")
            player_2_marker = 'O'
            print(f"Player 2 is: {player_2_marker}") 
        else:
            print(f"Player 1 is: {player_1_marker}")
            player_2_marker = 'X'
            print(f"Player 2 is: {player_2_marker}")

        who_first = choose_first()
        if who_first == 1:
            print(f"Player {who_first} will go first!")
            player = 1
            player_ = 2
        else:
            print(f"Player {who_first} will go first!")
            player = 2
            player_ = 1
        
        while game_on:
            display_board(board)
            print("\n")
            if player == 1 or player_ == 1:
                if who_first == 1:
                    board = place_marker(board, player_1_marker, position)
                else:
                    board = place_marker(board, player_2_marker, position)
                display_board(board)
                print("\n")
                if win_check(board, player_1_marker) == True or win_check(board, player_2_marker) == True:
                    #replay()
                    break
                elif full_board_check(board) == True:
                    print('The game has ended in a Tie!')
                    #replay()
                    break
            if player == 2 or player_ == 2:
                if who_first == 2:
                    board = place_marker(board, player_1_marker, position_)
                else:
                    board = place_marker(board, player_2_marker, position_)
                display_board(board)
                print("\n")

                if full_board_check(board) == True:
                    print('The game has ended in a Tie!')
                    #replay()
                    break
            '''
            position = player_choice(board)
            position_ = player_choice(board)
            '''
        if not replay():
            break
        else:
            board = ['1','2','3','4','5','6','7','8','9']


if __name__ == "__main__":
    main()

