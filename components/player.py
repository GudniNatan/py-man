import pygame
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT
from pygame.key import get_pressed
from components.component import Component
from components.physics import Physics
from components.sprite import Sprite
from math import atan2


class Player(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.physics = self.game_object.get_component(Physics)
        self.speed_scale = 1.0
        self.key_code = 0
        try:
            self.sprite = self.game_object.get_component(Sprite)
        except TypeError:
            self.sprite = None

    def update(self, ms):
        self.update_speed()

    def update_speed(self):
        keys = get_pressed()
        if not (keys[K_UP] or keys[K_DOWN] or keys[K_RIGHT] or keys[K_LEFT]):
            self.joystick_input()
            self.key_code = 0
        else:
            key_code = (keys[K_UP] << 3) + (keys[K_DOWN] << 2)
            key_code += (keys[K_RIGHT] << 1) + keys[K_LEFT]
            if self.key_code != key_code:
                self.key_input(keys)
                self.key_code = key_code
        # self.set_sprite_direction()
        if self.sprite:
            self.sprite.set_direction()

    def joystick_input(self):
        if pygame.joystick.get_count():
            x = 0
            y = 0
            js = pygame.joystick.Joystick(0)
            if js.get_numhats():
                hat = js.get_hat(0)
                x, y = hat
            if x == y == 0 and js.get_numaxes() >= 2:
                x = js.get_axis(0)
                y = js.get_axis(1)
            if abs(x) > 0.02 or abs(y) > 0.02:
                self.physics.speed = (x ** 2 + y ** 2) ** 0.5
                self.physics.speed *= self.speed_scale
                self.physics.direction = atan2(x, y)
                return
        self.physics.speed = 0.0

    def key_input(self, keys):
        x = keys[K_RIGHT] - keys[K_LEFT]
        y = keys[K_DOWN] - keys[K_UP]
        if x or y:
            self.physics.direction = atan2(x, y)
            self.physics.speed = 1.0 * self.speed_scale
        else:
            self.physics.speed = 0.0

    def set_speed_scale(self, scalar):
        self.speed_scale = scalar
