import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Rect():
    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def display(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, key):
        if key[pygame.K_LEFT]:
            self.x -= 1
        if key[pygame.K_RIGHT]:
            self.x += 1
        if key[pygame.K_UP]:
            self.y -= 1
        if key[pygame.K_DOWN]:
            self.y += 1


        if self.x < self.width:
            self.x = self.width
        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width
        if self.y < self.height:
            self.y = self.height
        if self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height


        if self.x > 400:
            self.color = (255, 0, 0)
        elif self.x < 200:
            self.color = (0, 0, 255)
        elif self.y < 200:
            self.color = (0, 255, 0)
        elif self.y > 400:
            self.color = (255, 255, 0)
        else:
            self.color = (150, 150, 150)

player = Rect(200, 100, (150, 150, 150), 60, 60)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    player.move(keys)

    screen.fill((0, 0, 0))
    player.display()
    pygame.display.update()
