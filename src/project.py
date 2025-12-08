import pygame


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
        zone = pygame.Rect(109, 101, 1252, 614)
        return zone

    def _create_area(self, surface):
        # testing
        pygame.draw.rect(surface, (255, 0, 0), self.collision)
    
    def draw_point(self, surface, pos):
        # Must activate when right mouse button is clicked, max three times
        for n in pos:
            rect = self.rays.get_rect(center=n)
            if not self.collision.collidepoint(n):
                return
            else:
                surface.blit(self.rays, rect)


class SaveFile():

    def __init__(self, canvas):
        self.area = canvas
        self.clicked = False

    def save(self, surface):
        area = surface.subsurface(self.area)
        pygame.image.save(area, "point-perspective-guidelines.png")
        print('Image saved to src folder.')


class Rectangle():

    def __init__(self, x=210, y=200, width=1050, height=410):
        self.button_zone = self.collision_box()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.frame = self.rectangle()
        self.pixels = 10 # pixels per key press
        self.sub_pixels = 30 # pixels per key press
        self.clicked = False

    # button
    def collision_box(self):
        # collision image
        zone = pygame.Rect(28, 132, 53, 53)
        return zone
    
    def _create_area(self, surface):
        # testing
        pygame.draw.rect(surface, (255, 0, 0), self.button_zone)
            
    def detect_click(self, pos_x):
        shown = False
        if self.button_zone.collidepoint(pos_x):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                shown = True
                self.clicked = True
        return shown
    
    # rectangle
    def rectangle(self):
        rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        return rectangle
    
    def move_keys(self, event):
        # arrow keys
        if event.key == pygame.K_UP:
            self.frame.y -= self.pixels
        elif event.key == pygame.K_DOWN:
            self.frame.y += self.pixels
        elif event.key == pygame.K_LEFT:
            self.frame.x -= self.pixels
        elif event.key == pygame.K_RIGHT:
            self.frame.x += self.pixels
    
    def shrink_keys(self, event):
        # arrow keys + cmd 
        if event.key == pygame.K_UP and pygame.key.get_mods() and \
                        pygame.KMOD_META:
            self.shrink(0, -self.sub_pixels)
        elif event.key == pygame.K_DOWN and pygame.key.get_mods() and \
                        pygame.KMOD_META:
            self.shrink(0, self.sub_pixels)
        elif event.key == pygame.K_LEFT and pygame.key.get_mods() and \
                        pygame.KMOD_META:
            self.shrink(-self.sub_pixels, 0)
        elif event.key == pygame.K_RIGHT and pygame.key.get_mods() and \
                        pygame.KMOD_META:
            self.shrink(self.sub_pixels, 0)
    
    def shrink(self, x, y):
        self.frame.inflate_ip(x, y)
        self.frame.width = max(0, self.frame.width)
        self.frame.height = max(0, self.frame.height)
    
    def update_rectangle(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.frame, 3)


def main():
    pygame.init()
    pygame.display.set_caption('point perspective tool')
    resolution = (1470, 816)
    screen = pygame.display.set_mode(resolution)
    # items
    min_clicks = 0
    max_clicks = 3
    pos = []
    rectangle_visible = False
    # classes
    rays = VanishingPoints()
    save_canvas = SaveFile(rays.collision_box())
    rectangle = Rectangle()
    # game
    running = True
    while running:
        # Program Event Loop
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[2] == True:
                    if min_clicks < max_clicks:
                        pos.append(pos_x)
                        min_clicks += 1
                        # stops right clicking entirely after 3 clicks
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and pygame.key.get_mods() and \
                                pygame.KMOD_META:
                    save_canvas.save(screen)
                rectangle.shrink_keys(event)
                rectangle.move_keys(event)
            elif event.type == pygame.QUIT:
                running = False
        # Program Logic
        color = pygame.Color(174, 166, 166)
        # Render & Display
        screen.fill(color)
        try:
            rays.draw_point(screen, pos)
            if rectangle.detect_click(pos_x):
                rectangle_visible = True
        except UnboundLocalError:
            pass
        if rectangle_visible:
            rectangle.update_rectangle(screen)
        border = pygame.image.load('assets/border.png').convert_alpha()
        screen.blit(border, (0, 0))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()