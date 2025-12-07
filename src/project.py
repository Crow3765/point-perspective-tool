import pygame
import math


class VanishingPoints():

    def __init__(self):
        self.color = pygame.Color(0, 0, 0)
        self.rays = self.point()
        self.collision = self.collision_box()
    
    def point(self):
        # point image
        point = pygame.image.load('assets/vanishing_point.png').convert_alpha()
        return point
    
    def collision_box(self):
        # collision image
        box = pygame.Rect(109, 101, 1252, 614)
        return box

    def _create_area(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.collision)
    
    def draw_point(self, surface, pos_x):
        # Must activate when left mouse button is clicked
        rect = self.rays.get_rect(center=pos_x)
        # clips to specified area area
        if not self.collision.collidepoint(pos_x):
            return
        else:
            surface.blit(self.rays, rect)
    # (x : <->, y : ^v)


def main():
    pygame.init()
    pygame.display.set_caption('point perspective tool')
    resolution = (1470, 816)
    screen = pygame.display.set_mode(resolution)
    rays = VanishingPoints()
    # game
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
        color = pygame.Color(0, 255, 255)
        # Render & Display
        screen.fill(color)
        rays._create_area(screen)
        # Keeps the image on the screen
        try:
            rays.draw_point(screen, pos_x)
        except UnboundLocalError:
            pass
        border = pygame.image.load('assets/border.png').convert_alpha()
        screen.blit(border, (0, 0))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()