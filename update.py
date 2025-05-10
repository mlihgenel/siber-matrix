import arcade 
from consts import OBSTACLE_SPEED, PLAYER_SPEED

def update_bg(self, time):
    if self.show_menu or self.game_over:
            self.bg_frame_timer += time
            if self.bg_frame_timer >= self.bg_frame_delay:
                self.current_bg_frame_index = (self.current_bg_frame_index + 1) % len(self.menu_bg_frames)
                self.bg_frame_timer = 0
            return