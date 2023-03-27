import pygame
import molkat_mania

# Initialize pygame
pygame.init()
pygame.font.init()

# Set the dimensions of the window
width = 1280
height = 960

# Create a window
screen = pygame.display.set_mode((width, height))

# Clock
clock = pygame.time.Clock()

# Set the title of the window
pygame.display.set_caption("Molkat Mania")

# Run the game loop
while True:

    #fill the screen with white
    screen.fill((255, 255, 255))

    molkat_mania.tick(screen)
    # Makes screen work
    pygame.display.flip()
    clock.tick(60)