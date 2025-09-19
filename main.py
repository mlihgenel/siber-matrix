import pygame
from game import SiberMatrixGame
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE)
    clock = pygame.time.Clock()

    game = SiberMatrixGame(screen)

    running = True
    while running:
        delta_ms = clock.tick(60)
        delta_time = delta_ms / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                game.handle_event(event)

        game.update(delta_time)
        game.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()