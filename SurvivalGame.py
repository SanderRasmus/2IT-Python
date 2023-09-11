import random as rd
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    player_health = 35
    player_damage = rd.randint(4,8)


    clear_screen()
    print("Great to have you on the team Traveler. I will be quick because you have a big journey to set foot in.")
    print("To give you the context of the task, the past few weeks many unknown hostile creatures have appeared around the area and attacked innocent civilians")
    print("We require a hero to save us all, in return you will be payed handsomly in both Gold and equipment. We are unsure where these creatures are located")
    print("But I am sure if you explore around the nearby area you will find some quite quickly. I wish you good luck Traveler on your journey!")
    print("\n[1] Start to Explore the nearby Area\n[2] Check Inventory\n[3] Quit the game\n")

    choice = int(input("Please choose a course of action: "))

    while choice != 1 and choice != 2 and choice != 3:
        clear_screen()
        print("Invalid Action, Please try again!")
        print("\n[1] Start to Explore the nearby Area\n[2] Check Inventory\n[3] Quit the game\n")
        choice = int(input("Please choose a course of action: "))
    
    while choice == 2:
        clear_screen()
        print("This feature is not yet availble, please try again later")
        print("\n[1] Start to Explore the nearby Area\n[2] Check Inventory\n[3] Quit the game\n")
        choice = int(input("Please choose a course of action: "))


    if choice == 1:
        clear_screen()
        print("Your journey begins and you have exited the village. Now time to start exploring")
        time.sleep(3)
        
        beast, beast_hp, beast_damage = small_encounter()
        print(f"\nYou have encountered a wild hostile {beast}! The creature has {beast_hp} HP and deals {beast_damage} damage!")
        print("You must defend yourself! Kill the creature before it kills you!")

    elif choice == 3:
        exit()


def small_encounter():
    beast_list = ["Boar", "Bat", "Hedgehog", "Minotaur"]
    beast = rd.choice(beast_list)

    if beast == "Boar":
        beast_hp = rd.randint(8, 12)
        beast_damage = rd.randint(4,8)
    elif beast == "Bat":
        beast_hp = rd.randint(5, 8)
        beast_damage = rd.randint(2,5)
    elif beast == "Hedgehog":
        beast_hp = rd.randint(10, 15)
        beast_damage = rd.randint(5,11)
    elif beast == "Minotaur":
        beast_hp = rd.randint(10, 16)
        beast_damage = rd.randint(8,12)
    
    return beast, beast_hp, beast_damage

    
def traveler():
    clear_screen()
    print("\nWelcome Traveler to the Streets of Trondheim, I have a challenge for you if you are up for it!")
    print("If you complete this challenge great rewards may follow. Do you got what it takes?")
    print("\n[1] Start Journey \n[2] No thank you!")
    play = int(input("\nPlease make your choice: "))

    while play != 1 and play != 2:
        clear_screen()
        print("Invalid Action, Please try again")
        play = int(input("\nPlease make your choice: "))

    if play == 1:
        main()
    else:
        print("Only true warriors can face such challenge, I had a feeling you werent one of them")


traveler()

