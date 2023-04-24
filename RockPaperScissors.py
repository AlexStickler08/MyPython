import random

print("Welcome to rock, paper, scissors!")

while True:
    
    user_input_start = input("Please choose either [1]rock, [2]paper or [3]scissors: ")

    if user_input_start == "1":
        user_input = "rock"
    
    elif user_input_start == "2":
        user_input = "paper"
    
    elif user_input_start == "3":
        user_input = "scissors"

    print("User: " + user_input)

    computer_input_list = ["rock", "paper", "scissors"]

    computer_choice = random.choice(computer_input_list)
  
    print("Computer: " + computer_choice)

    if user_input == computer_choice:
      print("Tie!")
      
    elif computer_choice == "paper":
        if user_input == "rock":
            print("You lose! " + computer_choice + " beats " + user_input + "!")
        elif user_input == "scissors":
            print("You win! " + user_input + " beats " + computer_choice + "!")
      
    elif computer_choice == "rock":
        if user_input == "scissors":
            print("You lose! " + computer_choice + " beats " + user_input + "!")  
        elif user_input == "paper":
            print("You win! " + user_input + " beats " + computer_choice + "!")
          
    else:
        if user_input == "rock":
            print("You win! " + user_input + " beats " + computer_choice + "!")          
        elif user_input == "paper":
            print("You lose! " + computer_choice + " beats " + user_input + "!")
    
          
    cont = input("Would you like to continue [y/n]: ")

    if cont != "y":
        break