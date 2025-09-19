import pygame
import random
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, ENGEL_SPRITES

def is_safe_position(obstacles_group, x, y, min_distance=100):
    for obstacle in obstacles_group:
        if (abs(obstacle.rect.centerx - x) < min_distance and 
            abs(obstacle.rect.centery - y) < min_distance):
            return False
        
    return True

def get_safe_position(obstacles_group):
    margin = 50
    y = -100
    x = random.randint(margin, SCREEN_WIDTH - margin)
    
    while not is_safe_position(obstacles_group, x, y):
        y -= random.randint(100, 200)
    
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
            obstacle = _Obstacle(random_sprite, scale=1.4)
            x, y = get_safe_position(self.obstacle_list)
            obstacle.rect.centerx = x
            obstacle.rect.centery = y
            self.obstacle_list.add(obstacle)
        return
    
    for _ in range(num_obstacles - current_obstacles):
        random_sprite = random.choice(ENGEL_SPRITES)
        obstacle = _Obstacle(random_sprite, scale=0.8)
        x, y = get_safe_position(self.obstacle_list)
        obstacle.rect.centerx = x
        obstacle.rect.centery = y
        self.obstacle_list.add(obstacle)


class _Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_path, scale=1.0):
        super().__init__()
        image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.rotozoom(image, 0, scale)
        self.rect = self.image.get_rect()