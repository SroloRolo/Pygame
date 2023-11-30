import pygame
import time
import random

WIDTH, HEIGHT = 1000,800 #pixels
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #window
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT)) #creating and scaling background

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

#loading the image into the game
def draw(player):
    WIN.blit(BG,(0, 0))

    pygame.draw.rect(WIN,(158, 100, 0), player)
    pygame.display.update()

#game loop
def main():
    run = True

    #moving a character
    player =pygame.Rect(500, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    # closing the game
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(player)

    pygame.quit()

#making sure that we are directly running this python file and not importing it
if __name__ == "__main__":
    main()