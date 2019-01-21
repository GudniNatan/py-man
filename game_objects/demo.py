import pygame
from game_objects.game_object import GameObject
from components.components import Physics


class Demo(GameObject):
    def __init__(self, game_objects, rect: pygame.Rect,
                 surface: pygame.Surface = None):
        super().__init__(game_objects, rect, surface)
        self.add_component(Physics)
        self.components[Physics].speed = 0
