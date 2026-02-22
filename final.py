"""
Rpg story Boss fight
    - Start in main screen (title)
    - Settings, leaderboard, play
    - 
"""
import pygame
from classes import Text, Button, Player, Background


screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

def start():
    title = Text(screen,"The Apocalypse",10,(50, 168, 82),600,200 )
    startIMG = pygame.image.load("mainScreen.png")
    start = Background(screen,startIMG,1,600,400)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        start.draw()
        
        pygame.display.update()
        clock.tick(60)

start()