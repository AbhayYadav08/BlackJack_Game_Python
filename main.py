import random
from art import logo
def deal_card():
    """
    Returns a random card from the deck
    :return:
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):

    """
    Returns the total of cards of user or computer
    :param cards:
    :return:
    """

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, Opponent has BlackJack"
    elif u_score == 0:
        return "Win with a blackjack"
    elif u_score>21:
        return "You Loose"
    elif c_score>21:
        return "Computer Loose"
    else:
        if u_score>c_score:
            return "User wins"
        else:
            return "Computer Wins"


def play_game():
    print(logo)
    user_cards = []

    computer_cards  = []

    computer_score = -1

    user_score = -1

    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your card: {user_cards}, your score is: {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True

        if not is_game_over:
            choice=input("Do you want to draw another card or not, type yes or no").lower()
            if choice == "yes":
                user_cards.append(deal_card())
            if choice == "no":
                is_game_over=True


    while computer_score !=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand is this {user_cards} and your final score is {user_score}")
    print(f"Computer final hand is this {computer_cards} and Computer final score is {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack, type 'y' or 'n'").lower() == 'y':
    print("\n" *20)
    play_game()
    