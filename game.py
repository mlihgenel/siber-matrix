import os
try:
    from PIL import Image
except Exception:
    Image = None
import pygame
from consts import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, PLAYER_SPEED, PLAYER_SPRITES_LEFT, PLAYER_SPRITES_RIGHT, ENGEL_SPRITES, OBSTACLE_SPEED
from drawing_functions import draw_menu, draw_game , draw_morpheus , draw_countdown , draw_paused, draw_how_to_play, draw_game_over
from update import update_game, handle_key_press, handle_key_release
from mouse_events import handle_mouse_press
from obstacle_manager import create_obstacles

def load_gif_frames(gif_path):
    # Fallback for web where Pillow may not be available
    if Image is None:
        try:
            surface = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets', 'matrix-bg.jpg')).convert()
            return [surface]
        except Exception:
            return [pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))]
    frames = []
    try:
        im = Image.open(gif_path)
        try:
            while True:
                frame = im.copy().convert('RGBA')
                mode = frame.mode
                size = frame.size
                data = frame.tobytes()
                surface = pygame.image.fromstring(data, size, mode)
                frames.append(surface.convert_alpha())
                im.seek(im.tell() + 1)
        except EOFError:
            pass
    except Exception:
        try:
            surface = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets', 'matrix-bg.jpg')).convert()
            frames = [surface]
        except Exception:
            frames = [pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))]
    return frames
    
class SiberMatrixGame:
    def __init__(self, screen):
        self.screen = screen
        self.font_path = os.path.join(os.path.dirname(__file__), 'assets', 'VT323-Regular.ttf')
        self.ui_font_large = pygame.font.Font(self.font_path, 40)
        self.ui_font_medium = pygame.font.Font(self.font_path, 40)
        self.ui_font_small = pygame.font.Font(self.font_path, 28)

        self.show_menu = True
        gif_path = os.path.join(os.path.dirname(__file__), 'assets', 'bggif.gif')
        self.menu_bg_frames = load_gif_frames(gif_path)
        self.current_bg_frame_index = 0
        self.bg_frame_timer = 0
        self.bg_frame_delay = 0.1

        self.header_surface = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets', 'matrixfont.png')).convert_alpha()
        self.header_w = self.header_surface.get_width()
        self.header_h = self.header_surface.get_height()
        header_margin_top = 150
        self.header_y = self.header_h // 2 + header_margin_top
        self.button_width = 200
        self.button_height = 60
        button_margin = 70
        button_spacing = 40
        self.play_button_x = SCREEN_WIDTH // 2
        self.play_button_y = SCREEN_HEIGHT // 2
        self.exit_button_x = SCREEN_WIDTH // 2
        self.exit_button_y = self.play_button_y + self.button_height + button_spacing

        self.music_on = True
        self.music_button_surface_on = pygame.image.load("assets/music-on.png").convert_alpha()
        self.music_button_surface_off = pygame.image.load("assets/music-off.png").convert_alpha()
        self.music_button_scale = 0.6
        self.music_button_surface_on = pygame.transform.rotozoom(self.music_button_surface_on, 0, self.music_button_scale)
        self.music_button_surface_off = pygame.transform.rotozoom(self.music_button_surface_off, 0, self.music_button_scale)
        self.music_button_rect = self.music_button_surface_on.get_rect(center=(80, SCREEN_HEIGHT - 100))

        music_path = os.path.join(os.path.dirname(__file__), "assets", "clubbed_to_death.wav")
        try:
            self.background_music = pygame.mixer.Sound(music_path)
        except Exception:
            self.background_music = None
        self.music_channel = None
        # Start once and keep channel for pause/unpause without restarting
        if self.background_music is not None:
            try:
                self.music_channel = self.background_music.play(loops=-1)
            except Exception:
                self.music_channel = None
        self.play_background_music()

        self.show_level_message = False
        self.level_transition_pause = False
        self.level_message_timer = 0
        self.level_message_duration = 2.0

        # ----------------------------------------
        
        self.player_speed = PLAYER_SPEED
        self.game_over = False
        self.player_group = pygame.sprite.Group()
        self.player_sprite = None
        self.score = 0
        self.last_score = 0
        self.best_score = 0
        self.level = 1
        
        self.paused = False
        self.pause_menu_button_width = 300
        self.pause_menu_button_height = 70
        self.pause_continue_button_x = SCREEN_WIDTH // 2
        self.pause_continue_button_y = SCREEN_HEIGHT // 2 + 40
        self.pause_menu_button_x = SCREEN_WIDTH // 2
        self.pause_menu_button_y = SCREEN_HEIGHT // 2 - 50

        self.player_textures = []
        self.current_texture_index = 0
        self.animation_counter = 0
        self.facing_right = True
        self.facing_left = True

        self.obstacle_list = pygame.sprite.Group()
        self.obstacle_speed = OBSTACLE_SPEED
        
        self.morpheus_shown = False
        self.show_morpheus = False
        self.morpheus_choice = None
        
        self.countdown_active = False    
        self.countdown_number = 3
        self.countdown_timer = 0
        self.countdown_duration = 1.0 
        
        self.blue_pill_surface = pygame.image.load("assets/heroes/blue_pill.png").convert_alpha()
        self.red_pill_surface = pygame.image.load("assets/heroes/red_pill.png").convert_alpha()
        self.blue_pill_surface = pygame.transform.rotozoom(self.blue_pill_surface, 0, 0.75)
        self.red_pill_surface = pygame.transform.rotozoom(self.red_pill_surface, 0, 0.75)
        self.red_pill_rect = self.red_pill_surface.get_rect(center=(SCREEN_WIDTH//2 - 165, SCREEN_HEIGHT//2 + 50))
        self.blue_pill_rect = self.blue_pill_surface.get_rect(center=(SCREEN_WIDTH//2 + 155, SCREEN_HEIGHT//2 + 50))
        self.pill_button_width = 170
        self.pill_button_height = 170
        
        self.show_how_to_play = False
        self.how_to_play_surface = pygame.image.load("assets/howtoplaybutton.png").convert_alpha()
        self.how_to_play_surface = pygame.transform.rotozoom(self.how_to_play_surface, 0, 0.6)
        self.how_to_play_rect = self.how_to_play_surface.get_rect(center=(SCREEN_WIDTH - 80, SCREEN_HEIGHT - 100))
        self.back_button_width = 200
        self.back_button_height = 50
        self.back_button_y = SCREEN_HEIGHT - 140
        
        self.game_over = False

    def play_background_music(self):
        if self.background_music is None or self.music_channel is None:
            return
        try:
            if self.music_on:
                self.music_channel.set_volume(1.0)
                self.music_channel.unpause()
            else:
                self.music_channel.pause()
        except Exception:
            pass

        # Touch drag controls (for mobile/web)
        self.touch_drag_enabled = True
        self.touch_active = False
        self.touch_target_x = None


    def setup(self):
        if self.score > 0:
            self.last_score = self.score
            if self.score > self.best_score:
                self.best_score = self.score
        self.level = 1

        self.player_group.empty()
        self.obstacle_list.empty()

        # Load player images
        self.player_images_right = [pygame.image.load(p).convert_alpha() for p in PLAYER_SPRITES_RIGHT]
        self.player_images_left = [pygame.image.load(p).convert_alpha() for p in PLAYER_SPRITES_LEFT]
        # Scale player
        self.player_images_right = [pygame.transform.rotozoom(img, 0, 0.27) for img in self.player_images_right]
        self.player_images_left = [pygame.transform.rotozoom(img, 0, 0.27) for img in self.player_images_left]

        # Create player sprite
        self.player_sprite = _Player(self.player_images_right[0])
        self.player_sprite.rect.centerx = SCREEN_WIDTH // 2
        self.player_sprite.rect.centery = SCREEN_HEIGHT - 70
        self.player_group.add(self.player_sprite)

        self.player_textures_right = self.player_images_right
        self.player_textures_left = self.player_images_left

        self.current_texture_index = 0
        self.facing_right = True 

        self.create_obstacles()

        self.game_over = False
        self.score = 0
        self.morpheus_shown = False
        self.show_morpheus = False
        self.morpheus_choice = None
        self.game_over = False

        self.create_obstacles()

    def create_obstacles(self):
        create_obstacles(self)

    def get_visual_speed(self, level):
        base_speed = 1.0
        increment = 0.5
        return base_speed + (level - 1) * increment
    
    def draw(self, screen):
        screen.fill((0, 0, 0))
        if self.show_menu:
            draw_menu(self)
            return
        if self.show_how_to_play:
            draw_how_to_play(self)
            return
        if self.countdown_active:
            draw_countdown(self)
            return

        if not self.game_over:
            draw_game(self)
        else:
            draw_game_over(self)

        if self.paused:
            draw_paused(self)
            return

        if self.show_morpheus:
            draw_morpheus(self)
            return


    def calculate_next_level_score(self, current_level):
        if current_level <= 3:
            return current_level * 35
        elif current_level <= 7:
            return 105 + (current_level - 3) * 45
        else:
            return 285 + (current_level - 7) * 60

    def update(self, time):
        update_game(self, time)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Drag-to-move during gameplay
            if not (self.show_menu or self.show_how_to_play or self.show_morpheus or self.paused or self.game_over):
                if self.touch_drag_enabled:
                    self.touch_active = True
                    self.touch_target_x = x
                    return
            handle_mouse_press(self, x, y, event.button, None)
        elif event.type == pygame.KEYDOWN:
            handle_key_press(self, event.key, None)
        elif event.type == pygame.KEYUP:
            handle_key_release(self, event.key, None)
        elif event.type == pygame.MOUSEBUTTONUP:
            # Stop drag movement on release
            self.touch_active = False
            self.touch_target_x = None
        elif event.type == pygame.MOUSEMOTION:
            if self.touch_active and not (self.show_menu or self.show_how_to_play or self.show_morpheus or self.paused or self.game_over):
                self.touch_target_x = event.pos[0]


class _Player(pygame.sprite.Sprite):
    def __init__(self, image_surface):
        super().__init__()
        self.image = image_surface
        self.rect = self.image.get_rect()
        self.change_x = 0
        

