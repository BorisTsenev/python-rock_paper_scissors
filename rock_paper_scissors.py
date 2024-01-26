import random

list_of_chance = [2, 4, 6, 1, 3, 5, 7, 9, 11, 13]
list_of_choices = ["rock", "paper", "scissors"]

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
    if difficulty == "hard":
        print("Excellent choice!")
        number_chance = random.choice(list_of_chance)
        if number_chance % 2 == 1:
            player_choice = input("Choose your character: ")
    elif difficulty == "normal":
        print("Good choice.")
        ai_choice = random.choice(list_of_choices)
        player_choice = input("Choose your character: ")


