import arcade
from draw_ui import draw_glass_box, draw_neon_box, draw_neon_button
from consts import SCREEN_HEIGHT, SCREEN_WIDTH

def draw_menu(self):
    arcade.start_render()
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, arcade.color.BLACK)

    if self.show_menu:
        # Menü arkaplanı: Seçili frame'i kullanarak çiziyoruz
        current_bg_texture = self.menu_bg_frames[self.current_bg_frame_index]
        arcade.draw_texture_rectangle(
            SCREEN_WIDTH//2,
            SCREEN_HEIGHT//2,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            current_bg_texture
        )
        arcade.draw_texture_rectangle(
            SCREEN_WIDTH//2,
            self.header_y,
            self.header_w,
            self.header_h,
            self.header_texture
        )
        for text, bx, by in [('OYNA', self.play_button_x, self.play_button_y),
                                ('ÇIKIŞ', self.exit_button_x, self.exit_button_y)]:
            draw_neon_box(bx, by, self.button_width, self.button_height, border=4, color=(0,255,70), glow=50)
        
            arcade.draw_text(text, bx, by, arcade.color.WHITE, 35, anchor_x='center', anchor_y='center', font_name='VT323', bold=True)
        
def draw_game(self):
    self.obstacle_list.draw()
    self.player_list.draw()
    
    arcade.draw_text(f"Skor: {self.score}", 40, SCREEN_HEIGHT - 50, (0,255,70), 32, font_name="VT323")
    arcade.draw_text(f"Level: {self.level}", 40, SCREEN_HEIGHT - 90, (0,255,70), 28, font_name="VT323")
    
    visual_speed = self.get_visual_speed(self.level)
    arcade.draw_text(f"Speed: {visual_speed:.1f}x", SCREEN_WIDTH - 200, SCREEN_HEIGHT - 100, (0,255,70), 28, font_name="VT323")
    
    arcade.draw_text(f"En Yüksek: {self.best_score}", 
                    SCREEN_WIDTH - 200, 
                    SCREEN_HEIGHT - 50, 
                    (0,255,70), 
                    28,
                    font_name="VT323")
    
    if self.show_level_message:
        draw_glass_box(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 400, 100)
        arcade.draw_text(f"LEVEL {self.level}!", 
                        SCREEN_WIDTH//2,
                        SCREEN_HEIGHT//2,
                        (0,255,70),
                        40,
                        anchor_x="center",
                        anchor_y="center",
                        font_name="VT323",
                        bold=True)
        