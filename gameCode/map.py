from items import *
from characters import *

room_lab = {
    "name": "Lab",

    "description":
    """In the dimly lit laboratory, an eerie green glow emanates from bubbling test tubes and flickering neon lights. The air is thick with the scent of chemicals, and the room 
is cluttered with arcane scientific instruments, rusty gears, and arcane tomes. Creeping shadows dance on the walls, casting unsettling silhouettes of towering, stitched-together
apparatuses and shelves filled with specimen jars containing mysterious, pulsating organs. A low, ominous hum fills the air as electricity crackles around an imposing 
operating table, surrounded by leather straps and stained tools. Cobwebs cling to the corners, and the faint echo of distant, haunting whispers adds to the chilling atmosphere, 
making every creak of the floorboards and drip of unknown substances a source of spine-tingling dread. """,

    "exits": {"south": "Basement"},

    "items": [item_saw, item_hammer, item_soul_jar],
    
    "character": None
}

room_attic = {
    "name": "Attic",

    "description":
    """The attic stands as a foreboding chamber, heavy with the weight of forgotten experiments and the echoes of mad ambition. The room is cloaked in an eerie half-light, with 
the weak glow of flickering candles barely penetrating the shadows that dance along the cracked, wooden floor. You see an old disused doll amoungst cobwebs that hang like veils, draping the rooms corners and ancient, 
forgotten artefacts. A weathered laboratory table occupies the centre, adorned with rusty instruments, vials of mysterious substances, and decaying parchments bearing Victor 
Frankensteins frantic scrawl. Broken, disused machinery looms in the darkness, its once-promising potential now a testament to the hubris of scientific curiosity.""",

    "exits":  {"west": "Bedroom"},

    "items": [item_chucky],
    
    "character": None
}

room_bedroom = {
    "name": "Master bedroom",

    "description":
    """The bedroom exudes an aura of lingering malevolence, trapped within its timeworn walls. Moonlight seeps through moth-eaten curtains, casting feeble rays that barely 
illuminate the room, leaving most of it in unsettling darkness, stood in the corner of the room you spot Dracula. The bed, once grand, now stands as a skeletal frame draped in tattered, cobweb-covered fabric. The air is thick 
with dust and the scent of decay, and the floorboards groan underfoot as if bearing the weight of unseen spectres. Faded wallpaper peels away, revealing glimpses of a long-
forgotten floral pattern, and the windows rattle softly in the chill wind, creating an eerie symphony of the forsaken. """,

    "exits": {"down": "Entrance", "east": "Attic"},

    "items": [item_needle_and_thread],
    
    "character": character_dracula
}

room_kitchen = {
    "name": "Kitchen",

    "description": 
    """You enter the kitchen, its once-vibrant colour now faded and peeling. The air is thick with an eerie stillness, broken only by occasional creaks from the old floorboards. 
Rusty knives and tarnished utensils hang from the walls, casting unsettling shadows in the dim light. The ancient stove, covered in soot, looms in the corner like a sinister 
sentinel. The cabinets, their doors warped with age, let out faint whispers as if concealing long-forgotten secrets. A chilling breeze sweeps through, rattling the windows, 
while ghostly apparitions of cooks long past seem to move just out of sight. A sense of dread lingers in the air, making your every step uneasy as you explore the haunted 
kitchen. """,

    "exits": {"north": "Entrance", "east": "Garden", "west": "Basement"},

    "items": [item_holy_water],
    
    "character": None
}

room_theatre = {
    "name": "Theatre",

    "description":
    """ You step into the old theatre, a grand space frozen in time. The scent of aged velvet and polished wood mingles with a faint aroma of distant perfume. Dust dances in the dim 
spotlight that pierces the darkness, casting eerie shapes upon the crimson velvet seats. The stage, adorned with faded curtains and ornate carvings, seems to hold its breath, as 
if anticipating a performance long overdue, where Freddy Fazbear awaits . The air is heavy with a sense of anticipation, and the echoes of long-forgotten applause linger in the rafters. Rows of empty seats 
stretch into the shadows, their occupants now spectral memories. A grand, cobweb-covered chandelier hangs precariously above, its crystals refracting ghostly glimmers. Tattered 
playbills litter the floor, hinting at performances from an era long past.""",

    "exits": {"east": "Entrance"},

    "items": [],
    
    "character": character_freddy
}

room_entrance = {
    "name": "Entrance Hall",

    "description":
    """You find yourself in the vast entrance room. Dim candle light flickers against the peeling wallpaper, casting unsettling shadows that dance with the wind's whispers. The air is thick 
with a musty scent, and the floorboards groan beneath your weight, as if sharing the secrets of countless visitors before you. A faded, grand chandelier hangs precariously overhead, 
swaying gently, its crystals refracting ghostly glimmers. To your left, an ancient, cracked mirror reflects distorted images of the room, creating an unsettling feeling of being watched. 
Cobwebs cling to the corners, and a chilling breeze sweeps through the room, carrying faint, ghostly whispers that send shivers down your spine. The atmosphere is heavy with anticipation, 
and the silence is broken only by distant, haunting echoes, setting the stage for the mysteries that lie deeper within the haunted abode.""",

    "exits": {"north": "Library", "east": "Living Room", "south": "Kitchen", "west": "Theatre", "up": "Bedroom"},

    "items": [],
    
    "character": None
}

room_basement = {
    "name": "Basement",

    "description":
    """The basement lies beneath the creaking floorboards, a realm of chilling darkness and unspeakable secrets. Descending the narrow, winding staircase, you find yourself enveloped in an 
oppressive, damp atmosphere, where the scent of mildew mingles with the earthy aroma of decay. Dim, flickering candles barely illuminate the vast expanse, casting long, menacing shadows 
that seem to dance with a life of their own. Pennywise is waiting for you, stood against the stone walls, damp and slick to the touch, bear the marks of age and neglect, adorned with cryptic symbols and faded graffiti from bygone 
eras. The floor is cold and uneven, scattered with forgotten remnants of the past rusted tools, discarded furniture, and shattered relics, all shrouded in a veil of dust. """,

    "exits": {"east": "Kitchen", "north": "Lab"},

    "items": [],
    
    "character": character_pennywise
}

room_garden = {
    "name": "Garden",

    "description":
    """A haunting garden unfolds before your eyes. The air is thick with an unsettling stillness, and the moonlight casts elongated shadows across gnarled trees and overgrown vines. Jagged 
tombstones jut from the earth like broken teeth, bearing cryptic inscriptions of forgotten souls. A dense fog shrouds the garden, concealing ancient stone statues that seem to whisper 
secrets of the past. Strange, luminescent flowers glow dimly, casting an otherworldly ambiance, while the distant howl of a wolf sends shivers down your spine. Amidst the macabre beauty, 
you'll find the remnants of forgotten experiments, rusted machinery, and remnants of scientific endeavours, all hinting at the dark secrets that lie within this haunting garden. 
Wandering around on the far side of the garden you spot Slenderman. """,

    "exits": {"west": "Kitchen"},

    "items": [item_rock],
    
    "character": character_slenderman
}

room_living_room = {
    "name": "Living Room",

    "description":
    """You step into the living room, a once-grand space now draped in shadows. Tattered curtains sway gently, revealing slivers of a pale, ghostly moonlight that dance across the faded 
wallpaper. A grand, cobweb-covered chandelier hangs from the ceiling, its crystals dulled by time. Antique furniture, draped in dusty sheets, huddles in the corners like forgotten phantoms. 
A lit fireplace dominates one wall, its hearth blowing  the smell of burning embers through the room. Next to it you see the tall, dark figure of the Grim Reaper.
The floorboards creak beneath your weight as if protesting your intrusion. Unsettling portraits of unknown faces line the walls, their eyes following your every move. A tinge of melancholy 
lingers in the air, as if the room itself mourns its lost elegance. Whispers echo faintly, carried by the breeze that seeps through the cracks, hinting at the presence of unseen entities. 
This living room, frozen in time, holds a haunting aura that sends shivers down your spine. """,

    "exits": {"west": "Entrance"},

    "items": [item_spear],
    
    "character": character_grim
}

room_library = {
    "name": "Library",

    "description":
    """In the library, ancient tomes line towering, dusty shelves that stretch from floor to ceiling. Dim candle light flickers, casting enormous shadows on the leather-bound volumes filled with 
esoteric knowledge. The air is thick with the scent of decaying paper, and the faint rustle of pages turning on their own sends shivers down the spine. Curiosities like anatomical sketches 
and peculiar specimens are displayed in glass cases, their ghostly glow illuminating the room. A ghostly whisper seems to ride the breeze, carrying fragments of forbidden incantations and 
scientific musings. The atmosphere is one of both intellectual curiosity and lingering, unsettling dread, as if the very essence of knowledge in the room is imbued with a dark, pulsating energy. """,

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
