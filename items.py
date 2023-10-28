class Item:
    def __init__(self, weight, name, id, description):
        self.__weight = weight
        self.__name = name
        self.__id = id
        self.__description = description
        
    def get_weight(self):
        return self.__weight
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_description(self):
        return self.__description

item_instruction_book = Item("instruction book", "the instruction book", """This book has instructions for how to assemble your monster. You will need to collect the following body parts
to your lab, as well as the correct materials.You need to collect a right arm, a left arm, a left leg, a right leg, as well as
the torso and head of your monster.You need to gain a needle and thread to also properly assemble the monster. Don't forget 
about the foes on your way who also covet the body parts you seek, and good luck.""", 0.7)

item_needle_and_thread= Item("needle and thread", "a needle and thread", "The needle and thread needed to assemble your monster.", .05)

item_rock = Item("rock", "a rock", """I have an inexplicable attachment to a comically funny-looking rock that defies all rational explanation. 
Its irregular shape, adorned with whimsical patterns, seems to evoke a perpetual grin on my face. I picked it up on a whim, 
and from that moment, it's as though the universe conspired to forge an inseverable bond between us. It's not particularly 
rare or valuable, but the sheer quirkiness of this geological oddity has ensnared my fascination. I've tried to set it down,
but it exerts a magnetic pull on my hand, tugging at my curiosity and igniting my imagination with endless tales of its origin.
""", 0.3)

item_baseball_bat = Item("baseball bat", "a baseball bat", "A baseball bat to defend yourself if necessary.", 1)

item_holy_water = Item("holy water", "holy water", "Holy Water", 0.3)

item_saw = Item("saw", "a saw", "A saw", 0.8)

item_hammer = Item("hammer", "a hammer", "A hammer", 0.9)

item_spear = Item("spear", "a spear", "A spear", 1)

item_eight_pages = Item("eight pages", "the eight pages", "The eight pages", 0.01)

item_soul_jar = Item("soul jar", "a soul jar", "A soul jar", 0.3)

item_water_bottle = Item("water bottle", "a water bottle", "Your water bottle", 0.6)

item_chucky = Item("doll", "a doll", "a doll", 0.6)

item_pizza = Item("pizza", "a slice of pizza", "A slice of freddy fazzbears pizza, it smells amazing", .075)

item_left_leg = Item("left leg", "the monster's left leg", "The left leg", 18)

item_right_leg = Item("right leg", "the monster's right leg", "The right leg", 18)

item_left_arm = Item("left arm", "the monster's left arm", "The left arm", 5)

item_right_arm = Item("right arm", "the monster's right arm", "The right arm", 5)

item_head = Item("head", "the monster's head", "The head", 7)

item_torso = Item("torso", "the monster's torso", "The torso", 35)

