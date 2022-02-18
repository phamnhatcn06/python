import random
GAME_LIMIT = 21


def roll_dice():
    user_roll = random.randint(1, 3)
    computer_roll = random.randint(1, 3)
    return user_roll, computer_roll


def get_response():
    response = input("Do you want to roll? (y/n): ")
    return response


def main():
    user_points = 0
    computer_points = 0
    print("Welcome to the game of 21!")
    print()
    isEnd = False  # added a is game end

    while not isEnd:
        answer = get_response()
        if(answer == "y"):  # checkes whther still roll dice
            points, comp_points = roll_dice()
            user_points += points
            computer_points += comp_points
            print("User Points:", user_points)
            print("Computer Points:", computer_points)
            if user_points == GAME_LIMIT:
                print("User's Points:", user_points)
                print("Computer's Points:", computer_points)
                if computer_points == GAME_LIMIT:
                    print("Tie Game!")
                else:
                    print("User Wins!")
                isEnd = True
            if user_points > GAME_LIMIT:
                print("User's Points:", user_points)
                print("Computer's Points:", computer_points)
                if computer_points < GAME_LIMIT:
                    print("Computer Wins!")
                elif computer_points == GAME_LIMIT:
                    print("Computer Wins!")
                else:
                    print("Tie Game!")
                isEnd = True

        if (answer == "n"):
            isEnd = True


if __name__ == "__main__":
    main()
