import pygame
import math


class ColoredButtons():

    def __init__(self):
        self.area = self.button()
        self.pos = (1100, 5)

    def button(self):
        button = pygame.image.load('assets/colors_button.png').convert_alpha()
        return button

    def colors(self):
        # To simplify process, use colored buttons with predefined palettes to 
        # set all vanishing points to those colors when pressed
        pass

    def set_area(self, surface):
        surface.blit(self.area, self.pos)

class VanishingPoints():

    def __init__(self):
        self.color = pygame.Color(0, 0, 0)
        self.rays = self.point()
    
    def point(self):
        # The image
        point = pygame.image.load('assets/vanishing_point.png').convert_alpha()
        return point
    
    def draw_point(self, surface, pos_x):
        # Must activate when left mouse button is clicked
        rect = self.rays.get_rect(center=pos_x)
        surface.blit(self.rays, rect)


def main():
    pygame.init()
    pygame.display.set_caption('point perspective tool')
    resolution = (1400, 800)
    screen = pygame.display.set_mode(resolution)
    cb = ColoredButtons()
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
        color = pygame.Color(0, 255, 255)
        screen.fill(color)
        # Keeps the image on the screen
        try:
            rays.draw_point(screen, pos_x)
        except UnboundLocalError:
            pass
        border = pygame.image.load('assets/border.png').convert_alpha()
        screen.blit(border, (0, 0))
        cb.set_area(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()