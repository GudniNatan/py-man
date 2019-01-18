import pygame
from pygame.locals import QUIT
from controllers.scene_controller import SceneController
from better_timers.better_timers import timers


def init():
    pygame.init()
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size, pygame.DOUBLEBUF)
    clock = pygame.time.Clock()
    game_loop(screen, clock, SceneController())
    timers.end_all_timers()
    pygame.quit()


def game_loop(screen, clock, scene_controller):
    running = True
    while running:
        if pygame.event.get(QUIT):
            running = False
            return
        events = pygame.event.get()
        scene_controller.render(screen)
        scene_controller.handle_events(events)
        scene_controller.update(clock.get_time())
        pygame.display.update()
        clock.tick()

if __name__ == "__main__":
    init()
