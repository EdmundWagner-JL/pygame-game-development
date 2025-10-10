import pygame

WIDTH = 800
HEIGHT = 600

class Circle():
    def __init__ (self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

circle1 = Circle(300, 250, "red", 60)
circle2 = Circle(460, 250, " red", 60)
circle3 = Circle(375, 420, "blue", 50)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("sky blue")
    circle1.display()
    circle2.display()
    circle3.display()
    pygame.display.update()

