import pygame
from math import atan2, sin, cos
from components.component import Component
from utils.pygame_utils import push_ip


class Physics(Component):
    BASE_SPEED = 1 / 10

    def __init__(self, game_object):
        super().__init__(game_object)
        self.bounciness = 0.0
        self.collision = True
        self.direction = 0.0
        self.speed = 0.0
        self.gravity = 0.0
        self.friction = -0.1
        self.rect = self.game_object.rect
        self.weight = self.rect.height * self.rect.width
        self.__static = False
        self.__default_update = self.update

    def update(self, ms):
        self.move(ms)
        self.detect_collision()

    def move(self, ms):
        dist = ms * self.BASE_SPEED * self.speed
        dx = sin(self.direction) * dist
        dy = cos(self.direction) * dist + self.gravity
        self.game_object.real_x += dx
        self.game_object.real_y += dy
        self.game_object.update_pos()
        if self.friction:
            self.speed = self.speed * (1 - (self.friction * ms / 1000))

    def handle_collision(self, other):
        try:
            phys = other.get_component(Physics)
        except TypeError:
            return
        my_rect = self.rect
        other_rect = other.rect
        if self.weight > phys.weight or phys.__static:
            push_ip(other_rect, self.rect)
            phys.detect_collision()
            if self.rect.colliderect(other.rect):
                push_ip(self.rect, other_rect)
        if abs(self.game_object.real_x - self.rect.x) > 1:
            self.game_object.real_x = self.rect.x
        if abs(self.game_object.real_y - self.rect.y) > 1:
            self.game_object.real_y = self.rect.y
        if self.bounciness:
            clip = pygame.Rect.clip(my_rect, other_rect)
            direction = atan2(
                my_rect.centerx - clip.centerx, my_rect.centery - clip.centery
            )
            self._bounce(direction)

    def _bounce(self, direction):
        x = (sin(direction) + sin(self.direction)) / 2
        y = (cos(direction) + cos(self.direction)) / 2
        self.direction = atan2(x, y)
        self.speed *= self.bounciness

    def _correct(self, ms, direction, dist):
        dx = sin(direction) * dist
        dy = cos(direction) * dist
        self.game_object.real_x += dx
        self.game_object.real_y += dy
        self.game_object.update_pos()

    def detect_collision(self):
        collision = self.rect.colliderect
        for game_object in self.game_object.game_objects:
            if game_object is self.game_object:
                continue
            if collision(game_object.rect):
                # handle collision
                self.handle_collision(game_object)

    def __static_update(self, ms):
        return

    def get_direction(self):
        return self.direction

    def get_speed(self):
        return self.speed

    def set_direction(self, direction: float):
        self.direction = direction

    def set_speed(self, speed: float):
        self.speed = speed

    def set_gravity(self, gravity: float):
        self.gravity = gravity

    def set_static(self, static: bool):
        self.__static = static
        if static:
            self.update = self.__default_update
        else:
            self.update = self.__static_update
