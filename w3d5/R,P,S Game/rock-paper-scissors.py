from game import Game


def get_user_menu_choice():
    """
    Displays a simple menu to the user and gets their choice.

    Returns:
        str: 'play' if the user wants to start a new game,
             'scores' if the user wants to view game scores,
             'q' if the user wants to quit the program.
    """

    while True:
        print("Menu:")
        print("1. Play a new game")
        print("2. Show scores")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            return 'play'
        elif choice == '2':
            return 'scores'
        elif choice == '3':
            return 'q'
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def print_results(results):
    """
    Prints the results of the games played.

    Parameters:
        results (dict): A dictionary containing the results of the games played.
            It should have the keys 'win', 'loss', and 'draw', representing
            the number of wins, losses, and draws respectively.
    Returns:
        None
    """
    print("Game Results:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thank you for playing!")


def main():
    """
    The main function of the Rock-Paper-Scissors game.

    Runs a game loop that displays the main menu and allows the user to:
        - Start a new game
        - View game scores
        - Quit the program

    During the game loop, it keeps track of the results of each game played.

    Returns:
        None
    """
    results = {'win': 0, 'loss': 0, 'draw': 0}

    while True:
        choice = get_user_menu_choice()

        if choice == 'play':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == 'scores':
            print_results(results)
        elif choice == 'q':
            print_results(results)
            break
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()
