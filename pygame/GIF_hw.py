import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
ground = pygame.image.load("images\ground.png")
a_1 = pygame.image.load("frame_01_delay-0.05s.gif")
a_2 = pygame.image.load("frame_04_delay-0.05s.gif")
a_3 = pygame.image.load("frame_07_delay-0.05s.gif")
a_4 = pygame.image.load("frame_10_delay-0.05s.gif")
ground_x = 0
images = [a_1, a_2, a_3, a_4]

class Walk(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = images
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.x = x
        self.y = y
        self.clicked = False
        self.velocity = 0
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
    def update(self):
            self.counter += 1
            if self.counter > 10:
                self.counter = 0
                self.index += 1
                print(self.index)
                if self.index >= 4:
                    self.index = 0
            self.image = self.images[self.index]
Boy_group = pygame.sprite.Group()
Boy = Walk(200, 250)
Boy_group.add(Boy)

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("sky blue")
    screen.blit(ground, (ground_x, 520))
    if run == True:
        ground_x -= 0.2
        if abs(ground_x) > 35:
            ground_x = 0
    Boy_group.update()
    Boy_group.draw(screen)
    pygame.display.update()
