"""
Rpg story Boss fight
    - Start in main screen (title)
    - Settings, leaderboard, play
    - 
Repo: https://github.com/AndrewPal04/The-Apocalypse
"""
import pygame, time, random
from classes import Text, Button, Player, Background, Zombie
pygame.init()

screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()


def policeGun():
    pygame.mixer.init()
    pygame.mixer.music.load("shot.mp3")
    desertIMG = pygame.image.load("sand.png")
    desert = Background(screen,desertIMG,0.7,500,300)
    sprite_group = pygame.sprite.Group()
    playerIMG = pygame.image.load("characterG.png")
    zombieIMG1 = pygame.image.load("zombie1.png")
    player = Player(playerIMG,0.08,100,300)
    zombies = [
        Zombie(screen,zombieIMG1,0.165,1100,random.randint(50,550)),
        Zombie(screen,zombieIMG1,0.165,1200,random.randint(50,550)),
        Zombie(screen,zombieIMG1,0.165,1050,random.randint(50,550)),
        Zombie(screen,zombieIMG1,0.165,1150,random.randint(50,550))
    ]
    sprite_group.add(player)
    texts =[
        Text(screen, "Woah a Gun...I wonder what its used for?", 40, (0,0,0), 500, 500),
        Text(screen, "Lets move on and find help", 35, (0,0,0), 500, 500)
    ]
    start = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        end = time.time()
        #workspace
        desert.draw()
        sprite_group.draw(screen)
        #draw texts with if statements, and draw player on screen, and player.update() after
        if end-start < 3:
            texts[0].draw()
        elif end-start < 5:
            texts[1].draw()
        else:
            player.update()
            for i in range(len(zombies)):
                if zombies[i].alive:
                    zombies[i].update(player)
                    zombies[i].draw()
        keystate = pygame.key.get_pressed()

        #shoot
        if keystate[pygame.K_SPACE]:
            pygame.mixer.music.play()
            for i in range(len(zombies)):
                if abs(player.rect.y - zombies[i].rect.y) < 20:
                    zombies[i].alive = False
        
        numZombies = 0
        for i in range(len(zombies)):
            if zombies[i].alive:
                numZombies +=1
        if numZombies == 0:
            for i in range(len(zombies)):
                zombies[i].alive = True
                zombies[i].rect.x = random.randint(1050, 1300)
                zombies[i].rect.y = random.randint(50, 550)


        
        if player.rect.right >=300:
            player.rect.right = 300
        
        
        pygame.display.update()
        clock.tick(60)


def main():
    #objects
    desertIMG = pygame.image.load("firstPage.png")
    desert = Background(screen,desertIMG,0.7,500,300)
    sprite_group = pygame.sprite.Group()
    playerIMG = pygame.image.load("mainCharacter.png")
    player = Player(playerIMG,0.25,500,300)
    sprite_group.add(player)
    # Gun
    gun_png = pygame.image.load("gun.png")
    gun = Background(screen,gun_png,0.14,800,150)
    

    texts =[
        Text(screen, "Hmm.. What is this place?", 40, (0,0,0), 500, 500),
        Text(screen, "This seem to be some kind of abondoned village", 35, (0,0,0), 500, 500),
        Text(screen, "Lets Explore and maybe find a weapon or perhaps help?", 32, (0,0,0), 500, 500)
    ]
    start = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #workspace
        desert.draw()
        end = time.time()
        if end-start < 3:
            texts[0].draw()
        elif end-start < 7:
            texts[1].draw()
        elif end-start < 11:
            texts[2].draw()
        else:
            player.update()
            
        gun.draw()
        if pygame.sprite.collide_rect(player, gun):
            screen.fill((0,0,0))
            pygame.display.update()
            time.sleep(2)
            policeGun()
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
For homework I want you to Change the images for some of the zombies, so there
are more types. Also, find an image for the barrier you wanted to add into the game
where the zombies will stop. Currently, the zombies can also spawn in
50 - 550, but the user can't hit them if they spawn too low or too high. Make it so they
can't spawn outside of where the user can hit them.
Good Luck!
"""


"""
Instructions:
go to https://github.com/AndrewPal04/The-Apocalypse
hit code, and then hit download so you can create a copy
of the entire code, and all the pictures
"""