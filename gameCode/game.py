#!/usr/bin/python3
import random
from time import sleep
import keyboard
from map import rooms
from player import *
from items import *
from gameparser import *
from text_art import *

#Slowing prints out a string one character at a time
def typewritter_effect_slow(text):
    # Keep track of printed text, so if skipped text can be finished
    printed = ''
    
    #Loops for each character in the string
    for char in text:
        #Slightly different pauses between each character
        sleep(random.uniform(0.05 , 0.1))
        #print out the character and make next character print besides it
        print(char, end='', flush=True)
        printed = printed + char
        
        # Detect skip condition
        if keyboard.is_pressed("s"):
            print(text.replace(printed, "", 1))
            break

#Slowing prints out a string one character at a time
def typewritter_effect_fast(text):
    # Keep track of printed text, so if skipped text can be finished
    printed = ''
    
    #Loops for each character in the string
    for char in text:
        #Slightly differant pauses between each character
        sleep(random.uniform(0.01 , 0.05))
        #print out the character and make next character print besides it
        print(char, end='', flush=True)
        printed = printed + char
        
        # Detect skip condition
        if keyboard.is_pressed("s"):
            print(text.replace(printed, "", 1))
            break

def list_of_items(items):
    #creates new empty list
    item_list = []

        # Append the item name for each item in the list
    for item in items:
        item_list.append(item["name"])

    # Return the list
    return ', '.join(item_list)

#does the same as list of items, but returns it as a list object rather than a list
def list_of_item_ids(items):
    list_of_items = []
    for item in items:
        list_of_items.append(item["id"])
    return list_of_items
        
#Prints a list of all items in a room
def print_room_items(room):

    #Used to check if the string from list of items is blank
    empty_check = list_of_items(room["items"])

    #If the string from list isn't blank will print out each item in the room. if the string is blank returns None
    if empty_check != "":
        print("There is" , empty_check , "here." + "\n")
    else:
        return

def print_inventory_items(items):
    # Get list of item names
    item_names = list_of_items(items)
    
    # Announce if there are no items
    if len(item_names) == '':
        print("You have nothing in your inventory.")
        return

    # Print the item names
    print("You have", item_names + ".")
    
    # Print blankline
    print()

def print_weight():
    # Initialises weight variable
    weight = 0
    
    #Adds together the weight value of each item in your inventory
    for i in range(len(inventory)):
        weight = weight + inventory[i]["weight"]

    #prints out the total weight you're carrying and shows the limit
    print("You are carrying" , str(weight) + "/" + str(weight_limit) + "kg!")

#Prints out all information about the room you're currently ins
def print_room(room):
    #prints out the name of the room in full capitals and description with a blank line after each
    typewritter_effect_slow(("\n" + room["name"].upper() + "\n"))
    typewritter_effect_fast((room["description"] + "\n"))

    #checks if the print_room_items returns none. If not prints room items. 
    if print_room_items(room) != None:
        typewritter_effect_fast((print_room_items(room) + "\n"))

#outputs the name of the exit in a given diretion
def exit_leads_to(exits, direction):
    #returns the name of where the exit leads to
    return rooms[exits[direction]]["name"]

#prints out a direction and the associated exit
def print_exit(direction, leads_to):
    #Prints out a given direction in caps and the exit it leads to
    print("GO " + direction.upper() + " to " + leads_to + ".")

#Prints out player inventory and all available actions the player can take in a given room
def print_menu(exits, room_items, inv_items):

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    # Print statement for each available item
    for item in room_items:
        print("TAKE", item["id"].upper() , "to take" , item["name"] + ".")
    
    # Print statement for each item in the inventory
    for item in inv_items:
        if item != item_chucky:
            #if there is already an article use that, otherwise use your
            if list(item["name"])[0] == "a" or list(item["name"])[0] == "the":
                print("DROP", item["id"].upper() , "to drop" , item["name"] + ".")
            else:
                print("DROP", item["id"].upper() , "to drop your" , item["name"] + ".")

    
    if has_chucky() == True and current_room == rooms["Living Room"]:
        print("DROP DOLL to cast Chucky into the fireplace.")

    #Print statement for each inventory item
    for item in inventory:
     print("INSPECT" , item["id"].upper() , "to view its description.")
    
        
    #if there's a character print that
    if current_room["character"] is not None:
        print("TALK to", current_room["character"]["name"])

    if item_pizza in inventory:
        print("EAT PIZZA to eat your pizza slice and gain some health.")

        #Prompt player to create monster and win game
        #Count used to check if all 6 monster parts are in the lab
        victory = 0
        #checks the current room is the lab
        if current_room == rooms["Lab"]:
            #loops for every iyem in the victory check list (contains all monster parts)
            for item in victory_check:
                #If the part is in the lab adds one to the victory counter
                if item in current_room["items"]:
                    victory += 1

            #If all parts are in the lab (counter = 6) and thread in inventory allows promts player with create command
            if victory == 6 and item_needle_and_thread in inventory:
                global create_allowed
                create_allowed = True
                print("CREATE MONSTER to sew together your monster")


    if health > 80:
            print("You feel exceptionaly healthy (" + str(health) + ")")

    elif health > 60:
            print("You feel healthy (" + str(health) + ")")


    elif health > 40:
            print("You're starting to feel week (" + str(health) + ")")

    elif health > 20:
            print("You're fading  (" + str(health) + ")")

    elif health > 0:    
        print("You have one foot in the grave (" + str(health) + ")")
        
    #prompt the player for an input    
    print("What do you want to do?")

#Checks if an exit exists in a given direction
def is_valid_exit(exits, chosen_exit):
    #returns true if the chosen direction exits a rooms exits if not return false
    return chosen_exit in exits

#move the player into a new room based on the players input
def execute_go(direction):
    #makes sure the function is working with the global
    global current_room 

    #checks if the exit exists using is valid exit, then if true updates current room using the move command, if false prints no exits
    if is_valid_exit(current_room["exits"], direction) == True:
        current_room = move(current_room["exits"] ,direction)
    else:
        print("No exits" , direction)

#Command used to take an item, adding it to the players inventory and removing it from the room
def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    #initializes weight
    weight = 0

    #loops through each item in the players inventory adding up their weights
    for item in inventory:
        weight += item["weight"]

    #Loops through for every item in the current room
    for i in range(len(current_room["items"])):
        #checks if the item given in the command matches the current item in the list
        if item_id == current_room["items"][i]["id"]:
            #if true checks that the weight won't go over the weight limit
            if weight + current_room["items"][i]["weight"] > weight_limit:
                #If weight exceeds limit prevents the item from being added to the player inventory
                print("cannot take" , current_room["items"][i]["name"] , "it's too heavy for you. Drop a heavy item to pick this up")
                return
            #if weight doesn't exceed the limit the item is added to the player inventory and removed from the room
            inventory.append(current_room["items"][i])
            current_room["items"].remove(current_room["items"][i])
            #returns to break search loop to prevent an error
            return 

#command to drop item from inventory and add it to the remove
def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    #loops through the list for every item in it
    for item in inventory:
        #if the item entered in the command is in the players inventory add it to the room and remove from inventory
        if item_id == item["id"]:
            if item_id == "doll":
                kill_chucky()
                return
            current_room["items"].append(item)
            inventory.remove(item)
            #return to leave the loop
            return
    print("You cannot drop that.")

def execute_inspect(item_id):
     #loops through the list for every item in it
    for item in inventory:
         #if the item entered in the command is in the players inventory add it to the room and remove from inventory
        if item_id == item["id"]:
            typewritter_effect_fast(item["description"] + "\n")
            return

#Function to run combat using the charater and chosen weapon as inputs
def execute_combat(weapon, foe):
    #tell the compiler to treat health as a global to prevent global errors
    global health
    #Loops through the combat list of a characer checking for the selected weapon
    for option in foe["combat"]:
        
        if option[0] == weapon:
            #If the Weapon is found in the combat list deals damage based on the health value in the tuple
            health -= option[1]
            
            #Prints a small statement based on "quality" of the combat
            if option[1] == 0:
                print("Well done perfectly executed")
                #give the limb and remove the character: they have died
                give_limb()
                remove_character()
            else:
                #give the limb and remove the character: they have died
                give_limb()
                remove_character()
                print("An ok performance")
            return

    #If the chosen weapon is not found combat is considered poor and greater damage is taken
    health -= 30
    print("A poor performance indeed")
    #give the limb and remove the character: they have died
    give_limb()
    remove_character()
    
#take the users input and execute a certain command based on the nomalised input
def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    #if nothing is input simply return and do nothing
    if 0 == len(command):
        return

    #if the first word in list is go execute the go command, if only go is entered and no second word prompt user to enter more
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
            #Returns true only if the character moves rooms (only needs to see the description if they've just moved room)
            return True
        else:
            print("Go where?")
            return False

    #if the first word in list is take execute the take command, if only take is entered and no second word prompt user to enter more
    elif command[0] == "take":
        if len(command) > 1:
            execute_take(' '.join(command[1:]))
            return False
        else:
            print("Take what?")
            return False

    #if the first word in list is drop execute the drop command, if only drop is entered and no second word prompt user to enter more
    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(' '.join(command[1:]))
            return False
        else:
            print("Drop what?")
            return False

    elif command[0] == "talk":
        if len(command) > 1:
            global current_room
            #print text art for current character
            display_character(current_room["character"])
            execute_dialogue(current_room["character"]["dialogue"])
            return False
        else:
            print("Talk to who?")
            return False
        
    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(" ".join(command[1:]))
        else:
            print("Inspect what?")

    elif command[0] == "create":
            if create_allowed == True:
                if len(command) > 1:
                    print("Fun win text")
                    #display frankenstein image
                    print(frankenstein)
                    exit()
                else:
                    print("Create what?")
            else:
                print("Too fast there get the monster parts first")

    elif command[0] == "eat":
            if item_pizza in inventory:
                if len(command) > 1:
                    typewritter_effect_fast("mmmmmm tasty pizza.")
                    health = health + (random.randrange(0 , 10) * 10)
                    inventory.remove(item_pizza)
                else:
                    print("Eat what?")
            else:
                print("No pizza to eat :(.")

    #If the first word entered doesn't match any command tell user
    else:
        print("This makes no sense.")

#take the dialogue of the character and print it out in an iterable list, sometimes taking an input from the character
def execute_dialogue(dialogue):
    #dialogue dictionary from character
    if check_interacted() and dialogue["method"] == "talk":
        execute_talk(dialogue["repeat dialogue"])
        return
            
    #if there are multiple options, to fight or talk, let the player pick
    if dialogue["multiple options"]:
        #user interacts with character based on their base dialogue, however their responses are not linked to user input
        for sentence in dialogue["base dialogue"]:
            typewritter_effect_fast(sentence)
            sleep(.5)
            print()
        normalised_input = ''
        while normalised_input != 'talk' and normalised_input != 'fight':
            typewritter_effect_slow("TALK or FIGHT:")
            print()
            user_input = input("> ")
            normalised_input = ''.join(normalise_input(user_input))
            
        if normalised_input == 'talk':
            #print the sentences in character interaction
            execute_talk(dialogue["dialogue one"])
            #give the player the limb
            give_limb()
                
        elif normalised_input == 'fight':
            #provide the fighting text if the player chooses to fight
            execute_fight(dialogue["dialogue two"])
    
    elif dialogue["method"] == "fight":
        execute_fight(dialogue["base dialogue"])

    elif dialogue["method"] == "talk":
        #print the sentences in character interaction
        execute_talk(dialogue["base dialogue"])
        #give the player the limb
        give_limb()
        
#executes a player fighting one of the characters, taking a list of dialogue to print to the player
def execute_fight(fight_dialogue):
    for sentence in fight_dialogue:
        typewritter_effect_fast(sentence)
        #pause between each sentence for better understanding
        sleep(0.5)
        print()
        
    print()
    print("CHOOSE YOUR WEAPON")
    print(", ".join(list_of_item_ids(inventory)))
    normalised_input = ''
    #allow the weapon to be shout for pennywise, but otherwise it has to be in the inventory
    while normalised_input not in list_of_item_ids(inventory) and normalised_input != 'shout':
        weapon = input("> ")
        normalised_input = ' '.join(normalise_input(weapon))
    execute_combat(weapon, current_room["character"]) 

#executes a player talking to one of the characters, taking a list of dialogue to print to the player
def execute_talk(talk_dialogue):
    for sentence in talk_dialogue:
        #provide the talking text if the player chooses talk
        typewritter_effect_fast(sentence)
        #pause between each sentence for better understanding
        sleep(0.5)
        print()
    print()

#gives the player the limb currently in the room after a successful interaction
def give_limb():
    inventory.append(current_room["character"]["defending_body_part"])
    current_room["character"]["defending_body_part"] = None
    
#removes the character when it dies
def remove_character():
    current_room["character"] = None
   
#checks if the player has interacted with the character before     
def check_interacted():
    if current_room["character"]["defending_body_part"] is None:
        return True
    else:
        return False

def has_chucky():
    for item in inventory:
        if item["id"] == "doll":
            return True
    return False

def kill_chucky():
    if current_room["name"] == "Living Room":
        typewritter_effect_fast("You drop Chucky into the fireplace, he screams as he melts on the fire, and with it any risk to you is diminished.")
        for item in inventory:
            if item["id"] == "doll":
                inventory.remove(item)
    else:
        typewritter_effect_fast("You cannot drop Chucky, the only way to get rid of him is to drop him in the living room fireplace.")

def check_chucky():
    if not has_chucky():
        return
    global health
    health -= 10
    typewritter_effect_fast("""Oh no! It seems that doll is not what it appears, you have Chucky! He is now going to follow you everywhere you go, taking your health (-10)
unless he is destroyed. Drop him in the fireplace (Living Room) to kill him.""")

def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    #returns the normalised input
    return normalised_user_input

def move(exits, direction):
    # Next room to go to
    return rooms[exits[direction]]

# This is the entry point of our program
def main():
    # Tell them how to skip
    print(haunted_house)
    print("Press S to skip.")
    typewritter_effect_fast("""Welcome to the haunted house, each room before you holds ancient secrets for you to unlock. Join us on an adventurous journey where you will meet suspicious 
individuals, some of which you might recognise from your favourite halloween productions. Along the way you will be able to talk to characters and battle some of the 
most famous horror villains. You are playing as Henry Frankenstein and your goal is to collect each limb of your monster in order to overcome the haunted 
house and build the monster. """)
    
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)
        print()
        check_chucky()

        #jumpscare 10% of the time the player moves srooms
        num = random.randint(0, 100)
        if num % 10 == 0:
            print(jumpscare())
            sleep(1)

        character_moved_room = False
        while not character_moved_room:
            # Show the menu with possible actions and ask the player
            command = menu(current_room["exits"], current_room["items"], inventory)
            print()
            # Execute the player's command
            character_moved_room = execute_command(command)

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

