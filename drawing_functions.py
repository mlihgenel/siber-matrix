import pygame
from draw_ui import draw_glass_box, draw_neon_box, draw_neon_button
from consts import SCREEN_HEIGHT, SCREEN_WIDTH

def draw_menu(self):
    # Background frame
    current_bg_surface = self.menu_bg_frames[self.current_bg_frame_index]
    self.screen.blit(pygame.transform.smoothscale(current_bg_surface, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
    # Header
    self.screen.blit(self.header_surface, self.header_surface.get_rect(center=(SCREEN_WIDTH // 2, self.header_y)))
    # Buttons with thin borders
    border_color = (0, 255, 70)
    pygame.draw.rect(self.screen, border_color, pygame.Rect(self.play_button_x - self.button_width//2, self.play_button_y - self.button_height//2, self.button_width, self.button_height), width=2)
    pygame.draw.rect(self.screen, border_color, pygame.Rect(self.exit_button_x - self.button_width//2, self.exit_button_y - self.button_height//2, self.button_width, self.button_height), width=2)
    title_font = pygame.font.Font(self.font_path, 35)
    play_text = title_font.render('OYNA', True, (255, 255, 255))
    exit_text = title_font.render('ÇIKIŞ', True, (255, 255, 255))
    self.screen.blit(play_text, play_text.get_rect(center=(self.play_button_x, self.play_button_y)))
    self.screen.blit(exit_text, exit_text.get_rect(center=(self.exit_button_x, self.exit_button_y)))
    # Icons
    self.screen.blit(self.how_to_play_surface, self.how_to_play_rect)
    music_surface = self.music_button_surface_on if self.music_on else self.music_button_surface_off
    self.screen.blit(music_surface, self.music_button_rect)
        
def draw_game(self):
    # Draw sprites
    for obstacle in self.obstacle_list:
        self.screen.blit(obstacle.image, obstacle.rect)
    if self.player_sprite:
        self.screen.blit(self.player_sprite.image, self.player_sprite.rect)
    # Texts
    score_text = self.ui_font_medium.render(f"Skor: {self.score}", True, (0, 255, 70))
    level_text = self.ui_font_small.render(f"Level: {self.level}", True, (0, 255, 70))
    visual_speed = self.get_visual_speed(self.level)
    speed_text = self.ui_font_small.render(f"Speed: {visual_speed:.1f}x", True, (0, 255, 70))
    best_text = self.ui_font_small.render(f"En Yüksek: {self.best_score}", True, (0, 255, 70))
    self.screen.blit(score_text, (40, 20))
    self.screen.blit(level_text, (40, 55))
    self.screen.blit(speed_text, (SCREEN_WIDTH - 200, 55))
    self.screen.blit(best_text, (SCREEN_WIDTH - 200, 20))
    # Level message
    if self.show_level_message:
        draw_glass_box(self.screen, SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 400, 100)
        msg = self.ui_font_large.render(f"LEVEL {self.level}!", True, (0, 255, 70))
        self.screen.blit(msg, msg.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)))

    # No on-screen buttons for movement; drag-to-move is handled by events
        
def draw_morpheus(self):
    box_x, box_y = SCREEN_WIDTH//2, SCREEN_HEIGHT//2
    bg = pygame.image.load("assets/matrix-bg.jpg").convert()
    bg = pygame.transform.smoothscale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    self.screen.blit(bg, (0, 0))
    morpheus_img = pygame.image.load("assets/heroes/morpheus.png").convert_alpha()
    target_w = int(SCREEN_WIDTH * 0.6)
    target_h = int(target_w * 1)
    morpheus_img = pygame.transform.smoothscale(morpheus_img, (target_w, target_h))
    self.screen.blit(morpheus_img, morpheus_img.get_rect(center=(box_x, box_y + 100)))
    title = pygame.font.Font(self.font_path, 61).render("CHOOSE ONE", True, (0, 255, 70))
    self.screen.blit(title, title.get_rect(center=(box_x, box_y + 370)))
    self.screen.blit(self.blue_pill_surface, self.blue_pill_rect)
    self.screen.blit(self.red_pill_surface, self.red_pill_rect)

def draw_countdown(self):
    title = self.ui_font_large.render("İkinci Bir Şans", True, (0, 255, 70))
    self.screen.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 100)))
    number_font = pygame.font.Font(self.font_path, 100)
    number = number_font.render(f"{self.countdown_number}", True, (0, 255, 70))
    self.screen.blit(number, number.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)))
    
def draw_paused(self):
    for obstacle in self.obstacle_list:
        self.screen.blit(obstacle.image, obstacle.rect)
    if self.player_sprite:
        self.screen.blit(self.player_sprite.image, self.player_sprite.rect)
    draw_neon_box(self.screen, self.pause_continue_button_x, self.pause_continue_button_y, self.pause_menu_button_width, self.pause_menu_button_height, border=4, color=(0,255,70), glow=30, glow_alpha=10)
    t1 = pygame.font.Font(self.font_path, 36).render("Devam Et", True, (255,255,255))
    self.screen.blit(t1, t1.get_rect(center=(self.pause_continue_button_x, self.pause_continue_button_y)))
    draw_neon_box(self.screen, self.pause_menu_button_x, self.pause_menu_button_y, self.pause_menu_button_width, self.pause_menu_button_height, border=4, color=(0,255,70), glow=30, glow_alpha=10)
    t2 = pygame.font.Font(self.font_path, 25).render("Ana Menüye Dön", True, (255,255,255))
    self.screen.blit(t2, t2.get_rect(center=(self.pause_menu_button_x, self.pause_menu_button_y)))

def draw_how_to_play(self):
    # Panel without neon borders (remove green top/bottom glow)
    panel_w, panel_h = 700, 700
    panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
    panel.fill((30, 30, 30, 180))
    self.screen.blit(panel, (SCREEN_WIDTH//2 - panel_w//2, SCREEN_HEIGHT//2 - panel_h//2))

    # Title at top
    title = pygame.font.Font(self.font_path, 40).render("NASIL OYNANIR", True, (0, 255, 70))
    self.screen.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, 120)))

    # Canonical instructions, then reverse order as requested
    canonical = [
        "Matrix'te hareket etmek için Sağ/Sol ok tuşlarını kullan",
        "Engellerden kaç ve hayatta kal",
        "Her engelden kaçtığında Matrix'te güçlenirsin",
        "Yeterli güce ulaştığında yeni seviyeye yükselirsin",
        "Eğer yakalanırsan, Morpheus seni 1 kez kurtarabilir",
        "Morpheus'un seçimi ile karşılaştığında:",
        "- Kırmızı hap: Gerçeği görmeye devam et",
        "- Mavi hap: Matrixten çık",
    ]
    instructions = list(canonical)

    # Center vertically within the panel area
    line_gap = 40
    line_font = pygame.font.Font(self.font_path, 20)
    total_h = len(instructions) * line_gap
    panel_top = 180
    panel_bottom = self.back_button_y - 80
    panel_center_y = (panel_top + panel_bottom) // 2
    start_y = panel_center_y - total_h // 2
    for i, text in enumerate(instructions):
        surf = line_font.render(text, True, (0, 255, 70))
        self.screen.blit(surf, (SCREEN_WIDTH//2 - surf.get_width()//2, start_y + i * line_gap))

    # Back button at bottom with thin border only
    border_color = (0, 255, 70)
    pygame.draw.rect(self.screen, border_color, pygame.Rect(
        SCREEN_WIDTH//2 - self.back_button_width//2,
        self.back_button_y - self.back_button_height//2,
        self.back_button_width,
        self.back_button_height
    ), width=2)
    back = pygame.font.Font(self.font_path, 25).render("ANA MENÜYE DÖN", True, (255,255,255))
    self.screen.blit(back, back.get_rect(center=(SCREEN_WIDTH//2, self.back_button_y)))

def draw_game_over(self):
    bg = pygame.transform.smoothscale(self.menu_bg_frames[self.current_bg_frame_index], (SCREEN_WIDTH, SCREEN_HEIGHT))
    self.screen.blit(bg, (0, 0))
    box_y = SCREEN_HEIGHT/2 - 200
    title = pygame.font.Font(self.font_path, 70).render("OYUN BİTTİ!", True, (0, 255, 70))
    self.screen.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, int(box_y))))
    score_box_y = SCREEN_HEIGHT/2 - 80
    # Thin bordered semi-transparent box
    box_w, box_h = 400, 80
    panel = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
    panel.fill((30, 30, 30, 180))
    self.screen.blit(panel, (SCREEN_WIDTH//2 - box_w//2, int(score_box_y) - box_h//2))
    pygame.draw.rect(self.screen, (0, 255, 70), pygame.Rect(SCREEN_WIDTH//2 - box_w//2, int(score_box_y) - box_h//2, box_w, box_h), width=2)
    t1 = pygame.font.Font(self.font_path, 32).render(f"En Yüksek Skor: {self.best_score}", True, (0, 255, 70))
    t2 = pygame.font.Font(self.font_path, 30).render(f"Son Skor: {self.last_score}", True, (0, 255, 70))
    self.screen.blit(t1, t1.get_rect(center=(SCREEN_WIDTH//2, int(score_box_y) + 15)))
    self.screen.blit(t2, t2.get_rect(center=(SCREEN_WIDTH//2, int(score_box_y) - 15)))
    button_y = SCREEN_HEIGHT/2 + 100
    t3 = pygame.font.Font(self.font_path, 28).render("Ana Menüye dönmek için SPACE tuşuna basın", True, (255, 255, 255))
    self.screen.blit(t3, t3.get_rect(center=(SCREEN_WIDTH//2, int(button_y))))