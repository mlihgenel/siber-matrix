import arcade
from consts import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, PLAYER_SPEED, PLAYER_SPRITES_LEFT, PLAYER_SPRITES_RIGHT, ENGEL_SPRITES, OBSTACLE_SPEED
from drawing_functions import draw_menu
from PIL import Image
import os 
from update import update_bg

def load_gif_frames(gif_path):
    """Pillow kullanarak GIF'teki frameleri Arcade Texture listesine çevirir."""
    frames = []
    im = Image.open(gif_path)
    try:
        while True:
            frame = im.copy().convert('RGBA')
            texture = arcade.Texture(name=f"gif_frame_{len(frames)}", image=frame)
            frames.append(texture)
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return frames

class SiberMatrix(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)
        
        self.show_menu = True
        gif_path = os.path.join(os.path.dirname(__file__), 'assets', 'bggif.gif')
        self.menu_bg_frames = load_gif_frames(gif_path)
        self.current_bg_frame_index = 0
        self.bg_frame_timer = 0
        self.bg_frame_delay = 0.1 

        self.header_texture = arcade.load_texture(os.path.join(os.path.dirname(__file__), 'assets', 'matrixfont.png'))
        self.header_w = self.header_texture.width
        self.header_h = self.header_texture.height
        header_margin_top = 150
        self.header_y = SCREEN_HEIGHT - self.header_h//2 - header_margin_top
        self.button_width = 200
        self.button_height = 60
        button_margin = 70
        button_spacing = 40
        self.play_button_x = SCREEN_WIDTH//2
        self.play_button_y = self.header_y - self.header_h//2 - button_margin - 10
        self.exit_button_x = SCREEN_WIDTH//2
        self.exit_button_y = self.play_button_y - self.button_height - button_spacing - 10

        
        
    def on_draw(self):
        if self.show_menu:
            draw_menu(self)
    
    def on_update(self, time):
        update_bg(self, time)
        

