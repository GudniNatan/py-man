from abc import ABC, abstractmethod
import pygame
from pygame.sprite import LayeredUpdates, groupcollide
from utils.pygame_utils import fix_path


class Scene(ABC):
    REGULAR_FONT = "fonts/Connection/Connection.otf"
    BOLD_FONT = "fonts/Connection/ConnectionBold.otf"

    def __init__(self, controller):
        self.__controller = controller
        self.__last_scene = controller.get_scene()
        self.game_objects = LayeredUpdates()
        self.screen_rect = pygame.display.get_surface().get_rect()
        try:
            open(self.REGULAR_FONT).close()
        except FileNotFoundError:
            fix_path()

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self, ms):
        game_objects = self.game_objects
        game_objects.update(ms)
        collisions = groupcollide(game_objects, game_objects, False, False)
        for key, value in collisions.items():
            value.pop(0)
            if value:
                key.collide(value)

    @abstractmethod
    def render(self, screen):
        return self.game_objects.draw(screen)

    def load(self):
        pass