import pygame
import Scenes

#general object type for something that you can draw on the screen
class GameObject():
    def __init__(self) -> None:
        self.position = [0,0]
        self.velocity_x = 0
        self.velocity_y = 0

    def tick(self):
        self.position[0] += self.velocity_x
        self.position[1] += self.velocity_y

    def render(self, screen):
        pass

class Player(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.speed = 10 

    def render(self,screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.position[0], self.position[1], 100, 100))

#define player
player = Player()

#current scene
current_scene = Scenes.Scene()
current_scene.scene_objects.append(player)

def tick(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        #register keys
        if event.type == pygame.KEYDOWN:
            #simple movement
            if event.key == pygame.K_w:
                player.velocity_y -= player.speed
            if event.key == pygame.K_a:
                player.velocity_x -= player.speed
            if event.key == pygame.K_s:
                player.velocity_y +=  player.speed
            if event.key == pygame.K_d:
                player.velocity_x += player.speed

        if event.type == pygame.KEYUP:
            #simple movement
            if event.key == pygame.K_w:
                player.velocity_y += player.speed
            if event.key == pygame.K_a:
                player.velocity_x += player.speed
            if event.key == pygame.K_s:
                player.velocity_y -=  player.speed
            if event.key == pygame.K_d:
                player.velocity_x -= player.speed
 

    #tick gameobjects
    for gameobject in current_scene.scene_objects:
        gameobject.tick()

    #render Scene
    current_scene.render(screen)

    #render gameobjects
    for gameobject in current_scene.scene_objects:
        gameobject.render(screen)            
    