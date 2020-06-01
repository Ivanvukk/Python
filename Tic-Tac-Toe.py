#IVU 01.06.2020
#Funations
def print_board(board):
    print(f"             |             |             ")
    print(f"      {board[7]}      |      {board[8]}      |      {board[9]}      ")
    print(f"             |             |             ")
    print(f"-------------|-------------|-------------")
    print(f"             |             |             ")
    print(f"      {board[4]}      |      {board[5]}      |      {board[6]}      ")
    print(f"             |             |             ")
    print(f"-------------|-------------|-------------")
    print(f"             |             |             ")
    print(f"      {board[1]}      |      {board[2]}      |      {board[3]}      ")
    print(f"             |             |             ")
    
def turn(player_sign, board):
    position = 0
    while position < 1 or position > 9:
            
        #Try casting string to number 
        try:
            n = input("Choose empty field (1-9): ")
            position = int(n)
        except ValueError:
            print("Invalid input")
            print("Please enter number!")
            continue
            
        #Check if in range [1,9]
        if not (position in range(1,10)):
            print("Invalid input")
            print("Please enter number in range 1-9!")
            continue
            
        #Check if position already taken
        if board[position] == "X" or board[position] == "O":
            print("Invalid input")
            print(f"Position {position} taken!")
            position = 0
            continue

        #Valid input
        board[position] = player_sign
    return board
    
def check_winner(board):
    # 8 Winning combinations
    game_has_winner = False
    
    #Check horisontal
    if board[1] == board[2] == board[3] or board[4] == board[5] == board[6] or board[7] == board[8] == board[9]:
        game_has_winner = True
    #Check vertical
    if board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[3] == board[6] == board[9]:
        game_has_winner = True
    #Check cross
    if board[1] == board[5] == board[9] or board[3] == board[5] == board[7]:
        game_has_winner = True

    return game_has_winner

def check_tie(board):
    game_tie = True
    for n in range(1,10):           #Go through all positions if any is numeric - Game is not TIE yet
        if board[n].isnumeric():
            game_tie = False
            break
    return game_tie
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#Main program
while True:

    #Global variables
    player_1 = ""
    player_2 = ""
    board = ["0","1","2","3","4","5","6","7","8","9"]


    #Sign selection for player 1 and 2 
    print("============================================")
    print("================TIC-TAC-TOE=================")
    print("============================================")
    print("Sign X starts first")
    
    while player_1 != "x" and player_1 != "o":
        player_1 = input("Player 1 choose sign (X/O): ").lower()
        if player_1 != "x" and player_1 != "o":
            print("Invalid input")
    
    if player_1 == "x":
        player_2 = "o"
    else:
        player_2 = "x"

    print(f"Player 1 is {player_1.upper()} and player 2 is {player_2.upper()}")

    #Game
    while True:
        #X Turn
        print_board(board)
        if player_1 == "x":
            print("======================Player 1 turn======================")
        else:
            print("======================PLayer 2 turn======================")
        board = turn("X", board)

        #Check if X wins
        if check_winner(board):
            if player_1 == "x":
                print("Game finished: Player 1 wins!")
            else:
                print("Game finished: Player 2 wins!")
            print_board(board)
            break                       #Game finished

        #Check if TIE
        if check_tie(board):
            print("Game finished: TIE!")
            print_board(board)
            break                       #Game finished
        
        # O Turn
        print_board(board)
        if player_1 == "o":
            print("======================Player 1 turn======================")
        else:
            print("======================PLayer 2 turn======================")
        board = turn("O", board)
        # Check if O wins
        if check_winner(board):
            if player_1 == "o":
                print("Game finished: Player 1 wins!")
            else:
                print("Game finished: Player 2 wins!")
            print_board(board)    
            break                       #Game finished

    #Game finished - play again?
    play_again_answer = ""
    while play_again_answer != "y" and play_again_answer != "n":
        play_again_answer = input("Would you like to play again? (Y/N): ").lower()
        if play_again_answer != "y" and play_again_answer != "n":
            print("Invalid input")
    
    if play_again_answer == "n":
        print("================Thank you for playing!==================")
        break #End game
    