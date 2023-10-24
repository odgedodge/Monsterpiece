from items import *
from map import rooms

weight_limit = 35.0
health = 100

inventory = [item_baseball_bat, item_water_bottle]

victory_check = [item_left_leg, item_right_leg , item_left_arm , item_right_arm , item_head , item_torso]

create_allowed = False

# Start game at the reception
current_room = rooms["Entrance"]
