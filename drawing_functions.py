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
    
    self.how_to_play_button.draw()
    self.music_button.draw()
        
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
        
def draw_morpheus(self):
    box_x, box_y = SCREEN_WIDTH//2, SCREEN_HEIGHT//2
    matrix_bg = arcade.load_texture("assets/matrix-bg.jpg")
    arcade.draw_texture_rectangle(box_x, box_y, SCREEN_WIDTH, SCREEN_HEIGHT, matrix_bg)
    morpheus_width = int(SCREEN_WIDTH * 0.6)
    morpheus_height = int(morpheus_width * 1)
    morpheus_texture = arcade.load_texture("assets/heroes/morpheus.png")
    arcade.draw_texture_rectangle(box_x, box_y+100, morpheus_width, morpheus_height, morpheus_texture)

    arcade.draw_text("CHOOSE ONE", 
                    box_x, 
                    box_y + 370, 
                    (0,255,70), 
                    61, 
                    anchor_x="center", 
                    anchor_y="center", 
                    font_name="VT323",
                    bold=True)
    
    self.blue_pill_button.draw()
    self.red_pill_button.draw()

def draw_countdown(self):
    arcade.draw_text("İkinci Bir Şans", 
                           SCREEN_WIDTH//2,
                           SCREEN_HEIGHT//2 + 100,
                           (0,255,70),
                           40,
                           anchor_x="center",
                           anchor_y="center",
                           font_name="VT323",
                           bold=True)
            
    arcade.draw_text(f"{self.countdown_number}", 
                    SCREEN_WIDTH//2,
                    SCREEN_HEIGHT//2,
                    (0,255,70),
                    100,
                    anchor_x="center",
                    anchor_y="center",
                    font_name="VT323",
                    bold=True)
    
def draw_paused(self):
    self.obstacle_list.draw()
    self.player_list.draw()
    draw_neon_box(self.pause_continue_button_x, self.pause_continue_button_y, self.pause_menu_button_width, self.pause_menu_button_height, border=4, color=(0,255,70), glow=30, glow_alpha=10)
    arcade.draw_text("Devam Et", self.pause_continue_button_x, self.pause_continue_button_y, arcade.color.WHITE, 36, anchor_x="center", anchor_y="center", font_name="VT323", bold=True)
    draw_neon_box(self.pause_menu_button_x, self.pause_menu_button_y, self.pause_menu_button_width, self.pause_menu_button_height, border=4, color=(0,255,70), glow=30, glow_alpha=10)
    arcade.draw_text("Ana Menüye Dön", self.pause_menu_button_x, self.pause_menu_button_y, arcade.color.WHITE, 25, anchor_x="center", anchor_y="center", font_name="VT323", bold=True)

def draw_how_to_play(self):
    draw_glass_box(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 700, 700)
            
    arcade.draw_text("NASIL OYNANIR", 
                    SCREEN_WIDTH//2,
                    SCREEN_HEIGHT - 150,
                    (0,255,70),
                    40,
                    anchor_x="center",
                    anchor_y="center",
                    font_name="VT323",
                    bold=True)

    instructions = [
        "Matrix'te hareket etmek için Sağ/Sol ok tuşlarını kullan",
        "Engellerden kaç ve hayatta kal",
        "Her engelden kaçtığında Matrix'te güçlenirsin",
        "Yeterli güce ulaştığında yeni seviyeye yükselirsin",
        "Eğer yakalanırsan, Morpheus seni 1 kez kurtarabilir",
        "Morpheus'un seçimi ile karşılaştığında:",
        "- Kırmızı hap: Gerçeği görmeye devam et",
        "- Mavi hap: Matrixten çık"
    ]
    
    start_y = SCREEN_HEIGHT - 250
    for i, text in enumerate(instructions):
        arcade.draw_text(text,
                        SCREEN_WIDTH//2,
                        start_y - i * 45, 
                        (0,255,70),
                        20, 
                        anchor_x="center",
                        anchor_y="center",
                        font_name="VT323")
    draw_neon_box(
    SCREEN_WIDTH//2,  
    150,              
    self.back_button_width,
    self.back_button_height,
    border=4,
    color=(0,255,70),
    glow=50
    )
    
    arcade.draw_text(
        "ANA MENÜYE DÖN",
        SCREEN_WIDTH//2,
        150,
        arcade.color.WHITE,
        25,
        anchor_x="center",
        anchor_y="center",
        font_name="VT323",
        bold=True
    )

def draw_game_over(self):
    current_bg_texture = self.menu_bg_frames[self.current_bg_frame_index]
    arcade.draw_texture_rectangle(
        SCREEN_WIDTH//2,
        SCREEN_HEIGHT//2,
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        current_bg_texture
    )

    box_y = SCREEN_HEIGHT/2 + 200
    arcade.draw_text("OYUN BİTTİ!", SCREEN_WIDTH/2, box_y,
                    (0,255,70), 55, anchor_x="center", anchor_y="center", font_name="VT323", bold=True)

    score_box_y = SCREEN_HEIGHT/2 + 80
    draw_glass_box(SCREEN_WIDTH/2, score_box_y, 400, 80)
    arcade.draw_text(f"En Yüksek Skor: {self.best_score}", SCREEN_WIDTH/2, score_box_y + 15,
                    (0,255,70), 25, anchor_x="center", anchor_y="center", font_name="VT323", bold=True)
    arcade.draw_text(f"Son Skor: {self.last_score}", SCREEN_WIDTH/2, score_box_y - 15,
                    (0,255,70), 24, anchor_x="center", anchor_y="center", font_name="VT323")

    button_y = SCREEN_HEIGHT/2 - 100
    arcade.draw_text("Ana Menüye dönmek için SPACE tuşuna basın", SCREEN_WIDTH/2, button_y,
                    (255,255,255), 25, anchor_x="center", anchor_y="center", font_name="VT323", bold=True)