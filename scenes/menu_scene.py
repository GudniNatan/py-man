import pygame
from scenes.scene import Scene
from utils.pygame_utils import *
from game_objects.demo import Demo
from game_objects.game_object import GameObject
from components.physics import Physics

class MenuScene(Scene):
    def __init__(self, controller):
        super().__init__(controller)
        import sys
        import os 
        connection_path = "fonts/Connection/Connection.otf"
        self.__font = pygame.font.Font(connection_path, 50)
        self.text = self.__font.render("py-Man", True, (255, 255, 255))
        self.text = pad(self.text, (0, 100), (255, 100, 100))
        demo = Demo(self.game_objects, self.text.get_rect(), self.text)
        demo.get_component(Physics).direction = 0.3
        demo.get_component(Physics).speed = 1
        demo.get_component(Physics).bounciness = 1
        background = pygame.Surface(self.screen_rect.size)
        background.fill((20, 20, 20))
        background = GameObject( self.game_objects,
            pygame.Rect(0, 0, 0, 0), background
        )
        crect1 = Rect(self.screen_rect)
        crect1.right = crect1.left
        crect2 = Rect(self.screen_rect)
        crect2.bottom = crect2.top
        crect3 = Rect(self.screen_rect)
        crect3.left = crect3.right
        crect4 = Rect(self.screen_rect)
        crect4.top = crect4.bottom
        collider1 = Demo(self.game_objects, crect1)
        collider2 = Demo(self.game_objects, crect2)
        collider3 = Demo(self.game_objects, crect3)
        collider4 = Demo(self.game_objects, crect4)
        self.game_objects.extend([background, demo, collider1, collider2, collider3, collider4])


    def handle_events(self, events):
        return super().handle_events(events)

    def update(self, ms):
        return super().update(ms)

    def render(self, screen):
        return super().render(screen)