# Tic Tac Toe

def disply_board(board):
    '''
        This function is responsible for displaying the current state of the Tic Tac Toe board. 
        It takes the board list as input and prints the board with the marks of each player (X or O) at the corresponding positions.
    '''
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print("--+---+--")
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print("--+---+--")
    print(f'{board[6]} | {board[7]} | {board[8]}')


def player_input(player):
    '''
        This function takes the player (X or O) as input and prompts them to enter a position (a number from 1 to 9). 
        The function then returns the index in the board list where the player's mark should be placed.
    '''
    posotion = int(input(f'Player {player}, enter a position (1-9) ')) - 1
    return posotion


def check_win(board, player):
    '''
        This function checks whether the player has won the game. 
        It takes the current board and the player's mark as inputs. 
        The function defines all possible winning combinations (rows, columns, and diagonals) and checks if any of them contain the player's mark in all three positions. 
        If a winning combination is found, the function returns True, indicating that the player has won. 
        Otherwise, it returns False.
    '''
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True

    return False


def play():
    '''
        This is the main function that orchestrates the game. 
        It initializes the board as a list with empty spaces, sets up the players as "X" and "O", 
        and starts the game loop that runs for a maximum of 9 turns (the total number of cells on the board). 
        In each turn, it displays the board, gets the player's input for their move, 
        and updates the board with the player's mark at the chosen position. 
        After each move, it checks if the current player has won using the check_win() function. 
        If there is a winner, it displays the winning board and the player's mark. 
        If there is no winner after 9 turns, it declares the game as a tie.
    '''
    board = [" " for _ in range(9)]
    players = ['X', '0']
    player_index = 0

    for turn in range(9):
        disply_board(board)
        player = players[player_index]

        position = player_input(player)
        while board[position] != " ":
            print("Position is already occupied. Try again.")
            position = player_input(player)

        board[position] = player

        if check_win(board, player):
            disply_board(board)
            print(f'Player {player} wins!')
            return

        player_index = (player_index + 1) % 2

    disply_board(board)
    print('Its a tie!')


if __name__ == "__main__":
    play()
