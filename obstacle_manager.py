import arcade
import random
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, ENGEL_SPRITES

def is_safe_position(self, x, y, min_distance=100):
    for obstacle in self:
        if (abs(obstacle.center_x - x) < min_distance and 
            abs(obstacle.center_y - y) < min_distance):
            return False
    return True

def get_safe_position(self):
    margin = 50
    y = SCREEN_HEIGHT + 100
    x = random.randint(margin, SCREEN_WIDTH - margin)
    
    while not is_safe_position(self, x, y):
        y += random.randint(100, 200)
    
    return x, y

def create_obstacles(self):
    base_obstacles = 2 
    max_level_bonus = 3 
    level_bonus = min(self.level - 1, max_level_bonus)
    num_obstacles = base_obstacles + level_bonus
    
    current_obstacles = len(self.obstacle_list)
    if current_obstacles >= num_obstacles:
        if random.random() < 0.02:  
            random_sprite = random.choice(ENGEL_SPRITES)
            obstacle = arcade.Sprite(random_sprite, scale=1.4)  
            x, y = get_safe_position(self.obstacle_list)
            obstacle.center_x = x
            obstacle.center_y = y
            self.obstacle_list.append(obstacle)
        return
    
    for _ in range(num_obstacles - current_obstacles):
        random_sprite = random.choice(ENGEL_SPRITES)
        obstacle = arcade.Sprite(random_sprite, scale=0.8)
        x, y = get_safe_position(self.obstacle_list)
        obstacle.center_x = x
        obstacle.center_y = y
        self.obstacle_list.append(obstacle)