from items import *
from dialogue import *
from text_art import text_art

class Character:
    def __init__(self, name, combat, role, dialogue, image):
        self.__name = name
        self.__combat = combat
        self.__role = role
        self.__dialogue = dialogue
        self.__image = image
        
    def get_name(self):
        return self.__name
    
    def get_combat(self):
        return self.__combat
    
    def get_role(self):
        return self.__role
    
    def get_dialogue(self):
        return self.__dialogue
    
    def get_image(self):
        return self.__image
        
dracula = Character("Dracula", [(item_holy_water.get_id(), 0) , (item_spear.get_id() , 15)], item_left_arm, dracula_interaction, text_art["dracula"])

freddy = Character("Freddy Fazbear", [(item_baseball_bat.get_id() , 0) , (item_water_bottle.get_id() , 15)], item_right_leg, freddy_interaction, text_art["freddy"])

grim = Character("The Grim Reaper", None, item_torso, grim_interaction, text_art["grim"])

slenderman = Character("Slenderman", [(item_eight_pages.get_id() , 0) , (item_instruction_book.get_id() , 15)], item_head, slenderman_interaction, text_art["slenderman"])

pennywise = Character("Pennywise", [("shout", 0), (item_spear.get_id(), 15)], item_left_leg, pennywise_interaction, text_art["pennywise"])
