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
        