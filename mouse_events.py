import pygame
from consts import SCREEN_WIDTH

def handle_mouse_press(self, x, y, button, modifiers):
    if self.show_menu:
        if abs(x - self.play_button_x) < self.button_width/2 and abs(y - self.play_button_y) < self.button_height/2:
            self.show_menu = False
            self.setup()
            return
        if abs(x - self.exit_button_x) < self.button_width/2 and abs(y - self.exit_button_y) < self.button_height/2:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            return
        if self.how_to_play_rect.collidepoint(x, y):
            self.show_how_to_play = True
            self.show_menu = False
            return
        if self.music_button_rect.collidepoint(x, y):
            self.music_on = not self.music_on
            self.play_background_music()
            return
    if self.show_morpheus:
        if self.red_pill_rect.collidepoint(x, y):
            self.show_morpheus = False
            self.morpheus_choice = 'red'
            self.countdown_active = True
            collided = [ob for ob in self.obstacle_list if self.player_sprite.rect.colliderect(ob.rect)]
            for ob in collided:
                self.obstacle_list.remove(ob)
            return
        if self.blue_pill_rect.collidepoint(x, y):
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
            abs(y - self.back_button_y) < self.back_button_height/2):
            self.show_how_to_play = False
            self.show_menu = True
            return         
    
    # On Game Over screen: any tap returns to menu (mobile-friendly)
    if self.game_over:
        self.show_menu = True
        return
    # no super in pygame version