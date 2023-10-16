#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
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
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    #Used to check if the string from list of items is blank
    empty_check = list_of_items(room["items"])

    #If the string from list isn't blank will print out each item in the room. if the string is blank returns None
    if empty_check != "":
        print("There is" , empty_check , "here." + "\n")
    else:
        return


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    #Initalizes weight variable
    weight = 0

    #Used to check if the string from list of items is blank
    empty_check = list_of_items(items)

    #If the string from list isn't blank will print out each item in your inventroy. if the string is blank returns None
    if empty_check != "":
        print("You have" , empty_check + ".\n")



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
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    #prints out the name of the room in full calpitals and description with a blank lines after each
    print("\n" + room["name"].upper() + "\n")
    print(room["description"] + "\n")

    #checks if the print_room_items returns none. If not prints room items. 
    if print_room_items(room) != None:
        print(print_room_items(room) + "\n")

#outputs the name of the exit in a given diretion
def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    #returns the name of where the exit leads to
    return rooms[exits[direction]]["name"]

#prints out a direction and the associated exit
def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    #Prints out a given direction in caps and the exit it leads to
    print("GO " + direction.upper() + " to " + leads_to + ".")

#Prints out player inventory and all avalible actions the player can take in a given room
def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
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

#Chceks if an exit exists in a given direction
def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    #returns true if the chosen direction exits a rooms exits if not return false
    return chosen_exit in exits

#move the player into a new room based on the players input
def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    #makes sure the function is working with the global
    global current_room 

    #checks if the exit exists using is valid exit, then if true updates current room using the move command, if false prints no exits
    if is_valid_exit(current_room["exits"], direction) == True:
        current_room = move(current_room["exits"] ,direction)
    else:
        print("No exits" , direction)


#Coamnd used to take an item, adding it to the players inventory and remving it from the room
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

    #If the first word entered doesn't match any command tell user
    else:
        print("This makes no sense.")


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
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

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

        #check basic victory condition, seeing if every item is dropped in reception
        if len(victory_check) == len(rooms["Reception"]["items"]):
            print("Congrats you won")
            return


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

