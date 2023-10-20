from items import *
from dialogue import *

character_dracula = {
    "name": "Dracula",
    
    "combat": [("holy water", 0) , ("spear" , 15)],
    
    "defending_body_part": item_left_arm,
    
    "dialogue": dialogue_dracula
}

character_freddy = {
    "name": "Freddy fazbear",
    
    "combat": [("baseball bat" , 0) , ("water bottle" , 15)],
    
    "defending_body_part": item_right_leg,
    
    "dialogue": dialogue_freddy
}

character_grim = {
    "name": "The Grim Reaper",
    
    "combat": None,
    
    "defending_body_part": item_torso,
    
    "dialogue": dialogue_grim
}

character_slenderman = {
    "name": "Slenderman",
    
    "combat": [("eight pages" , 0) , ("instruction book" , 15)],
    
    "defending_body_part": item_head,
    
    "dialogue": dialogue_slenderman
}

character_pennywise = {
    "name": "Pennywise",
    
    "combat": [("shout", 0)],
    
    "defending_body_part": item_left_leg,
    
    "dialogue": dialogue_pennywise
}
