import pygame
from pygame.locals import *
from better_timers import BetterTimers

# Alternatively:
# from BetterTimers import timers as myTimers

genericEvent = USEREVENT + 1
randomEvent = USEREVENT + 2

pygame.init()
window_size = window_width, window_height = 1280, 720
screen = pygame.display.set_mode(window_size, pygame.DOUBLEBUF)
clock = pygame.time.Clock()
pygame.display.set_caption('Better timer demo')

timers = BetterTimers()  # You need to define the BetterTimers object

coolEvent = pygame.event.Event(genericEvent, code="cool")
uncoolEvent = pygame.event.Event(genericEvent, code="uncool")

# Sets a timer for 500 milliseconds
timers.set_timer(coolEvent, 500)
# New genericEvent timer with a different code
timers.set_timer(uncoolEvent, 1000)
# Overrides old 500 rate timer, with delay
timers.set_timer(coolEvent, 2000, 300)

# Traditional timer set where there are no extra arguments
timers.set_timer(randomEvent, 5000)
timers.set_timer(randomEvent, 0)  # Timer stopped


running = True

while running:  # Game loop
    for event in pygame.event.get():  # Event handling
        if event.type == pygame.QUIT:
            running = False
            # We stop all the timers to be able to exit safely
            timers.end_all_timers()
            pygame.quit()
            break
        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            pygame.event.post(pygame.event.Event(QUIT))
        elif event.type == randomEvent:
            print("WOWZERS")
        elif event == coolEvent:
            print("COOL EVENT")
        elif event.type == genericEvent and event.code == 'uncool':
            print("SO UNCOOL")
    # It is good game design to try to limit the fps as little as possible.
    clock.tick(1000)
pygame.quit()
