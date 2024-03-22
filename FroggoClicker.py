import pygame
import random
import sys
import os
import time

# initialize Pygame
pygame.init()

# size of screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frog Spawner!")

# colors
COLOR = (129, 15, 233)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (218,165,32)

# froggos
frog_images = [
    pygame.image.load('frog1.png'),
    pygame.image.load('frog2.png'),
    pygame.image.load('frog3.png'),
    pygame.image.load('frog4.png'),
    pygame.image.load('frog5.png'),
    pygame.image.load('frog6.png'),
    pygame.image.load('frog7.png'),
    pygame.image.load('frog8.png'),
    pygame.image.load('frog9.png'),
    pygame.image.load('frog10.png')
]

# frog class
class Frog(pygame.sprite.Sprite):

    # this means, define a class method constructor which takes in one parameter; itself 
    # meaning initalizers are set it itself
    def __init__(self):

        # need to provide super here to call proper Sprite class initalizers
        super().__init__()
        self.image = random.choice(frog_images)

         # everytime this class is called, a new scalar is provided
        random_scalar = random.randint(1, 5)
        self.image = pygame.transform.scale(self.image, (random_scalar * 50, random_scalar * 50))

        # need this to properly spawn in frogs at random locations
        # frog is 'bounded' by a rectangular box
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))

# need this to add a frog to the current amount of frogs displayed
# not really sure how this works
all_sprites = pygame.sprite.Group()

# counter and message
counter = 0
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

# running the game
running = True
while running:

    # sets background color
    screen.fill(COLOR)

    # when pressing "X", it'll quit the infinite loop & game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # if the mouse or any of the keys are pressed, a new frog is made at a random location
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                frog = Frog()
                # adds random frog
                all_sprites.add(frog)
                counter += 1

    # spawn the frogs
    all_sprites.draw(screen)

    # show the current counter
    counter_text = font.render(f"Frogs: {counter}", True, BLACK)
    # blit draws content needed to be shown on screen
    screen.blit(counter_text, (10, 10))

    # counter rewards
    if counter == 10:
        message_text = big_font.render("Wow, you've spawned 10 frogs!", True, WHITE)
        screen.fill(BLACK)
        pygame.display.flip()
        screen.blit(message_text, (SCREEN_WIDTH // 2 - message_text.get_width() // 2, SCREEN_HEIGHT // 2))
    elif counter == 50:
        message_text = big_font.render("You're on fire! 50 frogs already!", True, WHITE)
        screen.fill(BLACK)
        pygame.display.flip()
        screen.blit(message_text, (SCREEN_WIDTH // 2 - message_text.get_width() // 2, SCREEN_HEIGHT // 2))
    elif counter == 100:
        message_text = big_font.render("I think that's enough frogs..", True, WHITE)
        screen.fill(BLACK)
        pygame.display.flip()
        screen.blit(message_text, (SCREEN_WIDTH // 2 - message_text.get_width() // 2, SCREEN_HEIGHT // 2))
    elif counter == 200:
        message_text = big_font.render("Please stop!", True, WHITE)
        screen.fill(BLACK)
        pygame.display.flip()
        screen.blit(message_text, (SCREEN_WIDTH // 2 - message_text.get_width() // 2, SCREEN_HEIGHT // 2))

    # flip shows the content on the screen
    pygame.display.flip()

pygame.quit()
sys.exit()
