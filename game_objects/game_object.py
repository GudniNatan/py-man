import pygame
from components.component import Component


class GameObject(object):
    def __init__(self, game_objects, rect: pygame.Rect,
                 surface: pygame.Surface = None):
        self.rect = rect
        if surface:
            rect.size = surface.get_rect().size
        else:
            surface = pygame.Surface(rect.size)
        self.surface = surface
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
                "GameObject does not have a",
                ComponentClass.__name__,
                "component."
            )

    def update(self, ms):
        for comp in self.components.values():
            comp.update(ms)

    def get_blit(self):
        blitinfo = [self.surface, self.rect.topleft]
        if self.area:
            blitinfo.append(self.area)
        return blitinfo