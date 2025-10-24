import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
class Rect():
    def __init__ (self, x, y ,color, height, width, vx, vy):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        self.width = width
        self.vx = vx
        self.vy = vy
    def display(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.height, self.width))
    def acceleration(self, dt):
        u = self.vy
        self.vy += 2000 * dt
        self.y += (u + self.vy) * 0.5 * dt
        self.x += self.vx * dt
        if self.y > HEIGHT - self.height:
            self.y - HEIGHT - self.height
            self.vy = -self.vy * 0.9
        if self.x > WIDTH - self.width:
            self.vx = -self.vx
        if self.x < self.width:
            self.vx = -self.vx
rect1=Rect(350, 100, (255, 100, 103), 50, 200, 450, 100)
rect2=Rect(100, 150, (126, 200, 255), 200, 80, 100, 500)
clock = pygame.time.Clock()
run = True
while run: 
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            rect1.vy = -1000
            rect2.vy = -1000
    screen.fill("blue")
    rect1.display()
    rect1.acceleration(dt)
    rect2.display()
    rect2.acceleration(dt)
    pygame.display.update()
