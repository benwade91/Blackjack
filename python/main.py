import random

cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
values = {
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

def deal_cards():
    for i in range(2):
        user.append(random.choice(cards))
        dealer.append(random.choice(cards))
    
    print_score(user)
    print_score(dealer)

def print_score(player):
    score = 0
    for i in range(len(player)):
        score += values[player[i]]
    print(score)


start()
