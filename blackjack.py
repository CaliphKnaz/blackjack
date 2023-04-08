import random
import os

"""Set up game state"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer = []
user = []
score_counter = {
    "Dealer": 0,
    "User": 0
}


def clear_screen():
    """Clears the screen based on the OS."""
    os_name = os.name.lower()
    if os_name == 'posix':
        # For Linux and macOS
        os.system('clear')
    elif os_name == 'nt':
        # For Windows
        os.system('cls')


def randomCard():
    """Generates random card from array"""
    randomCard = random.choice(cards)
    return randomCard


def startingCards():
    """Gives cards to user and dealer"""
    for n in range(1, 3):  # two cards for user
        user.append(randomCard())
    for n in range(1, 2):  # one card for dealer
        dealer.append(randomCard())

    # display starting cards to the user
    user_total = sumUserCards()
    dealer_total = int(sumDealerCards())
    print(
        f"Dealers cards: {dealer} Total: {dealer_total}, User's cards: {user} Total: {user_total}")


def checkBlackJack():
    """Check if user recieved blackjack in starting hand"""
    user_total = sumUserCards()
    dealer_total = int(sumDealerCards())

    # restart game if user has starting blackjack
    if str(checkWinner(dealer_total, user_total)) == "User Blackjack":
        return "Restart"


def sumDealerCards():
    """Sum dealer cards"""
    dealer_total = 0
    for card in range(len(dealer)):
        dealer_total += dealer[card]
    return dealer_total


def sumUserCards():
    """Sum user cards"""
    user_total = 0
    for card in range(len(user)):
        user_total += user[card]
    return user_total


def checkWinner(dealer_total, user_total):
    """ Compares the sum of user cards to dealer cards and return result"""

    # sets game state, continues if dealer has not won
    win = False
    if dealer_total == 21:
        # checks for dealer blackjack
        return "Dealer Blackjack"
    elif dealer_total > 21:
        # checks for dealer bust
        win = False
        return "Dealer Bust"

    if user_total == 21:
        if win == False:
            # checks user blackjack
            return "User Blackjack"
    elif user_total > 21:
        # check user has bust
        return "User Bust"

    if user_total == dealer_total:  # check whether user and dealer have drawn
        return "Draw"

    if not win:
        # checks who wins based on highest card sum
        if user_total > dealer_total:
            return "Dealer Beat"
        else:
            return "User Beat"


def hitCard():
    """Asks the user to draw cards and checks bust and blackjack cases"""
    user_total = sumUserCards()
    dealer_total = int(sumDealerCards())
    if checkBlackJack() != "Restart":  # checks if user starts with blackjack hand, if so does not proceed
        hit = input("Do you want to hit another card? \n Y or N \n").upper()
        # continues to ask user to draw a card until the specify N
        while hit != "N":

            card = randomCard()
            user.append(card)
            user_total = sumUserCards()
            if user_total > 21 and card == 11:  # checks whether drawn card is an 11 changes it into a 1 if over 21

                user[-1] = 1
                user_total = sumUserCards()

            print(
                f"Dealers cards: {dealer} Total: {dealer_total}, User's cards: {user} Total: {user_total}")

            # checks within the while loop if the user has gone over 21
            if checkWinner(dealer_total, user_total) == "User Bust":
                break

            # checks if the user has got blackjack
            if str(checkWinner(dealer_total, user_total)) == "User Blackjack":

                break

            hit = input(
                "Do you want to hit another card? \n Y or N \n").upper()

    # checks if user has reicevied or blackjack or gone bust, preventing the dealer from drawing more cards
    if str(checkWinner(dealer_total, user_total)) != "User Blackjack":
        # stops the dealer from drawing over 17
        while dealer_total < 17 and checkWinner(dealer_total, user_total) != "User Bust":
            card = randomCard()
            dealer.append(card)
            dealer_total = sumDealerCards()
            if dealer_total > 21 and card == 11:
                dealer[-1] = 1
                dealer_total = sumDealerCards()
        print(
            f"Dealers cards: {dealer} Total: {dealer_total}, User's cards: {user} Total: {user_total}")


def results():
    """Displays the results to the user"""
    user_total = sumUserCards()
    dealer_total = int(sumDealerCards())
    if checkWinner(dealer_total, user_total) == "Dealer Blackjack":
        print(
            f"Dealer got blackjack, you lose. \n Dealer Total: {dealer_total}, User Total: {user_total} ")
        score_counter["Dealer"] += 1

    elif checkWinner(dealer_total, user_total) == "Dealer Bust":
        print(
            f"Dealer has bust. You Win \n Dealer Total: {dealer_total}, User Total: {user_total}")
        score_counter["User"] += 1

    elif checkWinner(dealer_total, user_total) == "User Blackjack":
        print(
            f"You got blackjack. You win \n Dealer Total: {dealer_total}, User Total: {user_total}")
        score_counter["User"] += 1

    elif checkWinner(dealer_total, user_total) == "User Bust":
        print(
            f"You busted. You lose \n Dealer Total: {dealer_total}, User Total: {user_total}")
        score_counter["Dealer"] += 1

    elif checkWinner(dealer_total, user_total) == "Dealer Beat":
        print(
            f"You beat the dealer. You win \n Dealer Total: {dealer_total}, User Total: {user_total} ")
        score_counter["User"] += 1

    elif checkWinner(dealer_total, user_total) == "User Beat":
        print(
            f"The dealer beat you. You lost \n Dealer Total: {dealer_total}, User Total: {user_total}")
        score_counter["Dealer"] += 1

    elif checkWinner(dealer_total, user_total) == "Draw":
        print(
            f"You drew with the dealer \n Dealer Total: {dealer_total}, User Total: {user_total}")

    # display the current score of the game
    for results in score_counter:
        print("The current score is:", results, f"\n {score_counter[results]}")


def main():
    startingCards()
    checkBlackJack()
    hitCard()
    results()


main()

"""Asks to the user to play again and resets game state"""
continue_game = True

while continue_game:
    play_again = input("\n Do you want to play again? \n Y or N").upper()
    if play_again == "Y":
        clear_screen()
        dealer = []
        user = []
        main()

    else:
        continue_game = False
        clear_screen()
        exit()
