import pygame
import math

class VanishingPoints():

    def __init__(self):
        self.color = pygame.Color(0, 0, 0)

    def end(self, resolution, pos_x):
        # Needs to extend to the edge of the canvas
        angle = math.radians(45)
        x = pos_x[0] + resolution[0] * math.cos(angle)
        y = pos_x[1] + resolution[1] * math.sin(angle)
        pos_y = (x, y)
        return pos_y

    def draw_rays(self, surface, pos_x, pos_y):
        # Must activate when left mouse button is clicked
        pygame.draw.line(surface, self.color, pos_x, pos_y, 3)


def main():
    pygame.init()
    pygame.display.set_caption('point perspective tool')
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
        try:
            pos_y = rays.end(resolution, pos_x)
        except UnboundLocalError:
            pass
        # Render & Display
        color = pygame.Color(255, 255, 255)
        screen.fill(color)
        if pygame.mouse.get_pressed()[0] == True:
            rays.draw_rays(screen, pos_x, pos_y)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()