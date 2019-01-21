import pygame
from pygame.sprite import DirtySprite
from components.component import Component


class GameObject(DirtySprite):
    def __init__(self, game_objects, rect: pygame.Rect,
                 image: pygame.Surface = None):
        super().__init__()
        self.rect = rect
        if image:
            rect.size = image.get_rect().size
        else:
            image = pygame.Surface(rect.size)
        self.image = image
        self.area = None
        self.components = dict()
        self.real_x = self.rect.x
        self.real_y = self.rect.y
        self.game_objects = game_objects

    def add_component(self, ComponentClass) -> Component:
        if self.components.get(ComponentClass):
            return self.components[ComponentClass]
        component = ComponentClass(self)
        self.components[ComponentClass] = component
        return component

    def update_pos(self):
        self.rect.x = int(round(self.real_x))
        self.rect.y = int(round(self.real_y))

    def get_component(self, ComponentClass) -> Component:
        if isinstance(ComponentClass, Component):
            ComponentClass = type(ComponentClass)
        try:
            return self.components[ComponentClass]
        except:
            raise TypeError(
                "GameObject", self, "does not have a",
                ComponentClass.__name__,
                "component."
            )

    def update(self, ms):
        for comp in self.components.values():
            comp.update(ms)

    def handle_events(self, events):
        for comp in self.components.values():
            comp.handle_events(events)