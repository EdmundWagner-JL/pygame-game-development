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

base = Rect(200, 100, "brown", 400, 400)
window1 = Rect(250, 200, (66, 135, 245), 120, 80)
window2 = Rect(450, 200, (66, 135, 245), 120, 80)
door = Rect (350, 350, (97, 44, 0), 80, 150)
        
run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("sky blue")
    base.display()
    window1.display()
    window2.display()
    door.display()
    pygame.display.update()

