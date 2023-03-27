import pygame
import molkat_mania

# Initialize pygame
pygame.init()
pygame.font.init()

# Set the dimensions of the window
width = 800
height = 800

# Create a window
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Hello")

# Run the game loop
running = True
while running:

    molkat_mania.tick(screen)