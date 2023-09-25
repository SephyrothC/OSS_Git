import pygame, time, random

#def of the game window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zelda 1 : Survival game")

BackGround = 

def main():
    run = True
    while run : #run the game
        for event in pygame.event.get() :
            if event.type == pygame.QUIT : #if the exit cross is clicked the game just cole himself
                run = False
                break

    pygame.quit()


if __name__ == '__main__':
    main()