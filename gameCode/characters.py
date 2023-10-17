from items import *
from dialouge import *

character_dracula = {
    "name": "dracula",
    
    "combat": ["holy water", 0 , "spear" , 15],
    
    "defending_body_part": item_left_arm,
    
    "dialouge": dialouge_dracula
}

character_freddy = {
    "name": "freddy fazbear",
    
    "combat": ["baseball bat" , 0 , "water bottle" , 15],
    
    "defending_body_part": item_right_leg,
    
    "dialouge": dialouge_freddy
}

character_grim = {
    "name": "the grim reaper",
    
    "combat": None,
    
    "defending_body_part": item_torso,
    
    "dialouge": dialouge_grim
}

character_slenderman = {
    "name": "slenderman",
    
    "combat": ["eight pages" , 0 , "instruction book" , 15],
    
    "defending_body_part": item_head,
    
    "dialouge": None
}

character_pennywise = {
    "name": "pennywise",
    
    "combat": "talk",
    
    "defending_body_part": item_left_leg,
    
    "dialouge": dialouge_pennywise
}
