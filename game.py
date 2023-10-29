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
    def __init__(self, characters, player, map, parser, text_art):
        self.__game_over = False
        self.__create_allowed = False
        self.__needed_for_victory = [item_left_leg, item_right_leg , item_left_arm , item_right_arm , item_head , item_torso]
        self.__characters = characters
        self.__player = player
        self.__map = map
        self.__parser = parser
        self.__text_art = text_art
    
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

    def list_of_item_ids(self, items):
        """This function returns a list of item ids, from a list of items given"""
        list_of_items = []
        for item in items:
            list_of_items.append(item.get_id())
        return list_of_items
    
    def list_of_item_names(self, items):
        """This function returns a list of item names, from a list of items given"""
        list_of_items = []
        for item in items:
            list_of_items.append(item.get_name())
        return list_of_items
        
    def print_room(self, room):
        """Prints out all information about the room you're currently ins"""
        # Prints out the name of the room in full capitals and description with a blank line after each
        self.typewriter_effect(("\n" + room.get_name().upper() + "\n"))
        self.typewriter_effect((room.get_description() + "\n"))
        
        # Prints items in the room
        print()
        self.__player.get_current_room().print_room_items()
      
    def print_commands(self):
        """Prints out player inventory and all available actions the player can take in a given room"""
        print()
        self.print_directions()
        print()
        self.__player.print_weight()
        self.__player.print_health()
        print()
        print("INSPECT to view an item's description.")
        print("DROP to drop an item.")
        print("TAKE to take an item.")
        
        if self.__create_allowed:
            print()
            print("CREATE MONSTER to build your monster.")
        if self.__player.has_chucky() and self.__player.get_current_room().get_name() == "Living Room":
            print()
            print("DROP DOLL to cast Chucky into the fireplace.")
        if self.__player.has_pizza():
            print()
            print("EAT PIZZA to eat some pizza and gain some health.")
        
        print()
        if self.__player.get_current_room().get_character() is not None:
            print("TALK TO", self.__player.get_current_room().get_character().get_name())
        
        print("INVENTORY:")
        for item in self.__player.get_inventory():
            print("    " + str(item.get_id().title()))       
               
    def print_directions(self):
        exits = self.__player.get_current_room().get_exits()
        for direction in exits:
            print("GO " + direction.upper() + " to " + exits[direction] + ".")
        
    def take_command(self):
        print()
        print("---------------------------------------------------------------")
        print()

        self.print_commands()
        
        # Read player's input
        user_input = input("> ")
        # Normalise the input
        normalised_user_input = self.__parser.normalise_input(user_input)
        #returns the normalised input
        return normalised_user_input
    
    def move(self, exits, direction):
        # Next room to go to
        return self.__map[exits[direction]]
    
    def is_valid_exit(self, exits, chosen_exit):
        """Checks if an exit exists in a given direction"""
        #returns true if the chosen direction exits a rooms exits if not return false
        return chosen_exit in exits

    def execute_go(self, direction):
        """Move the player into a new room based on the players input"""
        # Checks if the exit exists using is valid exit, then if true updates current room using the move command, if false prints no exits
        if self.is_valid_exit(self.__player.get_current_room().get_exits(), direction):
            self.__player.set_current_room(self.move(self.__player.get_current_room().get_exits() ,direction))
        else:
            print("No exits" , direction, ".")

    def execute_take(self, item_id):
        """This function takes an item_id as an argument and moves this item from the
        list of items in the current room to the player's inventory. However, if
        there is no such item in the room, this function prints
        "You cannot take that."
        """

        for item in self.__player.get_current_room().get_items():
            #checks if the item given in the command matches the current item in the list
            if item_id == item.get_id():
                if self.__player.weight_check(item):
                    #if weight doesn't exceed the limit the item is added to the player inventory and removed from the room
                    self.__player.add_to_inventory(item)
                    self.__player.get_current_room().remove_item(item)
                    #returns to break search loop to prevent an error
                    return 
            
    def execute_drop(self, item_id):
        """This function takes an item_id as an argument and moves this item from the
        player's inventory to list of items in the current room. However, if there is
        no such item in the inventory, this function prints "You cannot drop that."
        """
        #loops through the list for every item in it
        for item in inventory:
            #if the item entered in the command is in the players inventory add it to the room and remove from inventory
            if item_id == item.get_id():
                if item_id == "doll":
                    self.kill_chucky()
                    return
                self.__player.get_current_room().add_item(item)
                self.__player.remove_from_inventory(item)
                #return to leave the loop
                return
        print("You cannot drop that.")

    def execute_inspect(self, item_id):
        """Prints the description of an item"""
        #loops through the list for every item in it
        for item in self.__player.get_inventory():
            #if the item entered in the command is in the players inventory add it to the room and remove from inventory
            if item_id == item.get_id():
                self.typewriter_effect(item.get_description() + "\n")
                return

    def execute_combat(self, weapon, foe):
        """Function to run combat using the charater and chosen weapon as input"""
        #tell the compiler to treat health as a global to prevent global errors
        #Loops through the combat list of a characer checking for the selected weapon
        health = self.__player.get_health()
        for option in foe.get_combat():
            
            if option[0] == weapon:
                #If the Weapon is found in the combat list deals damage based on the health value in the tuple
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
                    
                self.__player.set_health(health)
                self.__game_over = self.__player.health_check()
                return

        #If the chosen weapon is not found combat is considered poor and greater damage is taken
        health -= 30
        print("A poor performance indeed. You have lost 30 health.")
        self.__player.set_health(health)
        self.__game_over = self.__player.health_check()

    def execute_command(self, command):
        """This function takes a command (a list of words as returned by
        normalise_input) and, depending on the type of action (the first word of
        the command: "go", "take", or "drop"), executes either execute_go,
        execute_take, or execute_drop, supplying the second word as the argument.

        """
        #if nothing is input simply return and do nothing
        if 0 == len(command):
            return

        if command[0] == "go":
            if len(command) > 1:
                self.execute_go(command[1])
                #Returns true only if the character moves rooms (only needs to see the description if they've just moved room)
                return True
            else:
                print("Go where?")
                return False

        elif command[0] == "take":
            if len(command) > 1:
                self.execute_take(' '.join(command[1:]))
                return False
            else:
                print("Take what?")
                return False

        elif command[0] == "drop":
            if len(command) > 1:
                self.execute_drop(' '.join(command[1:]))
                return False
            else:
                print("Drop what?")
                return False

        elif command[0] == "talk":
            if len(command) > 1:
                #print text art for current character
                self.display_character(self.__player.get_current_room().get_character().get_image())
                self.execute_dialogue(self.__player.get_current_room().get_character().get_dialogue())
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
                if self.__create_allowed == True:
                    if len(command) > 1:
                        print("Congratulations, you win!")
                        self.typewriter_effect("Now get away while you still can...")
                        #display frankenstein image
                        print(self.__text_art["frankenstein"])
                        self.__game_over = True
                    else:
                        print("Create what?")
                else:
                    print("Too fast there, get the monster parts first.")

        elif command[0] == "eat":
                if item_pizza in self.__player.get_inventory():
                    if len(command) > 1:
                        self.typewriter_effect("mmmmmm tasty pizza.")
                        health = self.__player.get_health()
                        health += (random.randrange(0 , 10) * 10)
                        self.__player.remove_from_inventory(item_pizza)
                        self.__player.set_health(health)
                    else:
                        print("Eat what?")
                else:
                    print("No pizza to eat :(.")

        #If the first word entered doesn't match any command tell user
        else:
            print("This makes no sense.")

    def execute_dialogue(self, dialogue):
        """Take the dialogue of the character and print it out in an iterable list, sometimes taking an input from the character"""
        #dialogue dictionary from character
        if self.check_interacted() and (dialogue.get_method() == "talk" or dialogue.get_method() == "deal"):
            self.execute_talk(dialogue.get_speech()["repeat dialogue"])
            return
                
        #if there are multiple options, to fight or talk, let the player pick
        if dialogue.get_multiple_options():
            #user interacts with character based on their base dialogue, however their responses are not linked to user input
            for sentence in dialogue.get_speech()["base dialogue"]:
                self.typewriter_effect(sentence)
                print()
            normalised_input = ''
            while normalised_input != 'talk' and normalised_input != 'fight':
                self.typewriter_effect("TALK or FIGHT:")
                print()
                user_input = input("> ")
                normalised_input = ''.join(self.__parser.normalise_input(user_input))
                
            if normalised_input == 'talk':
                #print the sentences in character interaction
                self.execute_talk(dialogue.get_speech()["dialogue one"])
                #give the player the limb
                self.give_limb()
                    
            elif normalised_input == 'fight':
                #provide the fighting text if the player chooses to fight
                self.execute_fight(dialogue.get_speech()["dialogue two"])
        
        elif dialogue.get_method() == "fight":
            self.execute_fight(dialogue.get_speech()["base dialogue"])

        elif dialogue.get_method() == "talk":
            #print the sentences in character interaction
            self.execute_talk(dialogue.get_speech()["base dialogue"])
            #give the player the limb
            self.give_limb()
            
        elif dialogue.get_method() == "deal":
            self.execute_deal(dialogue)
            
    def execute_fight(self, fight_dialogue):
        """Executes a player fighting one of the characters, taking a list of dialogue to print to the player"""
        for sentence in fight_dialogue:
            self.typewriter_effect(sentence)
            #pause between each sentence for better understanding
            sleep(0.5)
            print()
            
        print()
        print("CHOOSE YOUR WEAPON")
        print("Remember, you can always run.")
        #Print inventory items
        if len(self.__player.get_inventory()) != 0:
            print("You have",", ".join(self.list_of_item_ids(self.__player.get_inventory())), "available.")
        else:
            print("You have no items in your inventory to fight with.")
        normalised_input = ''
        #allow the weapon to be shout for pennywise, but otherwise it has to be in the inventory
        while normalised_input not in self.list_of_item_ids(self.__player.get_inventory()) and normalised_input != 'shout' and normalised_input != "run":
            weapon = input("> ")
            normalised_input = ' '.join(self.__parser.normalise_input(weapon))
        if normalised_input == "run":
            return
        self.execute_combat(normalised_input, self.__player.get_current_room().get_character()) 

    def execute_talk(self, talk_dialogue):
        """Executes a player talking to one of the characters, taking a list of dialogue to print to the player"""
        for sentence in talk_dialogue:
            #provide the talking text if the player chooses talk
            self.typewriter_effect(sentence)
            #pause between each sentence for better understanding
            sleep(0.5)
            print()
        print()

    def execute_deal(self, dialogue):
        #print the sentences in character interaction
            for sentence in dialogue.get_speech()["base dialogue"]:
                self.typewriter_effect(sentence)
                sleep(0.5)
                print()
            #allow the player to either choose to give the gift or to leave the interaction
            print("Gift or Leave")
            normalised_input = ''
            while normalised_input != "gift" and normalised_input != "leave":
                user_input = input('> ')
                normalised_input = ' '.join(self.__parser.normalise_input(user_input))
            #if the user gifts, they can choose which item from their inventory to give, otherwise leaving results in ending the interaction
            if normalised_input == "gift":
                print("CHOOSE YOUR GIFT")
                if len(self.__player.get_inventory()) != 0:
                    print("You have",", ".join(self.list_of_item_ids(self.__player.get_inventory())), "available.")
                else:
                    print("You have no items in your inventory to fight with.")
                normalised_gift = ''
                while not normalised_gift in self.list_of_item_ids(self.__player.get_inventory()):
                    gift = input('> ')
                    normalised_gift = ' '.join(self.__parser.normalise_input(gift))
                #if the gift is correct, give the limb to the player
                if normalised_gift == dialogue.get_speech()["gift"]:
                    for sentence in dialogue.get_speech()["successful dialogue"]:
                        self.typewriter_effect(sentence)
                        sleep(0.5)
                        print()
                    for item in self.__player.get_inventory():
                        if item.get_id() == normalised_gift:
                            self.__player.remove_from_inventory(item)
                    self.give_limb()
                else:
                    for sentence in dialogue.get_speech()["unsuccessful dialogue"]:
                        self.typewriter_effect(sentence)
                        sleep(0.5)
                        print()

    def give_limb(self):
        """Gives the player the limb currently in the room after a successful interaction"""
        if self.__player.weight_check(self.__player.get_current_room().get_character().get_role()):
            inventory.append(self.__player.get_current_room().get_character().get_role())
            print()
            print("You have the", str(self.__player.get_current_room().get_character().get_role().get_id()) + ".")
            self.__player.get_current_room().get_character().remove_role()
        else:
            self.__player.add_item(self.__player.get_current_room().get_character().get_role())
            print()
            print("The", str(self.__player.get_current_room().get_character().get_role().get_id()) , "is too heavy to take, so it is now available to pick up from the room.")
            self.__player.get_current_room().get_character().remove_role()
    
    def victory_check(self):
        """Checks to see if all the limbs are in the lab and the needle and thread is in the players inventory, which is required for the player to build the monster"""
        # Checks limbs
        victory_count = 0
        for item in self.__map["Lab"].get_items():
            if item in self.__needed_for_victory:
                victory_count += 1
                
        # Checks needle and thread
        for item in self.__player.get_inventory():
            if item.get_id() == "needle and thread":
                needle_and_thread = True
                
        if victory_count == 6 and needle_and_thread:
            return True
        else:
            return False
                
        # This is the entry point of our program
                
    def remove_character(self):
        """Removes the character when it dies"""
        self.__player.get_current_room().remove_character()
         
    def check_interacted(self):
        """Checks if the player has interacted with the character before"""
        if self.__player.get_current_room().get_character().get_role() is None:
            return True
        else:
            return False

    def kill_chucky(self):
        if self.__player.get_current_room().get_name() == "Living Room":
            self.typewriter_effect("You drop Chucky into the fireplace, he screams as he melts on the fire, and with it any risk to you is diminished.")
            for item in self.__player.get_inventory():
                if item.get_id() == "doll":
                    self.__player.remove_from_inventory(item)
        else:
            self.typewriter_effect("You cannot drop Chucky, the only way to get rid of him is to drop him in the living room fireplace.")

    def check_chucky(self):
        if not self.__player.has_chucky():
            return
        self.__player.set_health(self.__player.get_health() - 10)
        self.typewriter_effect("""Oh no! It seems that doll is not what it appears, you have Chucky! He is now going to follow you everywhere you go, taking your health (-10)
unless he is destroyed. Drop him in the fireplace (Living Room) to kill him.""")
        print()
        self.__game_over = self.__player.health_check()
          
    def jumpscare(self):
        num = random.randint(0,4)
        array = []
        for key in text_art:
            array.append(text_art[key])
        print(array[num])
        print()
        print("BOO!!!")
            
    def display_character(self, character):
        print(character)
            
    def main(self):
        # Tell them how to skip
        print(self.__text_art["haunted_house"])    
        print()
        print("Press S to skip.")
        self.typewriter_effect("""Welcome to the haunted house, each room before you holds ancient secrets for you to unlock. Join us on an adventurous 
journey where you will meet suspicious individuals, some of which you might recognise from your favourite halloween 
productions. Along the way you will be able to talk to characters and battle some of the most famous horror villains. You
are playing as Victor Frankenstein and your goal is to collect each limb of your monster in order to overcome the haunted 
house and build the monster. """)
        print()
        
        # Main game loop
        while not self.__game_over:
            # Display game status (room description, inventory etc.)
            self.print_room(self.__player.get_current_room())
            
            #chucky affects health, so game-over has to be checked
            self.check_chucky()
            if self.__game_over:
                break
            
            #jumpscare 10% of the time the player moves srooms
            '''num = random.randint(0, 100)
            if num % 10 == 0:
                self.jumpscare()
                sleep(1)'''

            character_moved_room = False
            while not character_moved_room:
                self.__create_allowed = self.victory_check()
                # Show the menu with possible actions and ask the player
                
                command = self.take_command()
                print()
                # Execute the player's command
                character_moved_room = self.execute_command(command)
                if self.__game_over:
                    break
                
# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    characters = []
    inventory = [item_baseball_bat, item_water_bottle]
    text_art = text_art_other
    game_parser = GameParser()
    map = rooms
    player = Player("Victor Frankenstein", map["Entrance"], 100, 35, inventory)
    main_game = Game(characters, player, map, game_parser, text_art)
    main_game.main()
    

