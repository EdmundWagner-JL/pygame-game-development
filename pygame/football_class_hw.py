import pygame

WIDTH = 800
HEIGHT = 600


class FootballPlayer:
    def __init__(self, name, position, rating, goals=0, assists=0):
        self.name = name
        self.position = position
        self.rating = rating
        self.goals = goals
        self.assists = assists


    def score_goal(self):
        self.goals += 1

    def make_assist(self):
        self.assists += 1

player1 = FootballPlayer("Kylian Mbappé", "Forward", 91)
player1.score_goal()
player1.make_assist()
print (player1.name)
print (player1.goals)
print (player1.assists)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("sky blue")
    pygame.display.update()
