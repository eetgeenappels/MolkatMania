import pygame
import contants

#Base scene objects
class Scene:
    def __init__(self) -> None:
        self.scene_objects = []
    
    def render(self, screen):
        for i in range(0,20):
            pygame.draw.aaline(screen, (0, 0, 0), (i*100, 0), (i*100, contants.screen_height))
        for i in range(0,20):
            pygame.draw.aaline(screen, (0, 0, 0), (0, i*100), (contants.screen_width, i*100))