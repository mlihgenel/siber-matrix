import arcade 
from consts import OBSTACLE_SPEED, PLAYER_SPEED

def update_game(self, time):
    if self.show_menu or self.game_over:
        self.bg_frame_timer += time
        if self.bg_frame_timer >= self.bg_frame_delay:
            self.current_bg_frame_index = (self.current_bg_frame_index + 1) % len(self.menu_bg_frames)
            self.bg_frame_timer = 0
        return
        
    # Sprite'ın pozisyonunu güncelle
    self.player_list.update()  # Bu satırı ekleyin
    
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
 
def handle_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            self.close()
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