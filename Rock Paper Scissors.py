from math import e
import random

def y():
    try:
        gamer_option = input("Pick 'r' for Rock, 'p' for Paper or 's' for Scissor: ")
        possible_pick = ["r", "p", "s"]
        computer_pick = (random.choice(possible_pick))
        
        if gamer_option == computer_pick:
            print ("You chose " + gamer_option + "\nComputer chose " + computer_pick)
            print ("It's a tie!")
        elif gamer_option == "r":
            if computer_pick == "s":
                print ("You chose " + gamer_option + "\nComputer chose " + computer_pick)
                print("Rock smashes Scissor. \nYou win!")
            else:
                print ("You chose " + gamer_option + "\nComputer chose " + computer_pick)
                print("Paper covers Rock. \nYou loose!")
        elif gamer_option == "s":
            if computer_pick == "r":
                print ("You chose " + gamer_option + "\nComputer chose " + computer_pick)
                print("Rock smashes Scissor. \nYou loose!")
            else:
                print ("You chose " + gamer_option + "\nComputer chose " + computer_pick)
                print("Scissor cuts Paper. \nYou win!")
        elif gamer_option == "p":
            if computer_pick == "r":
                print ("You chose " + gamer_option + "\nComputer chose " + computer_pick)
                print("Paper cover Rock. \nYou win!")
            else:
                print ("You chose " + gamer_option + "\nComputer chose " + computer_pick)
                print("Scissor cuts Paper. \nYou loose!")
    except ValueError:
        print('Please try again')
        y()

def main():
    while True:
        answer = input("Run program? (y/n): ")
        if answer.lower() != 'y':
            break
        else:
            y()
main()