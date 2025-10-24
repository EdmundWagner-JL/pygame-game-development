import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True

class Circle():
    def __init__ (self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    def grow(self):
        self.radius += 10 
        self.display()
    def move_up(self):
        self.y -= 10
        self.display()
    def move_down(self):
        self.y += 10
        self.display()
    def move_left(self):
        self.x -= 10
        self.display()
    def move_right(self):
        self.x += 10
        self.display()

circle1 = Circle(300, 250, "red", 60)
circle2 = Circle(460, 250, " red", 60)
circle3 = Circle(375, 420, "blue", 50)

while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle1.display()
            circle2.display()
            circle3.display()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            circle1.grow()
            circle2.grow()
            circle3.grow()
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            circle4 = Circle(pos[0], pos[1], "green", 5)
            circle4.display()
            pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                circle1.move_up()
                pygame.display.update()
            if event.key == pygame.K_s:
                circle1.move_down()
                pygame.display.update()
            if event.key == pygame.K_a:
                circle1.move_left()
                pygame.display.update()
            if event.key == pygame.K_d:
                circle1.move_right()
                pygame.display.update()
    screen.fill("sky blue")