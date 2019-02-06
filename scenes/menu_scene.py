import pygame
from pygame.locals import *
from scenes.scene import Scene
from pygame import ftfont
from utils.pygame_utils import *
from game_objects.demo import Demo
from game_objects.game_object import GameObject
from components import Physics, Player, Sprite
from better_timers import timers


class MenuScene(Scene):
    def __init__(self, controller):
        super().__init__(controller)
        self.__font = ftfont.Font(self.REGULAR_FONT, 50)
        self.text = self.__font.render("py-Man", True, (255, 255, 255))
        self.text = pad(self.text, (0, 100), (255, 100, 100))
        demo2 = Demo(self.game_objects, self.text.get_rect(), self.text)
        demo = GameObject(self.game_objects, pygame.Rect(100, 100, 30, 30))
        demo.image.fill((255, 100, 100))
        demo.add_component(Physics)
        demo.add_component(Sprite)
        demo.add_component(Player)
        background = pygame.Surface(self.screen_rect.size)
        background.fill((20, 20, 20))
        background = GameObject(self.game_objects,
                                pygame.Rect(0, 0, 0, 0), background
                                )
        background.blit(demo)
        crect1 = Rect(self.screen_rect)
        crect1.right = crect1.left
        crect2 = Rect(self.screen_rect)
        crect2.bottom = crect2.top
        crect3 = Rect(self.screen_rect)
        crect3.left = crect3.right
        crect4 = Rect(self.screen_rect)
        crect4.top = crect4.bottom
        collider1 = Demo(self.game_objects, crect1)
        collider2 = Demo(self.game_objects, crect2)
        collider3 = Demo(self.game_objects, crect3)
        collider4 = Demo(self.game_objects, crect4)
        collider1.get_component(Physics).set_static(True)
        collider2.get_component(Physics).set_static(True)
        collider3.get_component(Physics).set_static(True)
        collider4.get_component(Physics).set_static(True)

        self.game_objects.add(
            background, demo2, demo, collider1, collider2, collider3, collider4
        )
        my_event = pygame.event.Event(USEREVENT, code='wow')
        timers.set_timer(my_event, 1000, 5000)

    def create_title(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == USEREVENT:
                print(event.code)

    def update(self, ms):
        return super().update(ms)

    def render(self, screen):
        return super().render(screen)
