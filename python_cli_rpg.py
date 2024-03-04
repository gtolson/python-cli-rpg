#!/usr/bin/python

#101
# X Ask the player for their name. X
# X Display a message that greets them and introduces them to the game world. X
# X Present them with a choice between two doors. X
# X If they choose the left door, they'll see an empty room. X
# X If they choose the right door, then they encounter a dragon. X
# X In both cases, they have the option to return to the previous room or interact further.
# X When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# X When encountering the dragon, they have the choice to fight it.
# X If they have the sword from the other room, then they will be able to defeat it and win the game.
# X If they don't have the sword, then they will be eaten by the dragon and lose the game.

#201
#Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
# X Create an inventory for your player, where they can add and remove items. X
#Players should be able to collect items they find in rooms and add them to their inventory.
#If they lose a fight against the dragon, then they should lose their inventory items.
#Add more rooms to your game and allow your player to explore.
#Some rooms can be empty, others can contain items, and yet others can contain an opponent.
#Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
# X Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.


import os
import time
import random

os.system('clear')
username = input("Please enter your name: ")
welcome_message = f"Welcome {username} to the world of Gary's mind, lets start to play!"
dragon_name = "AssHat"
sword_in_hand = "n"
empty_room_stay = None
dragon_fight_q = None
item_inventory = []
dragon_health = 20
player_health = 20

victory = f"""
                                  ___________
                             .---'::'        `---.
                            (::::::'              )
                            |`-----._______.-----'|
                            |              :::::::|
                           .|               ::::::!-.
                           \|               :::::/|/
                            |               ::::::|
                            |  {username} the ::::|
                            |    {dragon_name}::::|
                            |     Slayer    ::::::|
                            |              .::::::|
                            |              :::::::|
                             \            :::::::/
                              `.        .:::::::'
                                `-._  .::::::-'
                                    |     |
                                    |  :::|
                                    |   ::|
                                   /     ::\  
                              __.-'      :::`-.__
                             (_           ::::::_)
                               `:::---------:::'
"""
                             
    
def validate_yn():
    print("Please try again and make sure to choose either \"Y\" or \"N\"" )
    input("Press any \"Enter\" to continue: ")
    
def press_to_continue():
    input("Press any \"Enter\" to continue: ")


os.system('clear')
print(f"{welcome_message}", end='\n\n')

while username != None:
    os.system('clear')
    print(f"{username}, You are in the front room of a large castle, there are 2 doors in front of you. " 
          "One to the right and one to the left. ")
    print("Choose the door on the right by typing \"R\" or choose the door on the left by typing \"L\" "
          "or type \"E\" to exit the game", end='\n\n')
    frontroom_door = input("Make your choice (L/R/E): ")
    frontroom_door = frontroom_door.lower()
    if (frontroom_door != "l") and (frontroom_door != "r") and (frontroom_door != "e"):
        os.system('clear')
        print("Please try again and make sure to choose either \"L\" or \"R\" or \"E\"")
        press_to_continue()
        continue
    
    if frontroom_door == 'e':
        print("Thank you for playing come back if you dare!")
        exit()
        
    while frontroom_door == "l":
        os.system('clear')
        print("You have come to what appears to be an empty room.", end='\n\n')
        empty_room_stay = input("Would you like to stay and look around in this empty room? (Y/N)")
        empty_room_stay = empty_room_stay.lower()
        if empty_room_stay != "y" and empty_room_stay != "n":
            os.system('clear')
            validate_yn()
            continue
        break
    
    if empty_room_stay == "n":
        print("You have chosen not to stay, guiding you back to the front room: ")
        press_to_continue()
        empty_room_stay = None
        continue
    
    if empty_room_stay == "y":
        os.system('clear')
        print("Good for you in your looking around you found a sword, you really need a weapon.", end='\n\n')
        while empty_room_stay == "y":
            sword_in_hand = input("Would you like to pick up the sword (Y/N): ")
            sword_in_hand = sword_in_hand.lower()
            if sword_in_hand != "y" and sword_in_hand != "n":
                validate_yn()
                continue
            else:
                if sword_in_hand == "y":
                    item_inventory.append("sword")
                empty_room_stay = None
                break
            
        if "sword" in item_inventory:
            os.system('clear')
            print("Congrats.., you now have a sword! You are armed and ready "
                  "to fight whatever comes your way. ")
            print("You have found eveything here. We will guide you back to the front room. once there try the door on the Right.", end='\n\n')

        if "sword" not in item_inventory:
            os.system('clear')
            print("You chose not to pick up the sword, "
                  "once back in the front room enter any other room at your own parrel. ")
            print("We will guide you back to the front room.", end='\n\n')

        press_to_continue()
        continue
            
    while frontroom_door == "r":
        os.system('clear')
        print(f"In this room you meet the dragon named {dragon_name}, That's his name because he's a jerk.", end='\n\n')
        if "sword" in item_inventory:
            print(f"You have a sword and if you know how to use it, there are great treasures "
                  f"if you can get past {dragon_name} the dragon..") 
            print("With great risk comes great reward!!!", end='\n\n')
        else:
            print(f"You do not have any weapons to fight {dragon_name}," 
                  f"choose to fight only if you want to be lunch for {dragon_name}!", end='\n\n')
            
        print(f"Would you like to stay and fight {dragon_name}?", end='\n\n') 
        dragon_fight_q = input("Y to Fight, or N to run away: (Y/N)")
        dragon_fight_q  = dragon_fight_q.lower()
        if dragon_fight_q  != "y" and dragon_fight_q  != "n":
            os.system('clear')
            validate_yn()
            continue
        break
            
    if dragon_fight_q == "n":
        os.system('clear')
        if "sword" in item_inventory:
            print(f"You have a sword, yet you have chosen not to face {dragon_name}... how dissapointing! "
                  "guiding you back to the front room. ")
            press_to_continue()
        else:
            print(f"Smart move not fighting {dragon_name} with out a weapon... "
                  "guiding you back to the front room")
            press_to_continue()
        continue  
    
    if dragon_fight_q == "y":
        os.system('clear')
        print(f"Ok its on... best of luck! {dragon_name} is really big and does not like visitors! "
              "Fight brave human...")
        #time.sleep(10)
        if "sword" not in item_inventory:
            print("Because you dont have a weapon you will need to roll a 19 or better to score a hit.")
            while player_health > 0 and dragon_health > 0:
                input("Press any key to roll the dice: ")
                roll20 = random.randint(1, 20)
                print(f"battle_roll = {roll20}")
                roll12 = random.randint(1, 12)
                print(f"damage_roll = {roll12}")
                if roll20 >= 19:
                    dragon_health -= roll12
                    print(f"You scored a hit: {dragon_name} has {dragon_health} points remaning")
                elif roll20 < 19:
                    player_health -= roll12
                    print(f"Ouch! {dragon_name} got you.. you have {player_health} points remaning") 
            if player_health <= 0:
                os.system('clear') 
                print(f"{dragon_name} burned you alive, then ate you, waited an hour then pooped you out "
                    "so he could use you as compost for his collection of rare flowers. "
                    "(We told you he was a jerk...) ")
                exit()
            if dragon_health <=0:
                os.system('clear') 
                print(victory)
                print(f"No idea how you did it without a weapon but You killed {dragon_name}!!!! "
                    f"To the victor come the spoils!!! All of {dragon_name}'s treasure is yours")
                exit()
        elif "sword" in item_inventory:
            print("You will need to roll better than a 5 to score a hit!!!")
            while player_health > 0 and dragon_health > 0:
                input("Press any key to roll the dice: ")
                roll20 = random.randint(1, 20)
                print(f"battle_roll = {roll20}")
                roll12 = random.randint(1, 12)
                print(f"damage_roll = {roll12}")
                if roll20 >= 5:
                    dragon_health -= roll12
                    print(f"You scored a hit: {dragon_name} has {dragon_health} points remaning")
                elif roll20 < 5:
                    player_health -= roll12
                    print(f"Ouch! {dragon_name} got you.. you have {player_health} points remaning") 
                if player_health <= 0:
                    os.system('clear')
                    print(f"{dragon_name} burned you alive, then ate you, waited an hour then pooped you out "
                        "so he could use you as compost for his collection of rare flowers. "
                        "(We told you he was a jerk...) ")
                    exit()
                if dragon_health <=0:
                    os.system('clear')            
                    print(victory)
                    print(f"Wow you sure are good with that sword! You killed {dragon_name}!!!! "
                          f"To the victor come the spoils!!! All of {dragon_name}'s treasure is yours")
                    exit()
    
        
        