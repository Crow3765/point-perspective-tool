import pygame
import math

class VanishingPoints():

    def __init__(self):
        self.color = pygame.Color(0, 0, 0)
        self.rays = self.point()
    
    def point(self):
        # The image
        point = pygame.image.load('assets/vanishing_point.png').convert()
        return point
    
    def draw_ray(self, surface, pos_x):
        # Must activate when left mouse button is clicked
        surface.blit(self.rays, pos_x)


def main():
    pygame.init()
    pygame.display.set_caption('point perspective tool')
    clock = pygame.time.Clock()
    dt = 0
    resolution = (1400, 800)
    screen = pygame.display.set_mode(resolution)
    rays = VanishingPoints()
    running = True
    while running:
        # Program Event Loop
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    pos_x = pygame.mouse.get_pos()
                    print(pos_x)
            if event.type == pygame.QUIT:
                running = False
        # Program Logic

        # Render & Display
        color = pygame.Color(255, 255, 255)
        screen.fill(color)
        # Keeps the image on the screen
        try:
            rays.draw_ray(screen, pos_x)
        except UnboundLocalError:
            pass
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()
# (951, 601)

if __name__ == "__main__":
    main()