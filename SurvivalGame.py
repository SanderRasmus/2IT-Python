import random as rd
import os
import time
from colorama import Fore

def clear_screen():
    # Funksjon for å fjerne alt av tekst i terminalen for å gjøre spillet mer oversiktlig. Fungerer for både Windows og andre OSer
    os.system('cls' if os.name == 'nt' else 'clear')

#Spiller Variabler
player_health = 35
player_damage = rd.randint(4,8)


def battle(beast, beast_hp, beast_damage):
    # Funksjon som tar av seg kamper mellom spiller og creatures
    global player_health

    print("\n[1] Hit the target! (Damage 4-8)\n[2] Use an Item!\n[3] Attempt to flee\n")
    
    #Repeterer funksjonen til enten spiller eller NPC er død eller unnsluppet.
    while beast_hp > 0 and player_health > 0:
        battle_choice = int(input("Please choose a course of action: "))

        while battle_choice > 3 or battle_choice <= 0:
            clear_screen()
            print("Invalid Action, Please try again!")
            print("\n[1] Hit the target! (Damage 4-8)\n[2] Use an Item!\n[3] Attempt to flee\n")
            battle_choice = int(input("Please choose a course of action: "))
    
        if battle_choice == 1:
            beast_hp = beast_hp - player_damage
            print(f"You punched the {beast} and you dealt {player_damage} damage!")
            print(f"The {beast} has {beast_hp} HP Left.\n")
            time.sleep(2)
            if beast_hp > 0 and player_health > 0:
                print(f"The {beast} attacks you, and deals {beast_damage} damage to you!")
                player_health = player_health - beast_damage
                print(f"You have now {player_health} hp remaining!\n")
                time.sleep(1.3)
                print("\n[1] Hit the target! (Damage 4-8)\n[2] Use an Item!\n[3] Attempt to flee\n")

        elif battle_choice == 2:
            print("Wait")
        elif battle_choice == 3:
            flee = rd.randint(1,100)

            if flee >= 10:
                print(f"You have successfully fled the {beast}")
            else:
                print(f"You have failed to flee the {beast}, which made you vulnerable.")
                time.sleep(2)
                print(f"The {beast} attacks you, and deals {beast_damage} damage to you!")
                player_health = player_health - beast_damage
                print(f"You have now {player_health} hp remaining!")
    
    if beast_hp <= 0:
        print(f"You have successfully defeated the {beast}!")
    elif player_health <= 0:
        print("You were defeated in battle and have died.")
        time.sleep(2)
        clear_screen()
        exit()
        
def main():
    # Hovedfunksjonen i spillet. Denne Seksjonen som tar av seg teksting, veivalg etc. og kaller på andre funksjoner når det trengs
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
        print("\n[1] Exit the village and start to explore!\n[2] Check Inventory\n[3] Quit the game\n")
        choice = int(input("Please choose a course of action: "))
    while choice == 2:
        clear_screen()
        print("This feature is not yet availble, please try again later")
        print("\n[1] Start to Explore the nearby Area\n[2] Check Inventory\n[3] Quit the game\n")
        choice = int(input("Please choose a course of action: "))
    if choice == 1:
        clear_screen()
        print("Your journey begins and you have exited the village. Now time to start exploring\n")
        time.sleep(3)

        print("Some time have passed and you have reached a crossroads. To the right you see a giant Mountain with caves, however to your left there is an huge dense and dark Forest awaiting you.")
        print("Please pick which path you want to explore further!\n[1] Left\n[2] Right\n")
        path = int(input("Please choose a course of action: "))

        while path > 2 or path <= 0:
            clear_screen()
            print("Invalid Action, Please try again!")
            print("Pick which path you want to travel on!\n[1] Left\n[2] Right\n")
            path = int(input("Please choose a course of action: "))
        
        if path == 1:
            forest()
        else:
            cave()
    elif choice == 3:
        exit()

def forest():
    # Vei valg Venstre - Mørk og tett skog | Fortsetter på historien og kaller på small-encounters for kamper mot npcer.
    clear_screen()
    print("You have choosen to enter the dense and dark forest. ")
    time.sleep(3)
    print("After some time passes you have walked deep into the forest and you can suddenly hear something thats slowly approaching you.")
    time.sleep(4)

    beast, beast_hp, beast_damage = small_encounter()
    print(f"\nYou have encountered a wild hostile {Fore.RED}{beast}{Fore.RESET}! The creature has {Fore.RED}{beast_hp}{Fore.RESET} HP and deals {Fore.RED}{beast_damage}{Fore.RESET} damage!")
    print("You must defend yourself! Kill the creature before it kills you!")
    battle(beast, beast_hp, beast_damage)

def small_encounter():
    #Mindre Encounters listen. Tilfeldig genererer en fiende med ulike stats for hver spawn. Står for mindre encounters og vil bli brukt tidlig i spillet.
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

def cave():
    # Hule delen av spillet som vil kalle på encounters og dialog.
    clear_screen()
    print("")

def traveler():
    # Starten av spillet hvor spilleren (Traveller) får valget av å starte spillet eller ikke.
    clear_screen()
    print(f"\nWelcome {Fore.CYAN}Traveler {Fore.RESET} to the Streets of Trondheim, I have a challenge for you if you are up for it!")
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

