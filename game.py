import arcade
from consts import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, PLAYER_SPEED, PLAYER_SPRITES_LEFT, PLAYER_SPRITES_RIGHT, ENGEL_SPRITES, OBSTACLE_SPEED
from drawing_functions import draw_menu, draw_game
from PIL import Image
import os
from update import update_game, handle_key_press, handle_key_release
from mouse_events import handle_mouse_press

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

font_path = os.path.join(os.path.dirname(__file__), 'assets', 'VT323-Regular.ttf')
arcade.load_font(font_path)

class SiberMatrix(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
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
        self.header_y = SCREEN_HEIGHT - self.header_h // 2 - header_margin_top
        self.button_width = 200
        self.button_height = 60
        button_margin = 70
        button_spacing = 40
        self.play_button_x = SCREEN_WIDTH // 2
        self.play_button_y = self.header_y - self.header_h // 2 - button_margin - 10
        self.exit_button_x = SCREEN_WIDTH // 2
        self.exit_button_y = self.play_button_y - self.button_height - button_spacing - 10

        music_path = os.path.join(os.path.dirname(__file__), "assets", "clubbed_to_death.wav")
        self.background_music = arcade.load_sound(music_path)
        self.music_player = None
        self.play_background_music()

        self.show_level_message = False
        self.level_transition_pause = False
        self.level_message_timer = 0
        self.level_message_duration = 2.0

        # ----------------------------------------
        
        self.player_speed = PLAYER_SPEED
        self.game_over = False
        self.player_list = None
        self.player_sprite = None
        self.score = 0
        self.last_score = 0
        self.best_score = 0
        self.level = 1

        self.player_textures = []
        self.current_texture_index = 0
        self.animation_counter = 0
        self.facing_right = True
        self.facing_left = True
        
    def play_background_music(self):
        """Arkaplan müziğinin sesini kontrol eder."""
        if self.music_player is None:
            self.music_player = self.background_music.play(loop=True)

    def setup(self):
        """Oyunu başlatır ve gerekli değişkenleri sıfırlar."""
        
        if self.score > 0:
            self.last_score = self.score
            if self.score > self.best_score:
                self.best_score = self.score
        self.level = 1

        self.player_list = arcade.SpriteList()
        self.obstacle_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite(PLAYER_SPRITES_RIGHT[0], scale=0.27)
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = 70
        self.player_sprite.angle = 0
        self.player_list.append(self.player_sprite)

        self.player_textures_right = []
        self.player_textures_left = []

        for texture_path in PLAYER_SPRITES_RIGHT:
            texture = arcade.load_texture(texture_path)
            self.player_textures_right.append(texture)

        for texture_path in PLAYER_SPRITES_LEFT:
            texture = arcade.load_texture(texture_path)
            self.player_textures_left.append(texture)

        self.current_texture_index = 0
        self.facing_right = True
        self.facing_left = False
        self.game_over = False

    def get_visual_speed(self, level):
        base_speed = 1.0
        increment = 0.5
        return base_speed + (level - 1) * increment
    
    def on_draw(self):
        """Ekranı çizer."""
        arcade.start_render()
        
        if self.show_menu:
            draw_menu(self)
            return 
        
        if not self.game_over:
            draw_game(self)

    def on_update(self, time):
        """Oyun mantığını günceller."""
        update_game(self, time)

    def on_mouse_press(self, x, y, button, modifiers):
        """Fare tıklamalarını işler."""
        handle_mouse_press(self, x, y, button, modifiers)
    
    def on_key_press(self, key, modifiers):
        handle_key_press(self, key, modifiers)
    
    def on_key_release(self, key, modifiers):
        handle_key_release(self, key, modifiers)

