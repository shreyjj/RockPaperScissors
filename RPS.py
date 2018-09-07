import random
tracers = {"scissors":1, "paper":2, "rock":3, "lizard":4, "spock":5}
Number = 0
choice_names = ["scissors", "paper", "rock", "lizard", "spock"]
choice_numbers = [1,2,3,4,5]
odd = ("1,3,5")
even = ("2,4,6")

user_choice=input("Pick either rock, paper, scissors lizard or spock")

if user_choice not in choice_names:
 Print("not a valid choice")
 user_choice=input("Pick either rock, paper, scissors lizard or spock")
else:
    computer_choice =(random.choice(choice_names))
print("The computer picked", computer_choice)

user_value = tracers[user_choice]
computer_value = tracers[computer_choice]


number = user_value - computer_value

if number % 2 == 0:
    if user_value > computer_value: 
        print("Congratualtions, you won")
        
    else:
        print("You lose")
            
            
elif number % 2 == 1:
    if user_value < computer_value: 
        print("Congratualtions, you won")
        
    else:
        print("You lose")
        
else:
    print("You drew")