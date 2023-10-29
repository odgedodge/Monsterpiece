class Player:
    def __init__(self, name, starting_room, health, weight_limit, inventory):
        self.name = name
        self.__weight_limit = weight_limit
        self.__inventory = inventory
        self.__weight = self.calculate_weight()
        self.__current_room = starting_room
        self.__health = health
        
    def weight_check(self, item):   
        #checks that the weight won't go over the weight limit
        if self.__weight + item.get_weight() > self.__weight_limit:
            #If weight exceeds limit prevents the item from being added to the player inventory
            print("You cannot take", item.get_name(), ",it's too heavy for you. Drop a heavy item to pick this up.")
            return False
        else:
            return True
        
    def calculate_weight(self):
        weight = 0
        for item in self.__inventory:
            weight += item.get_weight()
        return weight
    
    def set_weight(self, value):
        self.__weight = value
        
    def get_weight_limit(self):
        return self.__weight_limit
        
    def print_weight(self):
        print("You are carrying" , str(self.__weight) + "/" + str(self.__weight_limit) + "kg")
        
    def health_check(self):
        if self.__health > 0:
            return False
        else:
            self.game_over = True
            print("You collapse, health depleted, as you die you mourn the loss of your ambition, and your legacy.")
            return True
    
    def print_health(self):
        if self.__health > 80:
            print("You feel exceptionally healthy (" + str(self.__health) + ").")
        elif self.__health > 60:
            print("You feel healthy (" + str(self.__health) + ").")
        elif self.__health > 40:
            print("You're starting to feel week (" + str(self.__health) + ").")
        elif self.__health > 20:
            print("You're fading (" + str(self.__health) + ")...")
        elif self.__health > 0:    
            print("You have one foot in the grave (" + str(self.__health) + ")...")   
    
    def print_inventory_items(self, items):
        # Get list of item names
        item_names = self.list_of_items(items)
        
        if len(item_names) == '':
            print("You have nothing in your inventory.")
            return
        
        print("You have", item_names + ".")
        self.print_weight()
        print()

    def get_health(self):
        return self.__health
    
    def set_health(self, new_value):
        self.__health = new_value
    
    def get_current_room(self):
        return self.__current_room 

    def set_current_room(self, new_room):
        self.__current_room = new_room
    
    def get_inventory(self):
        return self.__inventory
   
    def add_to_inventory(self, new_item):
        self.__inventory.append(new_item)
        
    def remove_from_inventory(self, removing_item):
        self.__inventory.remove(removing_item)
        
    def has_pizza(self):
        for item in self.__inventory:
            if item.get_id() == "pizza":
                return True
        return False
    
    def has_chucky(self):
        for item in self.__inventory:
            if item.get_id() == "doll":
                return True
        return False