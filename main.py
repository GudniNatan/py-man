import pygame
from pygame.locals import QUIT
from controllers.scene_controller import SceneController
from utils.pygame_utils import fix_path


def init():
    pygame.init()
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size, pygame.DOUBLEBUF)
    clock = pygame.time.Clock()
    game_loop(screen, clock, SceneController())
    pygame.quit()


def game_loop(screen, clock, scene_controller):
    running = True
    while running:
        if pygame.event.get(QUIT):
            running = False
            return
        events = pygame.event.get()
        updates = scene_controller.render(screen)
        scene_controller.handle_events(events)
        scene_controller.update(clock.get_time())
        pygame.display.update(updates)
        clock.tick()

if __name__ == "__main__":
    init()
