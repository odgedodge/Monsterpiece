from items import *
from characters import *

room_lab = {
    "name": "Lab",

    "description":
    """ """,

    "exits": {"south": "Basement"},

    "items": [item_saw, item_hammer, item_soul_jar],
    
    "character": None
}

room_attic = {
    "name": "Attic",

    "description":
    """ """,

    "exits":  {"west": "Bedroom"},

    "items": [item_chucky],
    
    "character": None
}

room_bedroom = {
    "name": "Master bedroom",

    "description":
    """ """,

    "exits": {"down": "Entrance", "east": "Attic"},

    "items": [item_needle_and_thread],
    
    "character": character_dracula
}

room_kitchen = {
    "name": "Kitchen",

    "description": 
    """ """,

    "exits": {"north": "Entrance", "east": "Garden", "west": "Basement"},

    "items": [item_holy_water],
    
    "character": None
}

room_theatre = {
    "name": "Theatre",

    "description":
    """ """,

    "exits": {"east": "Entrance"},

    "items": [],
    
    "character": character_freddy
}

room_entrance = {
    "name": "Entrance Hall",

    "description":
    """A grand entrance hall covered with a thick layer of dust and cobwebs""",

    "exits": {"north": "Library", "east": "Living room", "south": "Kitchen", "west": "Theatre", "up": "Bedroom"},

    "items": [],
    
    "character": None
}

room_basement = {
    "name": "Basement",

    "description":
    """ """,

    "exits": {"east": "Kitchen", "north": "Lab"},

    "items": [],
    
    "character": character_pennywise
}

room_garden = {
    "name": "Garden",

    "description":
    """ """,

    "exits": {"west": "Kitchen"},

    "items": [item_rock],
    
    "character": character_slenderman
}

room_living_room = {
    "name": "Living Room",

    "description":
    """ """,

    "exits": {"west": "Entrance"},

    "items": [item_spear],
    
    "character": character_grim
}

room_library = {
    "name": "Library",

    "description":
    """ """,

    "exits": {"south": "Entrance"},

    "items": [item_instruction_book, item_eight_pages],
    
    "character": None
}


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
