#!/usr/bin/python


import os
from datetime import datetime
import random

dragon_name = "AssHat"
dt = datetime.now()
item_inventory = []
user_choices_set = set()
dragon_health = 20
player_health = 20
player_strength_sword = 10
player_strength_club = 13
player_strengh_unarmed = 18                      

def get_username():
    """ Ask user for username and return it
    """
    user_name: str = input("Please enter your name: ")
    return user_name

def get_welcome_message(username):
    """ Sets welcome message. Takes username as input and retruns the message
    """
    welcome_message: str = f"Welcome to the world of Gary's mind, {username}... lets start to play!" 
    return welcome_message
    
def validate_yn():
    """ Simple text used when y/n questions do not validate.
    """
    print("Please try again and make sure to choose either \"Y\" or \"N\"" )
    input("Press \"Enter\" to continue: ")
    
def press_to_continue():
    """ Simple press enter to contiue
    """
    input("Press \"Enter\" to continue: ")
    
def try_again():
    """ Simple text again when input does not validate
    """
    os.system('clear')
    print("Please try again and make sure to choose one of the door numbers \"1-4\" or \"E\" to exit")
    press_to_continue()
    
    
def already_been_in_room():
    """ When a user has already entered a room they are given a choice if they want to continue on or go back to the main area.
        takes no inputs and returns y or n strings.
    """
    while True:
        print("You have already been to this room...")
        another_door_q = input(f"Would you like to choose another door? Y or N to continue into this door: ")
        if another_door_q.isalpha():
            another_door_q.lower()
            if another_door_q == "y":
                go_back_to_main: int = 1
                break
            if another_door_q == "n":
                go_back_to_main: int = 0
                break
            else:
                os.system('clear')
                print(f"Please enter only Y or N: Please try again\n")
    return go_back_to_main

def room_choice(username):
    """Main menu, user picks a door here. Takes username as an input, and returns the door number.
    """
    os.system('clear')
    try:
        getattr(room_choice, "has_run")
        print(f"{username}, You are back in the front room of the castle, please pick 1 of the 4 doors. ") 
    except AttributeError:
        setattr(room_choice, "has_run", True)
        print(f"{username}, You are in the front room of a large castle, there are 4 doors in front of you.\n" 
          "Each door has a number 1,2,3 or 4. ")
        print(f"\nChoose the door #1 by typing \"1\" door #2 by typing \"2\" etc... "
          "or type \"E\" to exit the game\n\n")
    frontroom_door = input("Make your choice (1-4 or E to exit): ")
    if frontroom_door.isalnum():
        if frontroom_door.isalpha():
            frontroom_door = frontroom_door.lower()
            if frontroom_door == 'e':
                print("Thank you for playing come back if you dare!")
                exit()
            else:
                try_again()
        elif frontroom_door.isnumeric():
            frontroom_door = int(frontroom_door)
            if frontroom_door not in range(1,5):
                try_again()
    else:
        try_again()
    return frontroom_door 

def room1(frontroom_door,user_choices_set):
    """Room1: takes frontroom_door and user_choices_set as inputs.
        - Room choice is added to the user_choices_set set.
        - Any item is added to the list inventory_list.
        - Returns no values.
    """
    os.system('clear')
    if 1 in user_choices_set:
        go_back_to_main = already_been_in_room()
        if go_back_to_main == 1:
            return
    while True:
        rm1_chest = input("The door opens and you find a chest.. Would you like to open it? (Y/N) ")
        rm1_chest = rm1_chest.lower()
        if rm1_chest != 'y' and rm1_chest != 'n':
            os.system('clear')
            validate_yn()
            continue
        break
    os.system('clear')
    if rm1_chest == 'y':
        if "skel_key" in item_inventory:
            print(f"The Chest is empty, you have already opened this Chest and added the key to your inventory.\nNothing more to see here.\n\nSending you back to the frontroom")
            press_to_continue()
            return
        else:
            print("In the chest you have found a key that you need, very good! It has been added to your inventory")
            item_inventory.append("skel_key")
            print(f"The key is the only worth while thing in this room.\n\nGuiding you back to the frontroom")
    else:
        print(f"You chose not to open the chest to see whats inside.\n\nSending you back to the frontroom.")           
    press_to_continue()
    user_choices_set.add(frontroom_door)
    return

def room2(frontroom_door,user_choices_set):
    """Room2: takes frontroom_door and user_choices_set as inputs.
        - Room choice is added to the user_choices_set set.
        - Any item is added to the list inventory_list.
        - Returns no values.
    """
    os.system('clear')
    if 2 in user_choices_set:
        go_back_to_main = already_been_in_room()   
        if go_back_to_main == 1:
            return
    while True:
        rm2_unlock = input("This door is locked. Do you have a key to open it? (Y/N) ")
        rm2_unlock = rm2_unlock.lower()
        os.system('clear')
        if rm2_unlock != "y" and rm2_unlock != "n":
            os.system('clear')
            validate_yn()
            continue
        break
    if "skel_key" in item_inventory and rm2_unlock == "y":
        print("You do have the skeleton key and it has worked to open the door...")
        if "club" in item_inventory:
            print(f"The room is empty, remember you were already here and added the Club to your inventory.\nNothing more to see here.\n\nSending you back to the frontroom")
            press_to_continue()
            return
        while True:
            club_item = input("Inside you find a club, would you like to pick it up? (Y/N)")
            club_item = club_item.lower()
            os.system('clear')
            if club_item != 'y' and club_item != 'n':
                os.system('clear')
                validate_yn()
                continue
            break
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
    return

def room3(frontroom_door,user_choices_set):
    """Room3: takes frontroom_door and user_choices_set as inputs.
        - Room choice is added to the user_choices_set set.
        - Any item is added to the list inventory_list.
        - Returns no values.
    """
    os.system('clear')
    if 3 in user_choices_set:
        go_back_to_main = already_been_in_room()
        if go_back_to_main == 1:
            return
    print("You have come to what appears to be an empty room.", end='\n\n')
    while True:
        room3_stay = input("Would you like to stay and look around in this empty room? (Y/N)")
        room3_stay = room3_stay.lower()
        if room3_stay != "y" and room3_stay != "n":
            os.system('clear')
            validate_yn()
            continue
        break
    if room3_stay == "n":
        print(f"You have chosen not to stay.\n\nGuiding you back to the front room: ")
        press_to_continue()
        room3_stay = None
        return
    if room3_stay == "y":
        os.system('clear')
        if "sword" in item_inventory:
            print(f"The room really is empty... remember you were already here and added found a sword to add to your inventory.\nNothing more to see here.\n\nSending you back to the frontroom")
            press_to_continue()
            return
        print("Good for you in your looking around you found a sword, you really need a weapon.", end='\n\n')
        while True:
            sword_item = input("Would you like to pick up the sword (Y/N): ")
            sword_item = sword_item.lower()
            os.system('clear')
            if sword_item != "y" and sword_item != "n":
                validate_yn()
                continue
            else:
                if sword_item == "y":
                    item_inventory.append("sword")
                room3_stay = None
            break
    user_choices_set.add(frontroom_door)
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
    return

def room4(frontroom_door,user_choices_set,item_inventory,dragon_health,player_health):
    """Room3: takes frontroom_door,user_choices_set, item_inventory, dragon_health and player_health as inputs.
        - Room choice (frontroom_door) is added to the user_choices_set var.
        - item_inventory is refrenced to see what items have been picked up, and any weapon seen will improve the users chance in the dragon fight.
        - player_health and dragon_health vars are initally set globally at 20.
        - Dice roll uses random to roll 2 dice.
        -- 1 battle roll - 20 sided - odds of wining are determined by the weapon used.
        --- ex if a sword is used then a 10 or better roll wins, if no weapon then a 18 or better will win.
        -- 1 damage roll - 12 sided - determines how much is deducted from the player or dragon health.
        - returns game_status (win/loss)
    """
    os.system('clear')
    if 4 in user_choices_set:
        go_back_to_main = already_been_in_room()
        if go_back_to_main == 1:
            return
        else:
            os.system('clear')
    user_choices_set.add(frontroom_door)
    if 4 in user_choices_set:
        print(f"So you are back to face {dragon_name}, he really is a jerk, good luck!!!\n\n")
    else:
        print(f"In this room you meet the dragon named {dragon_name}, That's his name because he's a jerk.\n\n")
    if "club" in item_inventory and "sword" not in item_inventory:
        print(f"You have a club and if you know how to use it, there are great treasures "
              f"if you can get past {dragon_name} the dragon..") 
        print("With great risk comes great reward!!!", end='\n\n')                
    elif "sword" in item_inventory:
        print(f"You have a sword and if you know how to use it, there are great treasures "
              f"if you can get past {dragon_name} the dragon..") 
        print("With great risk comes great reward!!!", end='\n\n')
    else:
        print(f"You do not have any weapons to fight {dragon_name}," 
              f"choose to fight only if you want to be lunch for {dragon_name}!", end='\n\n')
    print(f"Would you like to stay and fight {dragon_name}?", end='\n\n') 
    while True:
        dragon_fight_q = input("Y to Fight, or N to run away: (Y/N)")
        dragon_fight_q  = dragon_fight_q.lower()
        if dragon_fight_q  != "y" and dragon_fight_q  != "n":
            os.system('clear')
            validate_yn()
            continue
        break
    # Start Dragon Fight
    victory = f"""
                                  ___________
                             .---'::'        `---.
                            (::::::'              )
                            |`-----._______.-----'|
                            |              :::::::|
                           .|               ::::::!-.
                            |               :::::/|/
                            |               ::::::|
                            |  {username} the ::::|
                            |    {dragon_name}      ::::|
                            |     Slayer    ::::::|
                            |              .::::::|
                            |              :::::::|
                            '\'            :::::::/
                              `.        .:::::::'
                                `-._  .::::::-'
                                    |     |
                                    |  :::|
                                    |   ::|
                                   /     ::'\'  
                              __.-'      :::`-.__
                             (_           ::::::_)
                               `:::---------:::'
"""  
    
    if dragon_fight_q == "n":
        os.system('clear')
        if "sword" in item_inventory or "club" in item_inventory:
            print(f"You have a weapon, yet you have chosen not to face {dragon_name}... how dissapointing! "
                  "guiding you back to the front room. ")
            press_to_continue()
        else:
            print(f"Smart move not fighting {dragon_name} with out a weapon... "
                  "guiding you back to the front room")
            press_to_continue()
        game_status = base_game(username,user_choices_set,item_inventory,dragon_health,player_health)
    
    if dragon_fight_q == "y":
        os.system('clear')
        if "sword" in item_inventory:
            battle_roll_mark = player_strength_sword
            print(f"At least you came prepared with a Sword.\n\nYou will need to roll a {player_strength_sword} or better to score a hit.")
        elif "sword" not in item_inventory and "club" in item_inventory:
            battle_roll_mark = player_strength_club
            print(f"You only have a club to go against AssHat... good luck but i will not hold my breath.\n\nYou will need to roll a {player_strength_club} or better to score a hit.")
        else:
            battle_roll_mark = player_strengh_unarmed
            print(f"You dont have a weapon, you certinaly have a death wish.\n\nYou will need to roll a {player_strengh_unarmed} or better to score a hit.")
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
            game_status = "loss"
            os.system('clear') 
            print(f"{dragon_name} burned you alive, then ate you, waited an hour then pooped you out\n"
                "so he could use you as compost for his collection of rare flowers.\n"
                "(We told you he was a jerk...) \n\n")
            print(f"Thus ends your quest... \nYou may play again, however you have lost all the items you have collected.")
            return game_status

        if dragon_health <=0:
            game_status = "win"
            os.system('clear') 
            print(victory)
            if battle_roll_mark == player_strengh_unarmed:
                print(f"No idea how you did it without a weapon but You killed {dragon_name}!!!! "
                    f"\n\nTo the victor come the spoils!!! \n\nAll of {dragon_name}'s treasure is yours")
            if battle_roll_mark == player_strength_club:    
                print(f"You must be master with that club, amazing! You killed {dragon_name}!!!! "
                    f"\n\nTo the victor come the spoils!!! \n\nAll of {dragon_name}'s treasure is yours")
            if battle_roll_mark == player_strength_sword:    
                print(f"Wow you sure are good with that sword! You killed {dragon_name}!!!! "
                    f"\n\nTo the victor come the spoils!!! \n\nAll of {dragon_name}'s treasure is yours")
            return game_status

def play_game_again(item_inventory,game_status):
    """ Prompt user to play again and write game status to a file.
    """
    while True:
        play_again = input("Would you like to play again? (Y/N) ")
        play_again = play_again.lower()
        if play_again != 'y' and play_again != 'n':
            validate_yn()
            continue
        with open("gamestats.txt", "a") as file_out:
            file_out.write(f"{dt},{username},{game_status},{item_inventory}\n")
        return play_again

def base_game(username,user_choices_set,item_inventory,dragon_health,player_health):
    """Base game loop
        returns game_stats to main execution
    """
    while username != None:
        frontroom_door = room_choice(username)
        if frontroom_door == 1:
            room1(frontroom_door,user_choices_set)
        if frontroom_door == 2:
            room2(frontroom_door,user_choices_set)
        if frontroom_door == 3:
            room3(frontroom_door,user_choices_set)
        if frontroom_door == 4:
            gameStatus = room4(frontroom_door,user_choices_set,item_inventory,dragon_health,player_health)
            return gameStatus
 
#####
#execution
#####

if __name__ == "__main__":
    while True:
        os.system('clear')
        username = get_username()
        welcome_message = get_welcome_message(username)
        print(welcome_message)
        input("Press \"Enter\" to begin: ")
        game_status = base_game(username,user_choices_set,item_inventory,dragon_health,player_health)
        play_again = play_game_again(item_inventory,game_status)
        if play_again == "y":
            item_inventory = []
            user_choices_set = set()
            dragon_health = 20
            player_health = 20
            continue
        else: 
            print("Thank you for playing!") 
            break
