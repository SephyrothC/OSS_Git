import pygame, time, random

#def of the game window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zelda 1 : Survival game")

#def the player
Player_Width = 40
Player_Height = 60
Player_position = (WIDTH/2-Player_Width, HEIGHT/2-Player_Height)
Player_Velocity = 5

#def of the background
BackGround = pygame.transform.scale(pygame.image.load("python03_lab\Zelda1_Survival_game\Sprites\BG.png"), (WIDTH, HEIGHT))

#Managing the display
def draw(player):
    #Background
    WIN.blit(BackGround, (0,0))

    #Player
    pygame.draw.rect(WIN, "red", player)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(Player_position[0], Player_position[1], Player_Width, Player_Height)

    while run : #run the game
        for event in pygame.event.get() :
            if event.type == pygame.QUIT : #if the exit cross is clicked the game just cole himself
                run = False
                break
        
        #Get the player key press
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] :
            player.x -= Player_Velocity

        draw(player) #draw the background

    pygame.quit()


if __name__ == '__main__':
    main()