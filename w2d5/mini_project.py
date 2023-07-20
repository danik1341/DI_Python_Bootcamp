# Tic Tac Toe

def disply_board(board):
    '''
        Display the Tic Tac Toe board.

        Parameters:
        board (list): The Tic Tac Toe board represented as a list.

        Returns:
        None

    '''
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print("--+---+--")
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print("--+---+--")
    print(f'{board[6]} | {board[7]} | {board[8]}')


def player_input(player):
    '''
        Get the player's move.

        Parameters:
        player (str): The player's mark (X or O).

        Returns:
        int: The index where the player's mark should be placed on the board.

    '''
    posotion = int(input(f'Player {player}, enter a position (1-9) ')) - 1
    return posotion


def check_win(board, player):
    '''
        Check if the player has won the game.

        Parameters:
        board (list): The current Tic Tac Toe board represented as a list.
        player (str): The player's mark (X or O).

        Returns:
        bool: True if the player has won, False otherwise.

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
        Main function to play the Tic Tac Toe game.

        Parameters:
        None

        Returns:
        None

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
