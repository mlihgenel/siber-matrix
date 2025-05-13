import arcade 
from consts import OBSTACLE_SPEED, PLAYER_SPEED

def update_game(self, delta_time):
    if self.show_menu or self.game_over:
        self.bg_frame_timer += delta_time
        if self.bg_frame_timer >= self.bg_frame_delay:
            self.current_bg_frame_index = (self.current_bg_frame_index + 1) % len(self.menu_bg_frames)
            self.bg_frame_timer = 0
        return
    if self.show_morpheus or self.paused:
        return

    if self.countdown_active:
        self.countdown_timer += delta_time
        if self.countdown_timer >= self.countdown_duration:
            self.countdown_number -= 1
            self.countdown_timer = 0
            if self.countdown_number <= 0:
                self.countdown_active = False
                self.countdown_number = 3
                self.obstacle_list.clear()
                self.create_obstacles()
        return

    self.player_list.update()

    if self.level_transition_pause:
        self.level_message_timer += delta_time
        if self.level_message_timer >= self.level_message_duration:
            self.level_transition_pause = False
            self.show_level_message = False
            self.level_message_timer = 0
        return

    for obstacle in self.obstacle_list:
        obstacle.center_y -= self.obstacle_speed
        if obstacle.center_y < 0:
            obstacle.remove_from_sprite_lists()
            self.score += 1

    self.create_obstacles()

    next_level_score = self.calculate_next_level_score(self.level)
    if self.score >= next_level_score:
        old_level = self.level
        self.level += 1
        self.show_level_message = True
        self.level_transition_pause = True
        self.level_message_timer = 0
        self.obstacle_list.clear()
        
        if self.level <= 3:
            speed_multiplier = 0.3
        elif self.level <= 7:
            speed_multiplier = 0.5
        else:
            speed_multiplier = 0.7
            
        self.obstacle_speed = min(OBSTACLE_SPEED + (self.level * speed_multiplier), 12)
        self.player_speed = min(PLAYER_SPEED + (self.level * 0.25), 10)
        self.obstacle_list.clear()

    if self.player_sprite.change_x != 0:
        self.animation_counter += 1
        if self.animation_counter > 5:
            self.current_texture_index = (self.current_texture_index + 1) % 2
            if self.player_sprite.change_x > 0:
                self.player_sprite.texture = self.player_textures_right[self.current_texture_index]
            else:
                self.player_sprite.texture = self.player_textures_left[self.current_texture_index]
            self.animation_counter = 0
    else:
        if self.facing_right:
            self.player_sprite.texture = self.player_textures_right[0]
        else:
            self.player_sprite.texture = self.player_textures_left[0]

    if arcade.check_for_collision_with_list(self.player_sprite, self.obstacle_list):
        if not self.morpheus_shown:
            self.show_morpheus = True
            self.morpheus_shown = True
        else:
            self.game_over = True

def handle_key_press(self, key, modifiers):
    if key == arcade.key.Q:
        self.close()
        return

    if self.show_menu:
        if key == arcade.key.SPACE:
            self.show_menu = False
            self.setup()
        return
    
    if self.show_morpheus:
        if key == arcade.key.R:
            self.show_morpheus = False
            self.morpheus_choice = 'red'
            self.countdown_active = True
            for obstacle in arcade.check_for_collision_with_list(self.player_sprite, self.obstacle_list):
                obstacle.remove_from_sprite_lists()
            return
        elif key == arcade.key.M:
            self.show_morpheus = False
            self.morpheus_choice = 'blue'
            self.show_menu = True
            return

    if self.game_over:
        if key == arcade.key.SPACE:
            self.show_menu = True
        return

    if key == arcade.key.ESCAPE:
        self.paused = not self.paused
        return

    if key == arcade.key.LEFT:
        self.player_sprite.change_x = -self.player_speed
        self.facing_right = False
        self.player_sprite.texture = self.player_textures_left[0]
    elif key == arcade.key.RIGHT:
        self.player_sprite.change_x = self.player_speed
        self.facing_right = True
        self.player_sprite.texture = self.player_textures_right[0]

def handle_key_release(self, key, modifiers):
    if key in (arcade.key.LEFT, arcade.key.RIGHT):
        self.player_sprite.change_x = 0