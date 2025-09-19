import pygame
from consts import OBSTACLE_SPEED, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

def update_game(self, delta_time):
    if self.show_menu or self.game_over:
        self.bg_frame_timer += delta_time
        if self.bg_frame_timer >= self.bg_frame_delay:
            self.current_bg_frame_index = (self.current_bg_frame_index + 1) % len(self.menu_bg_frames)
            self.bg_frame_timer = 0
        return
    if self.show_morpheus or self.show_how_to_play or self.paused:
        return

    if self.countdown_active:
        self.countdown_timer += delta_time
        if self.countdown_timer >= self.countdown_duration:
            self.countdown_number -= 1
            self.countdown_timer = 0
            if self.countdown_number <= 0:
                self.countdown_active = False
                self.countdown_number = 3
                self.obstacle_list.empty()
                self.create_obstacles()
        return

    if self.player_sprite:
        self.player_sprite.rect.centerx += self.player_sprite.change_x
        player_w = self.player_sprite.rect.width
        if self.player_sprite.rect.centerx < player_w // 2:
            self.player_sprite.rect.centerx = player_w // 2
            self.player_sprite.change_x = 0
        elif self.player_sprite.rect.centerx > SCREEN_WIDTH - player_w // 2:
            self.player_sprite.rect.centerx = SCREEN_WIDTH - player_w // 2
            self.player_sprite.change_x = 0

    if self.level_transition_pause:
        self.level_message_timer += delta_time
        if self.level_message_timer >= self.level_message_duration:
            self.level_transition_pause = False
            self.show_level_message = False
            self.level_message_timer = 0
        return
   
    # Drag-to-move: move player towards touch_target_x while active
    if getattr(self, 'touch_drag_enabled', False) and self.player_sprite and self.touch_active and self.touch_target_x is not None:
        if abs(self.touch_target_x - self.player_sprite.rect.centerx) <= self.player_speed:
            self.player_sprite.rect.centerx = int(self.touch_target_x)
            self.player_sprite.change_x = 0
        elif self.touch_target_x < self.player_sprite.rect.centerx:
            self.player_sprite.change_x = -self.player_speed
            self.facing_right = False
            self.player_sprite.image = self.player_textures_left[0]
        elif self.touch_target_x > self.player_sprite.rect.centerx:
            self.player_sprite.change_x = self.player_speed
            self.facing_right = True
            self.player_sprite.image = self.player_textures_right[0]
    for obstacle in list(self.obstacle_list):
        obstacle.rect.centery += self.obstacle_speed
        if obstacle.rect.top > SCREEN_HEIGHT:
            self.obstacle_list.remove(obstacle)
            self.score += 1
    self.create_obstacles()

    next_level_score = self.calculate_next_level_score(self.level)
    if self.score >= next_level_score:
        old_level = self.level
        self.level += 1
        self.show_level_message = True
        self.level_transition_pause = True
        self.level_message_timer = 0
        self.obstacle_list.empty()
        if self.level <= 3:
            speed_multiplier = 0.3
        elif self.level <= 7:
            speed_multiplier = 0.5
        else:
            speed_multiplier = 0.7
        self.obstacle_speed = min(OBSTACLE_SPEED + (self.level * speed_multiplier), 12)
        self.player_speed = min(PLAYER_SPEED + (self.level * 0.25), 10)
        self.obstacle_list.empty()

    if self.player_sprite.change_x != 0:
        self.animation_counter += 1
        if self.animation_counter > 5:
            self.current_texture_index = (self.current_texture_index + 1) % 2
            if self.player_sprite.change_x > 0:
                self.player_sprite.image = self.player_textures_right[self.current_texture_index]
            else:
                self.player_sprite.image = self.player_textures_left[self.current_texture_index]
            self.animation_counter = 0
    else:
        if self.facing_right:
            self.player_sprite.image = self.player_textures_right[0]
        else:
            self.player_sprite.image = self.player_textures_left[0]
    # Collision
    collided = any(self.player_sprite.rect.colliderect(ob.rect) for ob in self.obstacle_list)
    if collided:
        if not self.morpheus_shown:
            self.show_morpheus = True
            self.morpheus_shown = True
        else:
            self.last_score = self.score  
            if self.score > self.best_score: 
                self.best_score = self.score
            self.game_over = True

def handle_key_press(self, key, modifiers):
    if key == pygame.K_q:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        return

    if self.game_over:
        if key == pygame.K_SPACE:
            self.show_menu = True
        return

    if key == pygame.K_ESCAPE:
        self.paused = not self.paused
        return

    if key == pygame.K_LEFT:
        self.player_sprite.change_x = -self.player_speed
        self.facing_right = False
        self.player_sprite.image = self.player_textures_left[0]
    elif key == pygame.K_RIGHT:
        self.player_sprite.change_x = self.player_speed
        self.facing_right = True
        self.player_sprite.image = self.player_textures_right[0]

def handle_key_release(self, key, modifiers):
    if key in (pygame.K_LEFT, pygame.K_RIGHT):
        self.player_sprite.change_x = 0