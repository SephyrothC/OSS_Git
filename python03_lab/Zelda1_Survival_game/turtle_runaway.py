import pygame, time, random
import botton

pygame.font.init() #initialize font module

#def of the game window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zelda 1 : Survival game")

#def the player
Player_Width = 40
Player_Height = 60
Player_position = (WIDTH/2-Player_Width, HEIGHT/2-Player_Height)
Player_Velocity = 6

#def the enemy
Enemy_Width = 20
Enemy_Height = 30
Enemy_Velocity = 1

#load the background
BackGround_Game = pygame.transform.scale(pygame.image.load("python03_lab\Zelda1_Survival_game\Sprites\BG.png"), (WIDTH, HEIGHT))
Background_Menu = pygame.transform.scale(pygame.image.load("python03_lab\Zelda1_Survival_game\Sprites\MENU.png"), (WIDTH, HEIGHT))

#load botton
Play_img = pygame.image.load("python03_lab\Zelda1_Survival_game\Sprites\Play_Botton.png").convert_alpha()
Score_img = pygame.image.load("python03_lab\Zelda1_Survival_game\Sprites\Score_Botton.png").convert_alpha()
Quit_img = pygame.image.load("python03_lab\Zelda1_Survival_game\Sprites\Quit_Botton.png").convert_alpha()

#create botton
x = pygame.Surface.get_width(Play_img) #all bottons have the same size
y = pygame.Surface.get_height(Play_img) #all bottons have the same size
Play_Botton = botton.Button(WIDTH/2 - x/4, HEIGHT/2 - y/5 , Play_img, 1/2)
Score_Botton = botton.Button(WIDTH/2 - x/4, HEIGHT/2 + y/3, Score_img, 1/2)
Quit_Botton = botton.Button(WIDTH/2 - x/4, HEIGHT - y/2 , Quit_img, 1/2)




#def Font 
FONT = pygame.font.SysFont("comicsans", 30)

#Managing the display
def draw(player, elapsed_time, enemies):
    #Background
    WIN.blit(BackGround_Game, (0,0))

    #Player
    pygame.draw.rect(WIN, "red", player)

    #Enemies
    for enemy in enemies[:] :
        pygame.draw.rect(WIN, "blue", enemy)

    #Time
    time_text = FONT.render(f"Time : {round(elapsed_time)}s", 1 , "white")
    WIN.blit(time_text, (10,10))

    pygame.display.update()

def Menu():
    menu_load = True
    while menu_load :
        #draw background
        WIN.blit(Background_Menu, (0,0))

        #draw bottons
        Play_Botton.draw(WIN)
        Score_Botton.draw(WIN)
        Quit_Botton.draw(WIN)

        if Play_Botton.clicked :
            menu_load = False

        if Quit_Botton.clicked :
            pygame.quit()

        #Set a exit point
        for event in pygame.event.get() :
            if event.type == pygame.QUIT : #if the exit cross is clicked the game just cole himself
                pygame.quit()
                break
        

        
        pygame.display.update()
        



def main():
    
    #game statement
    hit = False
    run = True
    load_menu = True
    

    #def a clock
    clock = pygame.time.Clock()

    #Current time 
    start_time = time.time()
    elapsed_time = 0

    #create a player
    player = pygame.Rect(Player_position[0], Player_position[1], Player_Width, Player_Height)

    #create a enemy
    enemy_add_incresement = 2000
    enemy_count = 0
    enemy_dificulty = 2

    enemies = []
    

    while run : #run the game

        if load_menu :
            #start the menu
            Menu()
            load_menu = False

            #restart player
            player = pygame.Rect(Player_position[0], Player_position[1], Player_Width, Player_Height)

            #restart time
            start_time = time.time()

            #restart enemies
            enemy_add_incresement = 2000
            enemy_count = 0
            enemy_dificulty = 2
            enemies = []

        #Set a clock tick and count for add enemies
        enemy_count += clock.tick(60)


        #Calculate elapsed time
        elapsed_time = time.time() - start_time
        
        #adding some enemy with a difficulty systeme
        if enemy_count > enemy_add_incresement :
            for _ in range(random.randint(1, enemy_dificulty)) : 

                start_enemy_pose = random.randint(1,4) #chose one corner

                if(start_enemy_pose == 1) : #top
                    enemy_y = -Enemy_Height
                    enemy_x = random.randint(0, WIDTH - Enemy_Width)
                    enemy = pygame.Rect(enemy_x, enemy_y, Enemy_Width, Enemy_Height) #create a new enemy
                    enemies.append(enemy) #add the enemy to the enemies list

                if(start_enemy_pose == 2) : #right
                    enemy_y = random.randint(0, HEIGHT - Enemy_Height)
                    enemy_x = WIDTH + Enemy_Width
                    enemy = pygame.Rect(enemy_x, enemy_y, Enemy_Width, Enemy_Height) #create a new enemy
                    enemies.append(enemy) #add the enemy to the enemies list

                if(start_enemy_pose == 3) : #bottom
                    enemy_y = HEIGHT + Enemy_Height
                    enemy_x = random.randint(0, WIDTH - Enemy_Width)
                    enemy = pygame.Rect(enemy_x, enemy_y, Enemy_Width, Enemy_Height) #create a new enemy
                    enemies.append(enemy) #add the enemy to the enemies list

                if(start_enemy_pose == 4) : #left
                    enemy_y = random.randint(0, HEIGHT - Enemy_Height)
                    enemy_x = -Enemy_Width
                    enemy = pygame.Rect(enemy_x, enemy_y, Enemy_Width, Enemy_Height) #create a new enemy
                    enemies.append(enemy) #add the enemy to the enemies list

            enemy_add_incresement = max(200, enemy_add_incresement - 10) #augment the speed of the enemy spawn
            enemy_dificulty = min(8, enemy_dificulty+random.randint(0, 1)) #add more dificulty
            enemy_count = 0 #reset count 



        #Set a exit point
        for event in pygame.event.get() :
            if event.type == pygame.QUIT : #if the exit cross is clicked the game just cole himself
                run = False
                break
        
        #Get the player key press and set deplacement 
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and player.x - Player_Velocity >= 0:
            player.x -= Player_Velocity
        elif key[pygame.K_RIGHT] and player.x + Player_Velocity + Player_Width <= WIDTH:
            player.x += Player_Velocity
        elif key[pygame.K_DOWN] and player.y + Player_Velocity + Player_Height <= HEIGHT:
            player.y += Player_Velocity
        elif key[pygame.K_UP] and player.y - Player_Velocity >= 0:
            player.y -= Player_Velocity

        #Pause game
        if key[pygame.K_ESCAPE] :
            load_menu = True

        #Add the enemy deplacement 
        for enemy in enemies[:] :
            check_x = ((player.x+(player.width/2)) - (enemy.x+((enemy.width)/2)) ) 
            check_y = ((player.y+(player.height/2)) - (enemy.y+((enemy.height)/2)) ) 
            check = min(check_x, check_y)
            if check == 0  and check_x == 0 : check = check_y
            if check == 0  and check_y == 0 : check = check_x
            if check == check_y :
                enemy.y += (check/abs(check))*Enemy_Velocity
            elif check == check_x :
                enemy.x += (check/abs(check))*Enemy_Velocity


            if enemy.colliderect(player):
                enemies.remove(enemy)
                hit = True
                break
        
        if hit:
            lost_text = FONT.render(f"You lost!   Time : {round(elapsed_time)}s" , 1 , "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, enemies) #draw the background, player, time elapsed

    pygame.quit()


if __name__ == '__main__':
    main()