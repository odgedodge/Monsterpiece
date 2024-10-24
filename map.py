from items import *
from characters import *

class Room:
    def __init__(self, name, description, exits, items, character):
        self.__name = name
        self.__description = description
        self.__exits = exits
        self.__items = items
        self.__character = character
        
    def print_room_items(self):
        """If the string from list isn't blank will print out each item in the room."""
        if len(self.__items) != 0:
            item_names = []
            for item in self.__items:
                item_names.append(item.get_name())
            print("There is" , ', '.join(item_names), "here." + "\n")    
            
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_exits(self):
        return self.__exits
    
    def get_items(self):
        return self.__items
    
    def get_character(self):
        return self.__character
    
    def remove_item(self, removing_item):
        self.__items.remove(removing_item)
        
    def add_item(self, new_item):
        self.__items.append(new_item)
        
    def remove_character(self):
        self.__character = None

lab_description = """In the dimly lit laboratory, an eerie green glow emanates from bubbling test tubes and fluorescent lights. The air is thick 
with the scent of chemicals, and the room is cluttered with arcane scientific instruments and rusty gears. Creeping shadows 
dance on the walls, casting unsettling silhouettes of towering, taped-together apparatuses, shelves littered with jars 
containing mysterious organs. One of said jars holds a floating blue cloud, moving like with a mind of its own - a soul. A low, 
ominous hum fills the air as electricity crackles around an imposing operating table, surrounded by leather straps and stained 
tools. Cobwebs cling to the corners, and the faint echo of distant, haunting whispers adds to the chilling atmosphere, a 
dripping sound a source of dread."""

room_lab = Room("Lab", lab_description, {"south": "Basement"}, [item_saw, item_hammer, item_soul_jar], None)

attic_description =  """The attic sits eerily, memories stashed away with nowhere to go. The room is cloaked in a half-light, with the weak glow of 
flickering light-bulbs barely affecting the shadows that dance along the cracked, wooden floor. You see an old disused doll 
amongst cobwebs that hang like veils, draping the rooms corners. Creaking rocking chairs, battered old shelves and rotting 
decorations show a history of this house being a home, before every ounce of hope was pushed out."""

room_attic = Room("Attic", attic_description, {"west": "Bedroom"}, [item_chucky, item_right_arm], None)

bedroom_description = """The bedroom exudes an aura of lingering malevolence, trapped within its timeworn walls. Moonlight seeps through moth-eaten
curtains, casting feeble rays that barely illuminate the room, leaving most of it in unsettling darkness, stood in the corner
of the room you spot Dracula. He is simply drinking what only looks like wine, seemingly lost in thought. The bed, once grand,
now stands as a skeletal frame draped in tattered, cobweb-covered fabric. The air is thick with dust and the scent of decay, 
and the floorboards groan underfoot as you enter the room, a testament to the lack of occupancy. Faded wallpaper peels away, 
revealing glimpses of a long forgotten floral pattern, and the windows rattle softly in the frosty wind."""

room_bedroom = Room("Master Bedroom", bedroom_description, {"down": "Entrance", "east": "Attic"}, [item_needle_and_thread], dracula)

kitchen_drescription = """You enter the kitchen, its once-vibrant yellow walls now faded and peeling. The air is thick with an eerie stillness, 
broken only by the sound of rustling trees from the garden outside. Rusting knives and tarnished utensils hang from the walls,
casting unsettling shadows in the dim light. The ancient stove, covered in soot, looms in the corner, echoing the memories of
life that once existed here. The cabinets, their doors warped with age, let out faint whispers as if concealing long-
forgotten secrets. A chilling breeze sweeps through, rattling the windows. A sense of dread lingers in the air, making your 
every step uneasy as you explore the space."""

room_kitchen = Room("Kitchen", kitchen_drescription, {"north": "Entrance", "east": "Garden", "west": "Basement"}, [item_holy_water], None)

theatre_description = """You step into the old theatre, a grand space frozen in time. The scent of aged velvet and polished wood mingles with a 
faint aroma of distant perfume. Dust dances in the dim spotlight that pierces the darkness, casting eerie shapes upon the 
crimson velvet seats. The stage, adorned with faded curtains and ornate carvings holds memories of performances past, where
Freddy Fazbear awaits. The air is heavy with a sense of anticipation, and the echoes of long-forgotten applause linger. A 
grand, cobweb-covered chandelier hangs precariously above, its crystals refracting ghostly glimmers."""

room_theatre = Room("Theatre", theatre_description, {"east": "Entrance"}, [item_pizza], freddy)

entrance_description = """You find yourself in the vast entrance room. Dim candle light flickers against the peeling wallpaper, casting unsettling
shadows that dance with the wind's whispers. The air is thick with a musty scent, and the floorboards groan beneath your 
weight, as if sharing the secrets of countless visitors before you. A faded, grand chandelier hangs precariously overhead,
swaying gently, its crystals refracting ghostly glimmers. To your left, an ancient, cracked mirror reflects distorted images
of the room, creating an unsettling feeling of being watched. Cobwebs cover the space, with every object becoming home to 
only those who can bare the atmosphere, heavy with anticipation. The silence is broken only by distant, haunting echoes, 
setting the stage for the mysteries that lie deeper within the building."""

room_entrance = Room("Entrance Hall", entrance_description, {"north": "Library", "east": "Living Room", "south": "Kitchen", "west": "Theatre", "up": "Bedroom"}, [], None)

basement_description = """The basement lies beneath the creaking floorboards, a realm of chilling darkness and unspeakable secrets. Descending 
the narrow staircase, you find yourself enveloped in an oppressive, damp atmosphere, where the scent of mildew mingles 
with the earthy aroma of decay. The exposed brick walls hold no warmth, simply making the space feel colder, the lone 
lightbulb barely allowing more than a few metres to be visible. Pennywise is waiting for you, stood against walls adorned
with cryptic symbols and faded graffiti from bygone eras. The floor is cold and uneven, scattered with discarded furniture
and shattered relics, all covered in a layer of dust. """

room_basement = Room("Basement", basement_description, {"east": "Kitchen", "north": "Lab"}, [], pennywise)

garden_description = """The garden seems endless as you step outside, trees spanning the fence with weeds covering stone of the path. Ivy 
crawls over the side of the house, covering the ypstairs windows and extending to the chimney. The only light is that which
leaks from the kitchen  The air is thick with an unsettling stillness, and the moonlight casts elongated shadows across the
ground. Jagged stones jut from the earth like broken teeth, a dense fog shrouding the area. Strange, luminescent flowers 
glow dimly, casting an otherworldly ambiance, while the distant howl of a wolf sends shivers down your spine. Wandering 
around on the far side of the garden you spot a tall, slender figure. """

room_garden = Room("Garden", garden_description, {"west": "Kitchen"}, [item_rock], slenderman)

living_room_description = """You step into the living room, a once-grand space now draped in shadows. Tattered curtains sway gently, revealing 
slivers of a pale, ghostly moonlight that dance across the faded wallpaper. A grand, cobweb-covered chandelier hangs from
the ceiling, its crystals dulled by time. Antique furniture, draped in dusty sheets, huddles in the corners like 
forgotten phantoms. A lit fireplace dominates one wall, its hearth blowing  the smell of burning embers through the room.
Next to it you see the tall, dark figure of the Grim Reaper. The floorboards creak beneath your weight as if protesting 
your intrusion. Unsettling portraits of unknown faces line the walls, their eyes following your every move. A tinge of 
melancholy lingers in the air, as if the room itself mourns its lost elegance."""

room_living_room = Room("Living Room", living_room_description, {"west": "Entrance"}, [item_spear], grim)

library_description = """In the library, ancient tomes line towering, dusty shelves that stretch from floor to ceiling. Dim candle light flickers,
casting enormous shadows on the leather-bound volumes filled with ancient knowledge. The air is thick with the scent of 
decaying paper, and the faint rustle of pages in the wind sends shivers down you spine. A ghostly whisper seems to ride the
breeze, carrying fragments of forbidden incantations and poetic musings. The atmosphere is one of both intellectual curiosity
and lingering, unsettling dread, as if the very essence of knowledge in the room is imbued with a dark energy. """

room_library = Room("Library", library_description, {"south": "Entrance"}, [item_instruction_book, item_eight_pages], None)

rooms = {
    "Lab": room_lab,
    "Entrance": room_entrance,
    "Attic": room_attic,
    "Bedroom": room_bedroom,
    "Kitchen": room_kitchen,
    "Theatre": room_theatre,
    "Basement": room_basement,
    "Garden": room_garden,
    "Living Room": room_living_room,
    "Library": room_library
}
