import arcade 

def draw_neon_box(x, y, w, h, border=5, color=(0,255,70), glow=120, glow_alpha=255):
    for i in range(glow, 0, -10):
        arcade.draw_rectangle_outline(x, y, w+i, h+i, (*color, int(25 * (i / glow))), border + i//20)
    arcade.draw_rectangle_outline(x, y, w, h, color + (255,), border)  # Ensure color is a valid tuple with alpha.
    arcade.draw_rectangle_filled(x, y, w-10, h-10, (10, 10, 10, glow_alpha))

# Cam kutu çizimi
def draw_glass_box(x, y, w, h):
    arcade.draw_rectangle_filled(x, y, w, h, (30, 30, 30, 180))
    draw_neon_box(x, y, w, h, color=(0,255,70), glow=60)

# Neon buton çizimi
def draw_neon_button(text, x, y, w, h, color=(0,255,70), text_color=arcade.color.WHITE, font_size=30):
    draw_neon_box(x, y, w, h, border=4, color=color, glow=50)
    arcade.draw_rectangle_filled(x, y, w-10, h-10, (10, 10, 10, 200))
    arcade.draw_text(text, x, y, text_color, font_size, anchor_x="center", anchor_y="center", font_name="assets/VT323-Regular.ttf", bold=True)
