import arcade
from consts import SCREEN_WIDTH

def handle_mouse_press(self, x, y, button, modifiers):
    if self.show_menu:
        if abs(x - self.play_button_x) < self.button_width/2 and abs(y - self.play_button_y) < self.button_height/2:
            self.show_menu = False
            self.setup()
            return
    if self.show_morpheus:
        if (abs(x - self.red_pill_button.center_x) < self.pill_button_width/2 and 
            abs(y - self.red_pill_button.center_y) < self.pill_button_height/2):
            self.show_morpheus = False
            self.morpheus_choice = 'red'
            for obstacle in arcade.check_for_collision_with_list(self.player_sprite, self.obstacle_list):
                obstacle.remove_from_sprite_lists()
            return

        if (abs(x - self.blue_pill_button.center_x) < self.pill_button_width/2 and 
            abs(y - self.blue_pill_button.center_y) < self.pill_button_height/2):
            self.show_morpheus = False
            self.morpheus_choice = 'blue'
            self.show_menu = True
            return
        
    if abs(x - self.exit_button_x) < self.button_width/2 and abs(y - self.exit_button_y) < self.button_height/2:
        self.close()
        return   
    super(self.__class__, self).on_mouse_press(x, y, button, modifiers)  