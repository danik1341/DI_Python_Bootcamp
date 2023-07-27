import random


class Game:
    """
    A class that represents a single game of Rock-Paper-Scissors against the computer.

    Attributes:
        None

    Methods:
        get_user_item(self): Ask the user to select an item (rock/paper/scissors).
            Keeps asking until the user has selected one of the items.
            Returns the selected item.

        get_computer_item(self): Selects rock/paper/scissors at random for the computer.
            Returns the computer's selected item.

        get_game_result(self, user_item, computer_item): Determines the result of the game.
            Parameters:
                user_item (str): The user's chosen item (rock/paper/scissors).
                computer_item (str): The computer's chosen (random) item (rock/paper/scissors).
            Returns:
                str: 'win' if the user has won, 'draw' if the user and the computer got the same item,
                    'loss' if the user has lost.

        play(self): Runs a single game of Rock-Paper-Scissors.
            Asks the user for their item choice and the computer selects its item randomly.
            Compares the user's item with the computer's item to determine the game result.
            Prints the output of the game, indicating whether the user won, lost, or drew.
            Returns the result of the game as a string: 'win', 'draw', or 'loss'.
    """

    def get_user_item(self):
        while True:
            user_input = input("Select (r)ock, (p)aper, or (s)cissors: ")
            if user_input in {'r', 'p', 's'}:
                user_item = {"r": "rock", "p": "paper",
                             "s": "scissors"}[user_input]
                return user_item
            else:
                print(
                    "Invalid move. Please choose either (r)ock, (p)aper, or (s)cissors.")

    def get_computer_item(self):
        computer_item = random.choice(['r', 'p', 's'])
        return {"r": "rock", "p": "paper", "s": "scissors"}[computer_item]

    def get_game_result(self, user_item, computer_item):
        if computer_item == user_item:
            return 'draw'
        elif (user_item == 'rock' and computer_item == 'scissors') or \
             (user_item == 'paper' and computer_item == 'rock') or \
             (user_item == 'scissors' and computer_item == 'paper'):
            return 'win'
        else:
            return 'loss'

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(
            f"You selected {user_item}. The computer selected {computer_item}. You {result}!")
        return result
