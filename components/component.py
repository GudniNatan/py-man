from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, game_object):
        self.game_object = game_object

    @abstractmethod
    def update(self, ms):
        pass