from items import *
from dialogue import *

character_dracula = {
    "name": "dracula",
    
    "combat": ["holy water", 0 , "spear" , 15],
    
    "defending_body_part": item_left_arm,
    
    "dialogue": dialogue_dracula
}

character_freddy = {
    "name": "freddy fazbear",
    
    "combat": ["baseball bat" , 0 , "water bottle" , 15],
    
    "defending_body_part": item_right_leg,
    
    "dialogue": dialogue_freddy
}

character_grim = {
    "name": "the grim reaper",
    
    "combat": None,
    
    "defending_body_part": item_torso,
    
    "dialogue": dialogue_grim
}

character_slenderman = {
    "name": "slenderman",
    
    "combat": ["eight pages" , 0 , "instruction book" , 15],
    
    "defending_body_part": item_head,
    
    "dialogue": None
}

character_pennywise = {
    "name": "pennywise",
    
    "combat": "talk",
    
    "defending_body_part": item_left_leg,
    
    "dialogue": dialogue_pennywise
}
