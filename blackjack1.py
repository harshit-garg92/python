import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4  

def draw_card():
    if len(deck) == 0:
        print("The deck is empty!")
        exit()
    
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_score(cards):
    return sum(cards)

def adjust_for_ace(cards):
    ace_count = cards.count(11)
    score = calculate_score(cards)

    while score > 21 and ace_count > 0:
        score -= 10  
        ace_count -= 1

    return score

def check_blackjack(cards):
    return any(card == 11 for card in cards) and any(card == 10 for card in cards)

def user_turn(user_cards):
    while True:
        user_score = calculate_score(user_cards)

        if user_score > 21:
            if 11 not in user_cards:
                print(f"User's cards: {user_cards} | Score: {user_score}")
                print(f"Computer's cards: {computer_cards} | Score: {computer_score}")
                print("User went over 21 and have no ace ! You lose!")
                exit()
            user_score = adjust_for_ace(user_cards)  
            if user_score > 21:
                print(f"User's cards: {user_cards} | Score: {user_score}")
                print(f"Computer's cards: {computer_cards} | Score: {computer_score}")
                print("User went over 21! You lose!")
                exit()

        print(f"User's cards: {user_cards} | Score: {user_score}")
        action = input("Do you want to draw another card? (y/n): ").strip().lower()

        if action == 'y':
            user_cards.append(draw_card())
            if check_blackjack(user_cards):
                print(f"User's cards: {user_cards} | Score: 21")
                print(f"Computer's cards: {computer_cards} | Score: {computer_score}")
                print("User has Blackjack! You win!")
                exit()
        else:
            return user_score

def computer_turn(computer_cards):
    while calculate_score(computer_cards) < 17:
        computer_cards.append(draw_card())
        computer_score = calculate_score(computer_cards)
        
        if computer_score > 21:
            computer_score = adjust_for_ace(computer_cards)  

    computer_score = calculate_score(computer_cards)  
    return computer_score

user_cards = [draw_card(), draw_card()]
computer_cards = [draw_card(), draw_card()]

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"User's cards: {user_cards} | Score: {user_score}")
print(f"Computer's cards: [{computer_cards[0]}, ?]")

if check_blackjack(user_cards) and check_blackjack(computer_cards):
    print("Both user and computer have Blackjack! It's a draw!")
    exit()
elif check_blackjack(user_cards):
    print("User has Blackjack! You win!")
    exit()
elif check_blackjack(computer_cards):
    print("Computer has Blackjack! You lose!")
    exit()
else:
    user_score = user_turn(user_cards)
    if user_score <= 21:
        computer_score = computer_turn(computer_cards)

    print(f"User's final cards: {user_cards} | Final score: {user_score}")
    print(f"Computer's final cards: {computer_cards} | Final score: {computer_score}")

    if computer_score > 21:
        print("User wins!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")
