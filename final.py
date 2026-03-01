"""
Rpg story Boss fight
    - Start in main screen (title)
    - Settings, leaderboard, play
    - 
Repo: https://github.com/AndrewPal04/The-Apocalypse
"""
import pygame
from classes import Text, Button, Player, Background
pygame.init()

screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

def main():
    #objects
    desertIMG = pygame.image.load("firstPage.png")
    desert = Background(screen,desertIMG,0.7,500,300)
    sprite_group = pygame.sprite.Group()
    playerIMG = pygame.image.load("mainCharacter.png")
    player = Player(playerIMG,0.4,500,300)
    sprite_group.add(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #workspace
        desert.draw()
        sprite_group.draw(screen)

        pygame.display.update()
        clock.tick(60)

def start():
    # objects
    title = Text(screen, "The Apocalypse", 100, (123,133,127), 500, 130)
    startIMG = pygame.image.load("mainScreen.png")
    start = Background(screen,startIMG,0.7,500,300)
    # Button
    playIMG = pygame.image.load("playbtn.png")
    play=Button(screen,playIMG,1, 500, 300)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # workspace
        start.draw()
        title.draw()
        if play.draw():
            main()

        pygame.display.update()
        clock.tick(60)

start()

"""
Homework
For homework, I want you to continue working on the
first screen after the start screen, where the player will
show up to the user for the first time. I also want you to
make the player able to move around using either arrows, or
WASD. Try to find some pictures for zombie sprites you want
to add in later as well!
Good Luck!
"""


"""
Instructions:
go to https://github.com/AndrewPal04/The-Apocalypse
hit code, and then hit download so you can create a copy
of the entire code, and all the pictures

"""