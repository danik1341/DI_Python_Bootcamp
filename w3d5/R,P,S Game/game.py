import random


class Game:
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
