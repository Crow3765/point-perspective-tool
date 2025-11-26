import pygame


class VanishingPoints():

    def __init__(self, pos_y=(500, 500)):
        self.color = pygame.Color(0, 0, 0)
        # self.pos1 = self.get_pos1()
        self.pos_y = pos_y

    # def get_pos1(self):
        # pos1 = pygame.mouse.get_pos()
        # print(pos1)
        # return pos1

    def draw_rays(self, surface, pos_x):
        # if self.pos1 == (0, 0):
            # return
        # Must activate when left mouse button is clicked
        pygame.draw.line(surface, self.color, pos_x, self.pos_y, 3)


def main():
    pygame.init()
    pygame.display.set_caption('point perspective tool')
    resolution = (1400, 800)
    screen = pygame.display.set_mode(resolution)
    rays = VanishingPoints((500, 500))
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
        if pygame.mouse.get_pressed()[0] == True:
            rays.draw_rays(screen, pos_x)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()