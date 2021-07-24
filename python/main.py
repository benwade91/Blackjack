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

def play_prompt():
    """Initiates new game"""

    play = input('Ready to play? \ny or n \n')

    del user[:]
    del dealer[:]

    if play == 'y':
        start_game()
    else:
        print('bye!')
    

def random_card():
    card, value = random.choice(list(cards.items()))
    return [card, value]

def start_game():
    for _ in range(2):
        user.append(random_card())
        dealer.append(random_card())

    game_over = False
    
    while not game_over:
        user_hand = get_hand(user)
        user_score = get_score(user)

        dealer_hand = get_hand(dealer)
        hidden_dealer_hand = get_hand(dealer)
        hidden_dealer_hand[0] = 'X'
        dealer_score = get_score(dealer)
        
        print(f'your hand is {user_hand}')
        print(f'the dealer is not showing {dealer_hand}')
        print(f'the dealer is showing {hidden_dealer_hand}')

        if user_score == 21:
            game_over = True
            print('You Win!')
        elif dealer_score == 21:
            game_over = True
            print('Dealer Wins!')
        elif user_score > 21:
            if 'A' in user_hand:
                user_score -= 10
            else:
                game_over = True
                print('Bust! You Lose!')
        elif dealer_score > 21:
            game_over = True
            print('Dealer Bust! You Win!')
        
        game_over = True

        # else:
        #     player_choice = input("Would you like to 'hit' or 'stand'?\n")
        #     while dealer_score < 17:
        #         dealer.append(random_card())
        #         dealer_score = get_score(dealer)
        #     if player_choice == 'hit':
        #         user.append(random_card())
        #     else: 
        #         game_over = True
        #         user_score = get_score(user)
        #         if user_score > dealer_score:
        #             print(f'You have {user_score} and the dealer has {dealer_score}. You Win!')
        #             print(get_hand(dealer))
        #         elif user_score < dealer_score:
        #             print(f'You have {user_score} and the dealer has {dealer_score}. You Lose!')
        #             print(get_hand(dealer))
        #         elif user_score == dealer_score:
        #             print(f'You have {user_score} and the dealer has {dealer_score}. Draw!')
        #             print(get_hand(dealer))
    play_prompt()

        
def get_score(player):
    score = 0
    for i in player:
        score += i[1]
    return score

def get_hand(player):
    hand = []
    for i in user:
           hand.append(i[0])
    return hand

play_prompt()


# STILL NEED
# fix random card generation
# test for more edge cases