import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
sky = pygame.image.load("images\sky.png")
ground = pygame.image.load("images\ground.png")
bird1 = pygame.image.load("images\Flap1.png")
bird2 = pygame.image.load("images\Flap2.png")
bird3 = pygame.image.load("images\Flap3.png")
images = [bird1, bird2, bird3]
ground_x = 0
game = True
run = True
flying = False
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = images
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
    def update(self):
        self.counter += 1
        if self.counter > 10:
            self.counter = 0
            self.index += 1
            if self.index >= 3:
                self.index = 0
        self.image = self.images[self.index]
Bird_group = pygame.sprite.Group()
Flappy = Bird(200, 250)
Bird_group.add(Flappy)
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and flying == False and game == True:
                flying = True
    screen.blit(sky, (0, -120))
    screen.blit(ground, (ground_x, 520))
    Bird_group.draw(screen)
    Bird_group.update()
    if game == True:
        ground_x -= 0.4
        if abs(ground_x) > 35:
            ground_x = 0
    pygame.display.update()