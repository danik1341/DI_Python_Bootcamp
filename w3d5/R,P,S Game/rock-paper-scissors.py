from game import Game


def get_user_menu_choice():
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
    print("Game Results:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thank you for playing!")


def main():
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
