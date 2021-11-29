def score(score_list):
    score = 0
    length = len(score_list)
    for i in range(0, length):
        score += score_list[i]
    return score


def computer_game(card_list):
    while score(card_list) < 17:
        chosen_one = random.randint(0, 12)
        if score(card_list) + chosen_one > 22 and chosen_one == 11:
            chosen_one = 1
        card_list.append(chosen_one)
    return card_list


from replit import clear
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
end_game = False

while not end_game:
    print(logo)
    print("\n\n")
    choice1 = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':  ")
    if choice1 == 'y':
        your_card = []
        computer_card = []
        for i in range(0, 2):
            chosen_one = random.randint(0, 12)
            chosen_two = random.randint(0, 12)
            if score(your_card) + chosen_one > 22 and chosen_one == 11:
                chosen_one = 1
            if score(computer_card) + chosen_two > 22 and chosen_two == 11:
                chosen_two = 1
            your_card.append(cards[chosen_one])
            computer_card.append(cards[chosen_two])
        your_score = score(your_card)
        computer_score = score(computer_card)
        print(f"Your cards : {your_card}, current score = {your_score}")
        print(f"Computer's first card: {computer_card[0]}\n")

        choice2 = input("Type 'y' to get another card, type 'n' to pass:  ")
        while score(your_card) < 22 and choice2 == 'y':
            clear()
            chosen_one = random.randint(0, 12)
            if chosen_one == 11 and score(your_card) + chosen_one > 23:
                chosen_one = 1
            your_card.append(cards[chosen_one])
            print(f"Your cards : {your_card}, current score = {score(your_card)}")
            print(f"Computer's first card : {computer_card[0]}\n\n")
            if score(your_card) < 22:
                choice2 = input("Type 'y' to get another card, type 'n' to pass: ")

        computer_flist = computer_game(computer_card)
        print(f"Your final hand : {your_card}, final score ={score(your_card)}")
        print(f"Computer's final hand :{computer_flist}, final score={score(computer_flist)} ")

        if score(computer_card) == 21:
            print("You lose, computer win the blaxkjack")

        elif score(your_card) == 21:
            print("You win the blackjack")

        elif score(your_card) > 21:
            print("You went over. You lose")

        elif score(computer_flist) > 21:
            print("Your opponent went over. You win")

        elif choice2 == 'n':
            if score(your_card) > score(computer_flist):
                print("You win")
            elif score(your_card) < score(computer_flist):
                print("You lose")
            elif score(your_card) == score(computer_flist):
                print("Its a draw")


    elif choice1 == 'n':
        print("Thank you")
        end_game = True

