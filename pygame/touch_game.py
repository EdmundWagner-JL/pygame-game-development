import pygame

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

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
        
player = Rect (100, 100, (235, 44, 30), 80, 80)
green = Rect (350, 350, (152, 255, 92), 40, 40)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("sky blue")
    
    
    keys = pygame.key.get_pressed()
    green.display()
    player.display()
    player.move(keys)
    pygame.display.update()