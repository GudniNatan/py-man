from abc import ABC, abstractmethod
import pygame


class Scene(ABC):
    def __init__(self, controller):
        self.__controller = controller
        self.__last_scene = controller.get_scene()
        self.game_objects = list()
        self.screen_rect = pygame.display.get_surface().get_rect()

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self, ms):
        for g_obj in self.game_objects:
            g_obj.update(ms)

    @abstractmethod
    def render(self, screen):
        blits = [g_obj.get_blit() for g_obj in self.game_objects]
        screen.blits(blits)

    def load(self):
        pass
