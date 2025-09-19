import pygame


def _centered_rect(x, y, w, h):
    return pygame.Rect(0, 0, w, h).move(x - w // 2, y - h // 2)


def draw_neon_box(surface, x, y, w, h, border=5, color=(0, 255, 70), glow=120, glow_alpha=255):
    temp = pygame.Surface((w + glow * 2, h + glow * 2), pygame.SRCALPHA)
    cx = (w + glow * 2) // 2
    cy = (h + glow * 2) // 2
    for i in range(glow, 0, -10):
        alpha = int(25 * (i / glow))
        rect = _centered_rect(cx, cy, w + i, h + i)
        pygame.draw.rect(temp, (*color, alpha), rect, width=border + i // 20)
    surface.blit(temp, (x - temp.get_width() // 2, y - temp.get_height() // 2), special_flags=pygame.BLEND_PREMULTIPLIED)
    pygame.draw.rect(surface, (*color, 255), _centered_rect(x, y, w, h), width=border)
    inner = pygame.Surface((w - 10, h - 10), pygame.SRCALPHA)
    inner.fill((10, 10, 10, glow_alpha))
    surface.blit(inner, (x - (w - 10) // 2, y - (h - 10) // 2))


def draw_glass_box(surface, x, y, w, h):
    glass = pygame.Surface((w, h), pygame.SRCALPHA)
    glass.fill((30, 30, 30, 180))
    surface.blit(glass, (x - w // 2, y - h // 2))
    draw_neon_box(surface, x, y, w, h, color=(0, 255, 70), glow=60)


def draw_neon_button(surface, font, text, x, y, w, h, color=(0, 255, 70), text_color=(255, 255, 255), font_size=30):
    draw_neon_box(surface, x, y, w, h, border=4, color=color, glow=50)
    inner = pygame.Surface((w - 10, h - 10), pygame.SRCALPHA)
    inner.fill((10, 10, 10, 200))
    surface.blit(inner, (x - (w - 10) // 2, y - (h - 10) // 2))
    text_surf = font.render(text, True, text_color)
    surface.blit(text_surf, text_surf.get_rect(center=(x, y)))
