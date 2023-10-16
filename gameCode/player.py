from items import *
from map import rooms

weight_limit = 3.0

inventory = [item_id, item_laptop, item_money]

victory_check = [item_id, item_laptop, item_money, item_biscuits, item_pen, item_handbook]

# Start game at the reception
current_room = rooms["Reception"]
