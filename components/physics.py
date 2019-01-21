import pygame
from components.component import Component
from math import atan2, sin, cos


class Physics(Component):
    BASE_SPEED = 1 / 10

    def __init__(self, game_object):
        super().__init__(game_object)
        self.weight = None
        self.bounciness = 0.0
        self.collision = True
        self.direction = 0.0
        self.speed = 0.0
        self.gravity = False
        self.friction = -0.1
        self.rect = self.game_object.rect

    def update(self, ms):
        self.move(ms)
        self.detect_collision(ms)

    def move(self, ms):
        dist = ms * self.BASE_SPEED * self.speed
        dx = sin(self.direction) * dist
        dy = cos(self.direction) * dist
        self.game_object.real_x += dx
        self.game_object.real_y += dy
        self.game_object.update_pos()
        if self.friction:
            self.speed = self.speed * (1 - (self.friction * ms / 1000))

    def _handle_collision(self, other, ms):
        my_rect = self.rect
        other_rect = other.rect
        dist = ms * self.BASE_SPEED * self.speed
        clip = pygame.Rect.clip(my_rect, other_rect)
        direction = atan2(
            my_rect.centerx - clip.centerx, my_rect.centery - clip.centery
        )
        if self.bounciness == 0:
            self._correct(ms, direction, dist)
        else:
            self._bounce(ms, direction)

    def _bounce(self, ms, direction):
        x = (sin(direction) + sin(self.direction)) / 2
        y = (cos(direction) + cos(self.direction)) / 2
        self.direction = atan2(x, y)
        self.speed *= self.bounciness
        self.move(ms)

    def _correct(self, ms, direction, dist):
        dx = sin(direction) * dist
        dy = cos(direction) * dist
        self.game_object.real_x += dx
        self.game_object.real_y += dy
        self.game_object.update_pos()

    def detect_collision(self, ms):
        collision = self.rect.colliderect
        for game_object in self.game_object.game_objects:
            if game_object is self.game_object:
                continue
            try:
                phys = game_object.get_component(Physics)
            except TypeError:
                continue
            if collision(game_object.rect):
                # handle collision
                self._handle_collision(game_object, ms)

    def get_direction(self):
        return self.direction

    def get_speed(self):
        return self.speed

    def set_direction(self, direction: float):
        self.direction = direction

    def set_speed(self, speed: float):
        self.speed = speed
