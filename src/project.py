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
    
    def draw_point(self, surface, pos):
        # Must activate when left mouse button is clicked, max three times
        for n in pos:
            rect = self.rays.get_rect(center=n)
            if not self.collision.collidepoint(n):
                return
            else:
                surface.blit(self.rays, rect)
    # (x : <->, y : ^v)


def main():
    pygame.init()
    pygame.display.set_caption('point perspective tool')
    resolution = (1470, 816)
    screen = pygame.display.set_mode(resolution)
    min_clicks = 0
    max_clicks = 3
    pos = []
    rays = VanishingPoints()
    # game
    running = True
    while running:
        # Program Event Loop
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    if min_clicks < max_clicks:
                        pos_x = pygame.mouse.get_pos()
                        print(pos_x)
                        pos.append(pos_x)
                        min_clicks += 1
                        # stops left clicking entirely after 3 clicks
            if event.type == pygame.QUIT:
                running = False
        # Program Logic
        color = pygame.Color(0, 255, 255)
        # Render & Display
        screen.fill(color)
        rays._create_area(screen)
        try:
            rays.draw_point(screen, pos)
        except UnboundLocalError:
            pass
        border = pygame.image.load('assets/border.png').convert_alpha()
        screen.blit(border, (0, 0))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()