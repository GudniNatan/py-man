from abc import ABC, abstractmethod
import pygame


class Scene(ABC):
    def __init__(self, controller):
        self.__controller = controller
        self.__last_scene = controller.get_scene()
        self.game_objects = pygame.sprite.LayeredUpdates()
        self.screen_rect = pygame.display.get_surface().get_rect()

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self, ms):
        self.game_objects.update(ms)

    @abstractmethod
    def render(self, screen):
        return self.game_objects.draw(screen)

    def load(self):
        pass
