import pygame
import time
import random
import sys
pygame.font.init() #initialize the font module

#screen size
WIDTH, HEIGHT = 1000,800 #pixels
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #window
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT)) #creating and scaling background

#player size
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 10
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30) #creating a font object

#loading the image into the game
def draw(player, elapsed_time, stars):
    WIN.blit(BG,(0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN,("yellow"), player) #158, 100, 0

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()

#game loop
def main():
    run = True

    #moving a character
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock() #creating a clock object
    start_time = time.time() #stroring current time
    elapsed_time = 0

    star_add_increment = 2000 #1st star will be every 2s
    star_count = 0 #variable that tells us when we should add a next star

    stars = [] #storing stars that are on the screen
    hit = False

    #closing the game
    while run:
        #delying the while loop so it moves 60times per second (frames per second)
        star_count += clock.tick(60) #it makes the speed the same on all computers
        #calculating how many milisec has passed since the last clock tick


        elapsed_time = time.time() - start_time #number of s that has elapsed since the gamr started

        if star_count > star_add_increment: #if 2000milisec has passed we add a new star
            for i in range(random.randint(0,4)):  #generating 3 stars at a time
                #randomly positioning it on the screen
                star_x = random.randint(0, WIDTH - STAR_WIDTH) #returning a ranom no between 0 and the end of a screen
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT) #starting at the top and moving down
                stars.append(star) #append adds additional elements to the end of a list star[]

            star_add_increment = max(200, star_add_increment - 50) #in every iteration the star moves faster
            star_count = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        #getting all the keys that the user has pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        elif key[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        elif key[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        elif key[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            #removing stars when they are off screen
            if star.y > HEIGHT:
                stars.remove(star)
            #another ver 'star.y >= player.y' only if the player is at the bottom
            elif star.colliderect(player): #colliderect tells us if 2 rectangles have collide
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(3000)
            break





        draw(player, elapsed_time, stars)

    pygame.quit()

#making sure that we are directly running this python file and not importing it
if __name__ == "__main__":
    main()