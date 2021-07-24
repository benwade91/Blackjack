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

# USER/DEALER HANDS
user = []
dealer = []

# PROMPTS USER TO BEGIN
def play_prompt():
    """Initiates new game"""

    play = input('Ready to play? \ny or n \n')

    del user[:]
    del dealer[:]

    if play == 'y':
        start_game()
    else:
        print('bye!')
    
# RANDOMLY SELECTS CARD FROM DICTIONARY
def random_card():
    card, value = random.choice(list(cards.items()))
    return [card, value]

# GAME LOGIC
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
        print(f'the dealer is showing {hidden_dealer_hand}')

        # LOOK FOR BLACKJACK
        if user_score == 21:
            game_over = True
            print('You Win! BlackJack!')
            print(user_hand)
        elif dealer_score == 21:
            game_over = True
            print('Dealer BlackJack!')
            print(dealer_hand)
        elif user_score > 21:
            game_over = True
            print('Bust! You Lose!')
            print(user_hand)

        else:        
            player_choice = input("Would you like to 'hit' or 'stand'?\n")
            
            if player_choice == 'hit':
                user.append(random_card())
            else: 
                game_over = True

                # DEALER PLAYS
                while dealer_score < 17:
                    dealer.append(random_card())
                    dealer_score = get_score(dealer)
                    dealer_hand = get_hand(dealer)
                
                # ASSESS SCORES
                if dealer_score > 21:
                    print('Dealer Bust! You Win!')
                    print(dealer_hand)
                elif dealer_score == 21:
                    print('Dealer BlackJack!')
                    print(dealer_hand)
                elif user_score > dealer_score:
                    print(f'You have {user_score} and the dealer has {dealer_score}. You Win!')
                    print(get_hand(dealer))
                elif user_score < dealer_score:
                    print(f'You have {user_score} and the dealer has {dealer_score}. You Lose!')
                    print(get_hand(dealer))
                elif user_score == dealer_score:
                    print(f'You have {user_score} and the dealer has {dealer_score}. Draw!')
                    print(get_hand(dealer))
    play_prompt()

# RETURNS SCORE OF PROVIDED USER
def get_score(player):
    score = 0
    for i in player:
        score += i[1]
        if score > 21:
            if i[0] == 'A':
                score -= 10
    
    return score

# RETURNS HAND OF PROVIDED USER
def get_hand(player):
    hand = []
    for i in player:
           hand.append(i[0])
    return hand

play_prompt()
