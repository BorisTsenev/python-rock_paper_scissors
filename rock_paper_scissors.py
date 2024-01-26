import random

list_of_chance = [2, 4, 6, 1, 3, 5, 7, 9, 11, 13]
list_of_choices = ["rock", "paper", "scissors"]
dict_of_win = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

print("Welcome to the game of Rock, Paper, Scissors \n"
      "You are playing Vs unbeatable AI. \n"
      "So would you try your luck with a bunch of games? \n"
      "You can choose between rock, paper and scissors. \n"
      "When you want to stop the game just type STOP. \n"
      "The first choice you need to take is the hardness of the game. \n"
      "So you can choose between hard and normal!! \n"
      "Enjoy :)")

while True:
    difficulty = input("Choose your game difficulty: ")
    if difficulty == "STOP":
        break
    player_choice = input("Choose your character: ")
    if player_choice == "STOP":
        break
    if difficulty == "hard":
        print("Excellent choice!")
        number_chance = random.choice(list_of_chance)
        if number_chance % 2 == 1:
            ai_choice = dict_of_win[player_choice]
        else:
            ai_choice = random.choice(list_of_choices)
    elif difficulty == "normal":
        print("Good choice.")
        ai_choice = random.choice(list_of_choices)

    if player_choice == dict_of_win[ai_choice]:
        print(f"You beated the AI {ai_choice} with {player_choice}")
    elif player_choice == ai_choice:
        print(f"You are draw with {player_choice}")
    else:
        print(f"The AI beat your {player_choice} with {ai_choice}")

print("Thank you for playing the Rock, Paper, Scissors game. :)")

