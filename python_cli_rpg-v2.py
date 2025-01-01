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
# X Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
# X Create an inventory for your player, where they can add and remove items. X
# X Players should be able to collect items they find in rooms and add them to their inventory.
# X If they lose a fight against the dragon, then they should lose their inventory items.
# X Add more rooms to your game and allow your player to explore.
# X Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# X Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
# X Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.


import os
import time
import random

username = ""
dragon_name = "AssHat"
sword_item = "n"
room3_stay = None
dragon_fight_q = None
item_inventory = []
user_choices_set = set()
dragon_health = 20
player_health = 20
play_again = None
player_strength_sword = 10
player_strength_club = 13
player_strengh_unarmed = 18
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

def get_username():
    user_name = input("Please enter your name: ")
    return user_name

def get_welcome_message(username):
    welcome_message = f"Welcome to the world of Gary's mind, {username}... lets start to play!" 
    return welcome_message
    
def validate_yn():
    print("Please try again and make sure to choose either \"Y\" or \"N\"" )
    input("Press \"Enter\" to continue: ")
    
def press_to_continue():
    input("Press \"Enter\" to continue: ")
    
def try_again():
    os.system('clear')
    print("Please try again and make sure to choose one of the door numbers \"1-4\" or \"E\" to exit")
    press_to_continue()
    
    
def already_been_in_room():
    while True:
        print("You have already been to this room...")
        another_door_q = input(f"Would you like to choose another door? Y or N to continue into this door: ")
        if another_door_q.isalpha():
            another_door_q.lower()
            if another_door_q == "y":
                go_back_to_main = 1
                break
            if another_door_q == "n":
                go_back_to_main = 0
                break
            else:
                os.system('clear')
                print(f"Please enter only Y or N: Please try again\n")
    return go_back_to_main

def room_choice(username):
    os.system('clear')
    if not hasattr(room_choice, "has_run"):
        room_choice.has_run = True
        print(f"{username}, You are in the front room of a large castle, there are 4 doors in front of you.\n" 
          "Each door has a number 1,2,3 or 4. ")
        print(f"\nChoose the door #1 by typing \"1\" door #2 by typing \"2\" etc... "
          "or type \"E\" to exit the game", end='\n\n')
    else:
        print(f"{username}, You are back in the front room of the castle, please pick 1 of the 4 doors. ") 
    frontroom_door = input("Make your choice (1-4 or E to exit): ")
    if frontroom_door.isalpha():
        frontroom_door = frontroom_door.lower()
        if frontroom_door == 'e':
            print("Thank you for playing come back if you dare!")
            exit()
        else:
            try_again()
            #continue
    frontroom_door = int(frontroom_door)
    if frontroom_door not in range(1,5):
        try_again()
        #continue
    else:
        first_pass = 1
    return frontroom_door

def base_game(username,user_choices_set,item_inventory,dragon_health,player_health,play_again):                   
    while username != None:
        frontroom_door = room_choice(username)

        while frontroom_door == 1:
            os.system('clear')
            if 1 in user_choices_set:
                go_back_to_main = already_been_in_room()
                if go_back_to_main == 1:
                    break
            rm1_chest = input("The door opens and you find a chest.. Would you like to open it? (Y/N) ")
            rm1_chest = rm1_chest.lower()
            if rm1_chest != 'y' and rm1_chest != 'n':
                os.system('clear')
                validate_yn()
                continue
            os.system('clear')
            if rm1_chest == 'y':
                if "room1_chest" in user_choices_set and "skel_key" in item_inventory:
                    print(f"The Chest is empty, you have already opened this Chest and added the key to your inventory.\nNothing more to see here.\n\nSending you back to the frontroom")
                    press_to_continue()
                    break
                else:
                    user_choices_set.add("room1_chest")
                    print("In the chest you have found a key that you need, very good! It has been added to your inventory")
                    item_inventory.append("skel_key")
                    print(f"The key is the only worth while thing in this room.\n\nGuiding you back to the frontroom")
            else:
                print(f"You chose not to open the chest to see whats inside.\n\nSending you back to the frontroom.")           
            press_to_continue()
            user_choices_set.add(frontroom_door)
            break

        while frontroom_door == 2:
            os.system('clear')
            if 2 in user_choices_set:
                go_back_to_main = already_been_in_room()   
                if go_back_to_main == 1:
                    break 
            rm2_unlock = input("This door is locked. Do you have a key to open it? (Y/N) ")
            rm2_unlock = rm2_unlock.lower()
            os.system('clear')
            if rm2_unlock != "y" and rm2_unlock != "n":
                os.system('clear')
                validate_yn()
                continue
            if "skel_key" in item_inventory:
                print("You do have the skeleton key and it has worked to open the door...")
                if "club" in item_inventory:
                    print(f"The room is empty, remember you were already here and added the Club to your inventory.\nNothing more to see here.\n\nSending you back to the frontroom")
                    press_to_continue()
                    break
                club_item = input("Inside you find a club, would you like to pick it up? (Y/N)")
                os.system('clear')
                if club_item != 'y' and club_item != 'n':
                    os.system('clear')
                    validate_yn()
                    continue
                if club_item == "y":
                    item_inventory.append("club")
                    print("Great you have added the club to your item inventory... you may need it.")
                    print("The club is all that is useful here.. guiding you back to the frontroom")
                else:
                    print("You have chosen not to take the club, there is not much else here...")
                    print("Guiding you back to the frontroom.")
            else:
                print(f"You dont have a key to open the door, you need to find that first.\n\nGuiding you back to the frontroom...")
            press_to_continue()
            user_choices_set.add(frontroom_door)
            break
        
        while frontroom_door == 3:
            os.system('clear')
            if 3 in user_choices_set:
                go_back_to_main = already_been_in_room()
                if go_back_to_main == 1:
                    break
            print("You have come to what appears to be an empty room.", end='\n\n')
            room3_stay = input("Would you like to stay and look around in this empty room? (Y/N)")
            room3_stay = room3_stay.lower()
            if room3_stay != "y" and room3_stay != "n":
                os.system('clear')
                validate_yn()
                continue
            #break

            if room3_stay == "n":
                print(f"You have chosen not to stay.\n\nGuiding you back to the front room: ")
                press_to_continue()
                room3_stay = None
                break

            while room3_stay == "y":
                os.system('clear')
                already_has_sword = 0
                if "sword" in item_inventory:
                    print(f"The room really is empty... remember you were already here and added found a sword to add to your inventory.\nNothing more to see here.\n\nSending you back to the frontroom")
                    already_has_sword = 1
                    press_to_continue()
                    break
                print("Good for you in your looking around you found a sword, you really need a weapon.", end='\n\n')
                sword_item = input("Would you like to pick up the sword (Y/N): ")
                sword_item = sword_item.lower()
                if sword_item != "y" and sword_item != "n":
                    validate_yn()
                    continue
                else:
                    if sword_item == "y":
                        item_inventory.append("sword")
                    room3_stay = None
                    break
            user_choices_set.add(frontroom_door)
            if already_has_sword == 1:
                break
            if "sword" in item_inventory:
                os.system('clear')
                print("Congrats.., you now have a sword! You are armed and ready "
                      "to fight whatever comes your way. ")
                print("You have found eveything here. We will guide you back to the front room. once there try one of the other doors.", end='\n\n')
            if "sword" not in item_inventory:
                os.system('clear')
                print("You chose not to pick up the sword, "
                      "once back in the front room enter any other room at your own parrel. ")
                print("We will guide you back to the front room.", end='\n\n')
            press_to_continue()
            break
        
        while frontroom_door == 4:
            os.system('clear')
            if 4 in user_choices_set:
                go_back_to_main = already_been_in_room()
                if go_back_to_main == 1:
                    break
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

            # Start Dragon Fight
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
                if "sword" in item_inventory:
                    battle_roll_mark = player_strength_sword
                    print(f"At least you came prepared with a Sword.\n\nYou will need to roll a 10 or better to score a hit.")
                elif "sword" not in item_inventory and "club" in item_inventory:
                    battle_roll_mark = player_strength_club
                    print(f"You only have a club to go against AssHat... good luck but i will not hold my breath.\n\nYou will need to roll a 13 or better to score a hit.")
                else:
                    battle_roll_mark = player_strengh_unarmed
                    print(f"You dont have a weapon, you certinaly have a death wish.\n\nYou will need to roll a 19 or better to score a hit.")

                while player_health > 0 and dragon_health > 0:
                    input("Press Enter to roll the dice: ")
                    roll20 = random.randint(1, 20)
                    print(f"battle_roll = {roll20}")
                    roll12 = random.randint(1, 12)
                    print(f"damage_roll = {roll12}")
                    if roll20 >= battle_roll_mark:
                        dragon_health -= roll12
                        print(f"You scored a hit: {dragon_name} has {dragon_health} points remaning")
                    elif roll20 < battle_roll_mark:
                        player_health -= roll12
                        print(f"Ouch! {dragon_name} got you.. you have {player_health} points remaning") 
                if player_health <= 0:
                    os.system('clear') 
                    print(f"{dragon_name} burned you alive, then ate you, waited an hour then pooped you out "
                        "so he could use you as compost for his collection of rare flowers. "
                        "(We told you he was a jerk...) \n\n")
                    print(f"Thus ends your quest... You may play again, however you have lost all the items you have collected.")
                    while  play_again != 'y' and play_again != 'n':
                        play_again = input("Would you like to play again? (Y/N) ")
                        play_again = play_again.lower()
                        if play_again != 'y' and play_again != 'n':
                            validate_yn()
                            continue
                    if play_again == "y":
                        item_inventory = []
                        user_choices_set = set()
                        dragon_fight_q = ""
                        dragon_health = 20
                        player_health = 20
                        play_again = None
                        #continue
                        break
                    if play_again == "n":
                        exit()
                if dragon_health <=0:
                    os.system('clear') 
                    print(victory)
                    if battle_roll_mark == player_strengh_unarmed:
                        print(f"No idea how you did it without a weapon but You killed {dragon_name}!!!! "
                            f"To the victor come the spoils!!! All of {dragon_name}'s treasure is yours")
                        exit() 
                    if battle_roll_mark == player_strength_club:    
                        print(f"You must be master with that club, amazing! You killed {dragon_name}!!!! "
                            f"To the victor come the spoils!!! All of {dragon_name}'s treasure is yours")
                        exit()
                    if battle_roll_mark == player_strength_sword:    
                        print(f"Wow you sure are good with that sword! You killed {dragon_name}!!!! "
                            f"To the victor come the spoils!!! All of {dragon_name}'s treasure is yours")
                        exit()

def main(username):
    os.system('clear')
    username = get_username()
    welcome_message = get_welcome_message(username)
    print(welcome_message)
    input("Press \"Enter\" to begin: ")
    base_game(username,user_choices_set,item_inventory,dragon_health,player_health,play_again) 
 
#####
#execution
#####

if __name__ == "__main__":
    main(username)