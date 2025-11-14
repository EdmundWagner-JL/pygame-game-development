import pygame

WIDTH = 800
HEIGHT = 600
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

lit = pygame.image.load("images\lit_light-removebg-preview.png")
off = pygame.image.load("images\off-light.png")
font = pygame.font.SysFont("Calibri", 50, bold=True, italic=False)
text1 = font.render("on", True, "Black")
text2 = font.render("off", True, "Black")
screen.fill("white")
run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            screen.blit(lit, (0, 0))
            screen.blit(text1,(300, 300))
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            screen.blit(off, (0, 0))
            screen.blit(text2,(300, 300))
            pygame.display.update()



