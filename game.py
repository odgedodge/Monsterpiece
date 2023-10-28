#!/usr/bin/python3
import random
from time import sleep
import keyboard
from map import rooms
from player import *
from items import *
from gameparser import *
from text_art import *
import sys

class Game:
    def __init__(self, characters, player, map):
        self.__game_over = False
        self.__characters = characters
        self.__player = player
        self.__map = map
    
    def typewriter_effect(self, text):
        character_print_time = random.uniform(0.01, 0.05)
        pressed_s = False

        for character in text:
            if keyboard.is_pressed("s"):
                pressed_s = True
                character_print_time = 0
            
            sys.stdout.write(character)
            sys.stdout.flush()
            sleep(character_print_time)

        if pressed_s:
            keyboard.press_and_release("backspace")
    
    def list_of_items(self, items):
        """This function returns a string expressing a list of item names, from a list of items given"""
        #creates new empty list
        item_list = []

            # Append the item name for each item in the list
        for item in items:
            item_list.append(item["name"])

        # Return the list
        return ', '.join(item_list)

    #does the same as list of items, but returns it as a list object rather than a list
    def list_of_item_ids(self, items):
        """This function returns a list of item ids, from a list of items given"""
        list_of_items = []
        for item in items:
            list_of_items.append(item["id"])
        return list_of_items
    
    #Prints out player inventory and all available actions the player can take in a given room
    def print_menu(self, exits, room_items, inv_items):
        #Sleeps after each print statement to allow user to read
        print()
        print("You can:")
        # Iterate over available exits
        for direction in exits:
            # Print the exit name and where it leads to
            self.__player.print_exit(direction, self.player.exit_leads_to(exits, direction))
            sleep(0.2)

        # Print statement for each available item
        for item in room_items:
            print("TAKE", item["id"].upper() , "to take" , item["name"] + ".")
            sleep(0.2)
        
        # Print statement for each item in the inventory
        for item in inv_items:
            if item != item_chucky:
                #if there is already an article use that, otherwise use your
                if list(item["name"])[0] == "a" or list(item["name"])[0] == "the":
                    print("DROP", item["id"].upper() , "to drop" , item["name"] + ".")
                    sleep(0.2)
                else:
                    print("DROP", item["id"].upper() , "to drop your" , item["name"] + ".")
                    sleep(0.2)

        # prints the instruction to kill chucky if necessary
        if self.has_chucky() == True and current_room == rooms["Living Room"]:
            print("DROP DOLL to cast Chucky into the fireplace.")
            sleep(0.2)

        #Print statement for each inventory item
        for item in inventory:
            print("INSPECT" , item["id"].upper() , "to view its description.")
            sleep(0.2)
            
        #if there's a character print that
        if current_room["character"] is not None:
            print("TALK to", current_room["character"]["name"])
            sleep(0.2)

        if item_pizza in inventory:
            print("EAT PIZZA to eat your pizza slice and gain some health.")
            sleep(0.2)
            
        self.__player.print_health()
        sleep(0.2)

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
                sleep(0.2)
            
        #prompt the player for an input  
        print()  
        print("What do you want to do?")
        
    #Checks if an exit exists in a given direction
    def is_valid_exit(self, exits, chosen_exit):
        #returns true if the chosen direction exits a rooms exits if not return false
        return chosen_exit in exits

    #move the player into a new room based on the players input
    def execute_go(self, direction):
        #makes sure the function is working with the global
        global current_room 

        #checks if the exit exists using is valid exit, then if true updates current room using the move command, if false prints no exits
        if self.is_valid_exit(current_room["exits"], direction) == True:
            current_room = self.move(current_room["exits"] ,direction)
        else:
            print("No exits" , direction, ".")

    #Command used to take an item, adding it to the players inventory and removing it from the room
    def execute_take(self, item_id):
        """This function takes an item_id as an argument and moves this item from the
        list of items in the current room to the player's inventory. However, if
        there is no such item in the room, this function prints
        "You cannot take that."
        """

        for item in current_room["items"]:
            #checks if the item given in the command matches the current item in the list
            if item_id == item["id"]:
                if self.__player.weight_check(item):
                    #if weight doesn't exceed the limit the item is added to the player inventory and removed from the room
                    inventory.append(item)
                    current_room["items"].remove(item)
                    #returns to break search loop to prevent an error
                    return 
            
    #command to drop item from inventory and add it to the remove
    def execute_drop(self, item_id):
        """This function takes an item_id as an argument and moves this item from the
        player's inventory to list of items in the current room. However, if there is
        no such item in the inventory, this function prints "You cannot drop that."
        """
        #loops through the list for every item in it
        for item in inventory:
            #if the item entered in the command is in the players inventory add it to the room and remove from inventory
            if item_id == item["id"]:
                if item_id == "doll":
                    self.kill_chucky()
                    return
                current_room["items"].append(item)
                inventory.remove(item)
                #return to leave the loop
                return
        print("You cannot drop that.")

    def execute_inspect(self, item_id):
        #loops through the list for every item in it
        for item in inventory:
            #if the item entered in the command is in the players inventory add it to the room and remove from inventory
            if item_id == item["id"]:
                self.typewriter_effect(item["description"] + "\n")
                return

    #Function to run combat using the charater and chosen weapon as inputs
    def execute_combat(self, weapon, foe):
        #tell the compiler to treat health as a global to prevent global errors
        #Loops through the combat list of a characer checking for the selected weapon
        for option in foe["combat"]:
            
            if option[0] == weapon:
                #If the Weapon is found in the combat list deals damage based on the health value in the tuple
                health = self.__player.get_health()
                health -= option[1]
                
                #Prints a small statement based on "quality" of the combat
                if option[1] == 0:
                    print()
                    print("Well done, perfectly executed.")
                    #give the limb and remove the character: they have died
                    self.give_limb()
                    self.remove_character()
                else:
                    #give the limb and remove the character: they have died
                    self.give_limb()
                    self.remove_character()
                    print("An ok performance.")
                    self.health_check()
                return

        #If the chosen weapon is not found combat is considered poor and greater damage is taken
        health -= 30
        print("A poor performance indeed. You have lost 30 health.")
        self.__player.health_check()
        
    #take the users input and execute a certain command based on the nomalised input
    def execute_command(self, command):
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
                self.execute_go(command[1])
                #Returns true only if the character moves rooms (only needs to see the description if they've just moved room)
                return True
            else:
                print("Go where?")
                return False

        #if the first word in list is take execute the take command, if only take is entered and no second word prompt user to enter more
        elif command[0] == "take":
            if len(command) > 1:
                self.execute_take(' '.join(command[1:]))
                return False
            else:
                print("Take what?")
                return False

        #if the first word in list is drop execute the drop command, if only drop is entered and no second word prompt user to enter more
        elif command[0] == "drop":
            if len(command) > 1:
                self.execute_drop(' '.join(command[1:]))
                return False
            else:
                print("Drop what?")
                return False

        elif command[0] == "talk":
            if len(command) > 1:
                global current_room
                #print text art for current character
                display_character(current_room["character"])
                self.execute_dialogue(current_room["character"]["dialogue"])
                return False
            else:
                print("Talk to who?")
                return False
            
        elif command[0] == "inspect":
            if len(command) > 1:
                self.execute_inspect(" ".join(command[1:]))
            else:
                print("Inspect what?")

        elif command[0] == "create":
                if create_allowed == True:
                    if len(command) > 1:
                        print("Congratulations, you win!")
                        self.typewriter_effect("Now get away while you still can...")
                        #display frankenstein image
                        print(frankenstein)
                        self.__game_over = True
                    else:
                        print("Create what?")
                else:
                    print("Too fast there, get the monster parts first.")

        elif command[0] == "eat":
                if item_pizza in inventory:
                    if len(command) > 1:
                        self.typewriter_effect("mmmmmm tasty pizza.")
                        health = self.__player.get_health()
                        health += (random.randrange(0 , 10) * 10)
                        inventory.remove(item_pizza)
                    else:
                        print("Eat what?")
                else:
                    print("No pizza to eat :(.")

        #If the first word entered doesn't match any command tell user
        else:
            print("This makes no sense.")

    #take the dialogue of the character and print it out in an iterable list, sometimes taking an input from the character
    def execute_dialogue(self, dialogue):
        #dialogue dictionary from character
        if self.check_interacted() and (dialogue["method"] == "talk" or dialogue["method"] == "deal"):
            self.execute_talk(dialogue["repeat dialogue"])
            return
                
        #if there are multiple options, to fight or talk, let the player pick
        if dialogue["multiple options"]:
            #user interacts with character based on their base dialogue, however their responses are not linked to user input
            for sentence in dialogue["base dialogue"]:
                self.typewriter_effect(sentence)
                sleep(.5)
                print()
            normalised_input = ''
            while normalised_input != 'talk' and normalised_input != 'fight':
                self.typewriter_effect("TALK or FIGHT:")
                print()
                user_input = input("> ")
                normalised_input = ''.join(normalise_input(user_input))
                
            if normalised_input == 'talk':
                #print the sentences in character interaction
                self.execute_talk(dialogue["dialogue one"])
                #give the player the limb
                self.give_limb()
                    
            elif normalised_input == 'fight':
                #provide the fighting text if the player chooses to fight
                self.execute_fight(dialogue["dialogue two"])
        
        elif dialogue["method"] == "fight":
            self.execute_fight(dialogue["base dialogue"])

        elif dialogue["method"] == "talk":
            #print the sentences in character interaction
            self.execute_talk(dialogue["base dialogue"])
            #give the player the limb
            self.give_limb()
            
        elif dialogue["method"] == "deal":
            self.execute_deal(dialogue)
            
    #executes a player fighting one of the characters, taking a list of dialogue to print to the player
    def execute_fight(self, fight_dialogue):
        for sentence in fight_dialogue:
            self.typewriter_effect(sentence)
            #pause between each sentence for better understanding
            sleep(0.5)
            print()
            
        print()
        print("CHOOSE YOUR WEAPON")
        print("Remember, you can always run.")
        #Print inventory items
        if len(inventory) != 0:
            print("You have",", ".join(self.list_of_item_ids(inventory)), "available.")
        else:
            print("You have no items in your inventory to fight with.")
        normalised_input = ''
        #allow the weapon to be shout for pennywise, but otherwise it has to be in the inventory
        while normalised_input not in self.list_of_item_ids(inventory) and normalised_input != 'shout' and normalised_input != "run":
            weapon = input("> ")
            normalised_input = ' '.join(normalise_input(weapon))
        if normalised_input == "run":
            return
        self.execute_combat(normalised_input, current_room["character"]) 

    #executes a player talking to one of the characters, taking a list of dialogue to print to the player
    def execute_talk(self, talk_dialogue):
        for sentence in talk_dialogue:
            #provide the talking text if the player chooses talk
            self.typewriter_effect(sentence)
            #pause between each sentence for better understanding
            sleep(0.5)
            print()
        print()

    def execute_deal(self, dialogue):
        #print the sentences in character interaction
            for sentence in dialogue["base dialogue"]:
                self.typewriter_effect(sentence)
                sleep(0.5)
                print()
            #allow the player to either choose to give the gift or to leave the interaction
            print("Gift or Leave")
            normalised_input = ''
            while normalised_input != "gift" and normalised_input != "leave":
                user_input = input('> ')
                normalised_input = ' '.join(normalise_input(user_input))
            #if the user gifts, they can choose which item from their inventory to give, otherwise leaving results in ending the interaction
            if normalised_input == "gift":
                print("CHOOSE YOUR GIFT")
                if len(inventory) != 0:
                    print("You have",", ".join(self.list_of_item_ids(inventory)), "available.")
                else:
                    print("You have no items in your inventory to fight with.")
                normalised_gift = ''
                while not normalised_gift in self.list_of_item_ids(inventory):
                    gift = input('> ')
                    normalised_gift = ' '.join(normalise_input(gift))
                #if the gift is correct, give the limb to the player
                if normalised_gift == dialogue["gift"]:
                    for sentence in dialogue["successful dialogue"]:
                        self.typewriter_effect(sentence)
                        sleep(0.5)
                        print()
                    for item in inventory:
                        if item["id"] == normalised_gift:
                            inventory.remove(item)
                    self.give_limb()
                else:
                    for sentence in dialogue["unsuccessful dialogue"]:
                        self.typewriter_effect(sentence)
                        sleep(0.5)
                        print()

    #gives the player the limb currently in the room after a successful interaction
    def give_limb(self):
        if self.weight_check(current_room["character"]["defending_body_part"]):
            inventory.append(current_room["character"]["defending_body_part"])
            print()
            print("You have the", str(current_room["character"]["defending_body_part"]["id"]) + ".")
            current_room["character"]["defending_body_part"] = None
        else:
            current_room["items"].append(current_room["character"]["defending_body_part"])
            print()
            print("The", str(current_room["character"]["defending_body_part"]["id"]) , "is too heavy to take, so it is now available to pick up from the room.")
            current_room["character"]["defending_body_part"] = None
    
    # This is the entry point of our program
    def main(self):
        # Tell them how to skip
        print(haunted_house)    
        print()
        print("Press S to skip.")
        self.typewriter_effect("""Welcome to the haunted house, each room before you holds ancient secrets for you to unlock. Join us on an adventurous 
    journey where you will meet suspicious individuals, some of which you might recognise from your favourite halloween 
    productions. Along the way you will be able to talk to characters and battle some of the most famous horror villains. You
    are playing as Victor Frankenstein and your goal is to collect each limb of your monster in order to overcome the haunted 
    house and build the monster. """)
        print()
        
        # Main game loop
        while not game_over:
            # Display game status (room description, inventory etc.)
            self.print_room(current_room)
            print()
            self.print_inventory_items(inventory)
            
            #chucky affects health, so game-over has to be checked
            self.check_chucky()
            if game_over:
                break

            #jumpscare 10% of the time the player moves srooms
            num = random.randint(0, 100)
            if num % 10 == 0:
                jumpscare()
                sleep(1)

            character_moved_room = False
            while not character_moved_room:
                # Show the menu with possible actions and ask the player
                command = self.menu(current_room["exits"], current_room["items"], inventory)
                print()
                # Execute the player's command
                character_moved_room = self.execute_command(command)
                if game_over:
                    break
                
    #removes the character when it dies
    def remove_character(self):
        current_room["character"] = None
    
    #checks if the player has interacted with the character before     
    def check_interacted(self):
        if current_room["character"]["defending_body_part"] is None:
            return True
        else:
            return False

    def has_chucky(self):
        for item in inventory:
            if item["id"] == "doll":
                return True
        return False

    def kill_chucky(self):
        if current_room["name"] == "Living Room":
            self.typewriter_effect("You drop Chucky into the fireplace, he screams as he melts on the fire, and with it any risk to you is diminished.")
            for item in inventory:
                if item["id"] == "doll":
                    inventory.remove(item)
        else:
            self.typewriter_effect("You cannot drop Chucky, the only way to get rid of him is to drop him in the living room fireplace.")

    def check_chucky(self):
        if not self.has_chucky():
            return
        global health
        health -= 10
        self.typewriter_effect("""Oh no! It seems that doll is not what it appears, you have Chucky! He is now going to follow you everywhere you go, taking your health (-10)
    unless he is destroyed. Drop him in the fireplace (Living Room) to kill him.""")
        self.__player.health_check()

    def menu(self, exits, room_items, inv_items):
        """This function, given a dictionary of possible exits from a room, and a list
        of items found in the room and carried by the player, prints the menu of
        actions using print_menu() function. It then prompts the player to type an
        action. The players's input is normalised using the normalise_input()
        function before being returned.

        """

        # Display menu
        self.print_menu(exits, room_items, inv_items)

        # Read player's input
        user_input = input("> ")

        # Normalise the input
        normalised_user_input = normalise_input(user_input)

        #returns the normalised input
        return normalised_user_input

    def move(self, exits, direction):
        # Next room to go to
        return rooms[exits[direction]]
    
    

        return self.__health
    
# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    characters = []
    inventory = [item_baseball_bat, item_water_bottle]
    player = Player(input("What would you like to be called?: ", "Entrance Hall", 100, 35, inventory))
    map = rooms
    main_game = Game(characters, player, map)
    main_game.main()
    

