import arcade
from consts import SCREEN_WIDTH

def handle_mouse_press(self, x, y, button, modifiers):
    if self.show_menu:
        if abs(x - self.play_button_x) < self.button_width/2 and abs(y - self.play_button_y) < self.button_height/2:
            self.show_menu = False
            self.setup()
            return
        if abs(x - self.exit_button_x) < self.button_width/2 and abs(y - self.exit_button_y) < self.button_height/2:
            self.close()
            return
        if (abs(x - self.how_to_play_button.center_x) < self.how_to_play_button.width/2 and 
            abs(y - self.how_to_play_button.center_y) < self.how_to_play_button.height/2):
            self.show_how_to_play = True
            self.show_menu = False
            if self.player_list is None:
                self.player_list = arcade.SpriteList()
            if self.obstacle_list is None:
                self.obstacle_list = arcade.SpriteList()
            return
        if (abs(x - self.how_to_play_button.center_x) < self.how_to_play_button.width/2 and 
            abs(y - self.how_to_play_button.center_y) < self.how_to_play_button.height/2):
            self.show_how_to_play = True
            self.show_menu = False
            if self.player_list is None:
                self.player_list = arcade.SpriteList()
            if self.obstacle_list is None:
                self.obstacle_list = arcade.SpriteList()
            return
        if (abs(x - self.music_button.center_x) < self.music_button.width/2 and 
            abs(y - self.music_button.center_y) < self.music_button.height/2):
            self.music_on = not self.music_on
            if self.music_on:
                self.music_button.texture = arcade.load_texture("assets/music-on.png")
            else:
                self.music_button.texture = arcade.load_texture("assets/music-off.png")
            self.play_background_music()
            return
    if self.show_morpheus:
        if (abs(x - self.red_pill_button.center_x) < self.pill_button_width/2 and 
            abs(y - self.red_pill_button.center_y) < self.pill_button_height/2):
            self.show_morpheus = False
            self.morpheus_choice = 'red'
            self.countdown_active = True
            for obstacle in arcade.check_for_collision_with_list(self.player_sprite, self.obstacle_list):
                obstacle.remove_from_sprite_lists()
            return
        if (abs(x - self.blue_pill_button.center_x) < self.pill_button_width/2 and 
            abs(y - self.blue_pill_button.center_y) < self.pill_button_height/2):
            self.show_morpheus = False
            self.morpheus_choice = 'blue'
            self.show_menu = True
            return
    if self.paused:
        if (abs(x - self.pause_continue_button_x) < self.pause_menu_button_width/2 and
            abs(y - self.pause_continue_button_y) < self.pause_menu_button_height/2):
            self.paused = False
            return
        if (abs(x - self.pause_menu_button_x) < self.pause_menu_button_width/2 and
            abs(y - self.pause_menu_button_y) < self.pause_menu_button_height/2):
            self.paused = False
            self.show_menu = True
            self.setup()
            return
    if self.show_how_to_play:
        if (abs(x - SCREEN_WIDTH//2) < self.back_button_width/2 and 
            abs(y - 150) < self.back_button_height/2):
            self.show_how_to_play = False
            self.show_menu = True
            return         
    
    super(self.__class__, self).on_mouse_press(x, y, button, modifiers)  