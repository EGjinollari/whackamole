import pygame
import random


def main():
    x = 0
    y = 0
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect.collidepoint(mole_image.get_rect(topleft=(x, y)), pygame.mouse.get_pos()):

                        x = random.randrange(0, 20) * 32
                        y = random.randrange(0, 16) * 32

            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))

            # Make Grid
            i = 32
            while i < 640:
                pygame.draw.line(screen, 'black', (i, 0), (i, 512))
                i += 32
            i = 32
            while i < 512:
                pygame.draw.line(screen, 'black', (0, i), (640, i))
                i += 32

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
