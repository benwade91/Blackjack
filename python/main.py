import random

cards = {
    'A':11,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10
}
user = []
dealer = []
def start():
    """Initiates new game"""

    play = input('Ready to play? \ny or n \n')

    if play == 'y':
        deal_cards()
    else:
        print('bye!')

def random_card():
    card, value = random.choice(list(cards.items()))
    return [card, value]

def deal_cards():
    for i in range(2):
        user.append(random_card())
        dealer.append(random_card())
    print_score(user)
    print_score(dealer)

def print_score(player):
    score = 0
    for i in player:
        score += i[1]
    print(score)


start()
