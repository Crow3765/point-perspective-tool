import pygame


def main():
    pygame.init()
    pygame.display.set_caption('point perspective tool')
    resolution = (1400, 800)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        # Program Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Program Logic
        # Render & Display
        color = pygame.Color(255, 255, 255)
        screen.fill(color)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()