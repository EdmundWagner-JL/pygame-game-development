import pygame
import time
pygame.init()
pygame.mixer.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday")
card = pygame.image.load("images\happy_birthday.jpg")
card = pygame.transform.scale(card, (800,600))
#card = pygame.transform.rotate(card, 90)
present = pygame.image.load("images\open_present.jpg")
present = pygame.transform.scale(present, (300, 300))
cake = pygame.image.load("images\cake.jpg")
cake = pygame.transform.scale(cake, (300, 300))
font = pygame.font.SysFont("Calibri", 50, bold=True, italic=False)
text1 = font.render("HAPPY BIRTHDAY", True, "Black")
font2 = pygame.font.SysFont("Arial", 30, bold=False, italic=True)
text2 = font.render("To you", True, (66, 38, 38))
#celebrate = pygame.mixer.Sound("sounds\level-up-04-243762.mp3")
pygame.mixer.music.load("sounds\level-up-04-243762.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("sky blue")
    #celebrate.play()
    screen.blit(card, (0,0))
    screen.blit(text1, (240, 150))
    pygame.display.update()
    time.sleep(2)
    screen.blit(present, (0,300))
    screen.blit(text2, (330, 250))
    pygame.display.update()
    time.sleep(2)
    screen.blit(cake, (500,300))
    pygame.display.update()
    pygame.display.update()
    time.sleep(2)
