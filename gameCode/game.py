#!/usr/bin/python3
import random
from time import sleep
from map import rooms
from player import *
from items import *
from gameparser import *

#Slowing prints out a string one character at a time
def typewritter_effect_slow(text):
    #Loops for each character in the string
    for char in text:
        #Slightly different pauses between each character
        sleep(random.uniform(0.025 , 0.015))
        #print out the character and make next character print besides it
        print(char, end='', flush=True)

#Slowing prints out a string one character at a time
def typewritter_effect_fast(text):
    #Loops for each character in the string
    for char in text:
        #Slightly differant pauses between each character
        sleep(random.uniform(0.01 , 0.05))
        #print out the character and make next character print besides it
        print(char, end='', flush=True)

def list_of_items(items):
    #creates new empty list
    item_list = []

    #Adds the name of each item to the new list
    for i in range(len(items)):
        item_list.append(items[i]["name"])
        
    #joins all the items in the list into one string seperated by commas
    item_names = str(", ".join(item_list))
    #returns the list created
    return item_names 

#Prints a list of all items in a room
def print_room_items(room):

    #Used to check if the string from list of items is blank
    empty_check = list_of_items(room["items"])

    #If the string from list isn't blank will print out each item in the room. if the string is blank returns None
    if empty_check != "":
        typewritter_effect_fast(("There is" , empty_check , "here." + "\n"))
    else:
        return


def print_inventory_items(items):
    #Initalizes weight variable
    weight = 0

    #Used to check if the string from list of items is blank
    empty_check = list_of_items(items)

    #If the string from list isn't blank will print out each item in your inventroy. if the string is blank returns None
    if empty_check != "":
        typewritter_effect_fast(("You have " , empty_check + ".\n"))

        #!!!!! Doc Test doesnt like it printing weight !!!!!
        #Adds together the weight value of each item in your inventory
        #for i in range(len(inventory)):
        #    weight = weight + inventory[i]["weight"]

        #prints out the total weight your carrying and shows the limit
        ##print("you are carying" , weight , "/" , weight_limit , "!")
    else:
        return

#Prints out all information about the room your currently in
def print_room(room):
    #prints out the name of the room in full calpitals and description with a blank lines after each
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

#Prints out player inventory and all avalible actions the player can take in a given room
def print_menu(exits, room_items, inv_items):

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    #For every item in the current room print out take, its ID in caps and name 
    for i in range(len(room_items)):
        print("TAKE" , room_items[i]["id"].upper() , "to take" , room_items[i]["name"])

    #For every item in your inventory print out drop, its ID in caps and name
    for i in range(len(inv_items)):
        print("DROP" , inv_items[i]["id"].upper() , "to drop your" , inv_items[i]["name"])
    
    #promt the player for an input
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

#Command used to take an item, adding it to the players inventory and remving it from the room
def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    #initializes weight
    weight = 0

    #loops through each item in the players inventory adding up their weights
    for i in range(len(inventory)):
            weight = weight + inventory[i]["weight"]

    #Loops through for every item in the current room
    for i in range(len(current_room["items"])):
        #checks if the item given in the command matches the current item in the list
        if item_id == current_room["items"][i]["id"]:
            #if true checks that the weight wont go over the weight limit
            if weight + current_room["items"][i]["weight"] > weight_limit:
                #If weight excedes limit prevents the item from being added to the player inventory
                print("cannot take" , current_room["items"][i]["name"] , "its too heavy for you. Drop a heavy item to pick this up")
                return
            #if weight doesn't excede the limit the item is added to the player inventory and removed from the room
            inventory.append(current_room["items"][i])
            current_room["items"].remove(current_room["items"][i])
            #returns to break search loop to prevent an error
            return 

#command to drop item from inventroy and add it to the remove
def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    #loops through the list for every item in it
    for i in range(len(inventory)):
        #if the item entered in the command is in the players inventory add it to the room and remove from inventory
        if item_id == inventory[i]["id"]:
            current_room["items"].append(inventory[i])
            inventory.remove(inventory[i])
            #return to leave the loop
            return

#Function to run combat using the charater and chosen weapon as inputs
def execute_combat(weapon, foe):
    #Loops through the combat list of a characer checking for the selected weapon
    for i in len(foe["combat"]):
        
        if foe["combat"][i] == weapon:
            #If the Weapon is found in the combat list deals damage based on the next value in the list
            health = health - foe["combat"][i+1]
            
            #Prints a small statement based on "quality" of the combat
            if foe["combat"][i+1] == 0:
                print("Well done perfectly exectued")
            else:
                print("An ok performance")
            return

    #If the chosen weapon is not found combat is considered poor and greater damage is taken
    health = health - 30
    print("A poor performance indeed")


    
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

    #if the first word in list is go execute the go command, if only go is entered and no second word promt user to enter more
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    #if the first word in list is take execute the take command, if only take is entered and no second word promt user to enter more
    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    #if the first word in list is drop execute the drop command, if only drop is entered and no second word promt user to enter more
    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "talk":
        if len(command) > 1:
            global current_room
            execute_talk(current_room["character"]["dialogue"])
        else:
            print("Talk to who?")
        
    #If the first word entered doesn't match any command tell user
    else:
        print("This makes no sense.")

#take the dialogue of the character and print it out in an iterable list, sometimes taking an input from the character
def execute_talk(dialogue):
    global current_room #tell the compiler to use current_room as a global to avoid global errors
    #dialogue dictionary from character
    #user interacts with character based on their base dialogue, however their responses are not linked to user input
    for sentence in dialogue["base dialogue"]:
            typewritter_effect_fast(sentence)
            sleep(.5)
            print()
            
    #if there are multiple options, to fight or talk, let the player pick
    if dialogue["multiple options"]:
        user_input = ''
        while normalise_input(user_input)[0] != "talk" or normalise_input(user_input)[0] != "fight":
            typewritter_effect_slow("Talk or Fight")
            user_input = input("> ")
            
            if normalise_input(user_input)[0] == "talk":
                for sentence in dialogue["dialogue one"]:
                    #provide the talking text if the player chooses talk
                    typewritter_effect_fast(sentence)
                    #pause between each sentence for better understanding
                    sleep(0.5)
                    print()
                #give the character the limb
                inventory.append(current_room["character"]["defending_body_part"])
                    
            elif normalise_input(user_input)[0] == "fight":
                #provide the fighting text if the player chooses to fight
                for sentence in dialogue["dialogue two"]:
                    typewritter_effect_fast(sentence)
                    #pause between each sentence for better understanding
                    sleep(0.5)
                    print()
                print("CHOOSE YOUR WEAPON FROM YOUR INVENTORY")
                weapon = ''
                while ''.join(normalise_input(weapon)) not in inventory:
                    weapon = input("> ")
                execute_combat(weapon, current_room["character"]) 
                # implement being given the limb
    
    elif dialogue["method"] == "fight":
        for sentence in dialogue["base dialogue"]:
            typewritter_effect_fast(sentence)
            #pause between each sentence for better understanding
            sleep(0.5)
            print()
        print("CHOOSE YOUR WEAPON FROM YOUR INVENTORY")
        weapon = ''
        while ''.join(normalise_input(weapon)) not in inventory:
            weapon = input("> ")
        execute_combat(weapon, current_room["character"]) 
        # implement being given the limb

    elif dialogue["method"] == "talk":
        for sentence in dialogue["base dialogue"]:
            typewritter_effect_fast(sentence)
            #pause between each sentence for better understanding
            sleep(0.5)
            print()
        #give the character the limb
        inventory.append(current_room["character"]["defending_body_part"])
        

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

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

