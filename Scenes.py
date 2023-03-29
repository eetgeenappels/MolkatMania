import pygame
import random

grasspng1 = pygame.transform.scale(pygame.image.load("Textures/Grass texture.png"), (96, 96))
grasspng2 = pygame.transform.scale(pygame.image.load("Textures/Grass texture2.png"), (96, 96))
grasspng3 = pygame.transform.scale(pygame.image.load("Textures/Grass texture3.png"), (96, 96))

#Base scene objects
class Scene:
    def __init__(self) -> None:
        self.scene_objects = []

        self.grassmap = []
        for x in range(0,20):
            self.grassmap.append([])
            for y in range (0, 20):
                randompng = random.randint(0,2)
                if randompng == 0:
                    self.grasspng = grasspng1
                if randompng == 1:
                    self.grasspng = grasspng2
                if randompng == 2:
                    self.grasspng = grasspng3
                self.grassmap[x].append(self.grasspng)
    
    def render(self, screen: pygame.Surface):
        for i in range(0,20):
            pygame.draw.aaline(screen, (0, 0, 0), (i*100, 0), (i*100, 960))
        for i in range(0,20):
            pygame.draw.aaline(screen, (0, 0, 0), (0, i*100), (1280, i*100))
        for x in range(0,20):
            for y in range(0,20):
                screen.blit(self.grassmap[x] [y], (x*96, y*96))