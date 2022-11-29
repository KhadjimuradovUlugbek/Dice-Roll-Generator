import random

#Enter the minimum and maximum limits of the dice rolls below

min_val = 1

max_val = 10

#The variable that stores the user's decision

roll_again = "yes"

#The dice rool loop if the user wants to continue

while roll_again == "yes" or roll_again == "y":
    
    print("Dice rolling...")
    print("The values are: ")
    
    #Printing the randomly generated variable of the first dice
    
    print(random.randint(min_val, max_val))
    
    #Printing the randomly generated variable of the second dice 
    
    print(random.randint(min_val, max_val))
    
    #Here the user enters yes or y to continue and other input ends the programm
    
    roll_again = input("Please write 'yes' or 'y' to roll the dice again: ")