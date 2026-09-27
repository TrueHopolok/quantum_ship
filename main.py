import pygame

pygame.init()

import src.game as game
from pygame.locals import (
    K_ESCAPE,
)
from src.const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    DELTA_TIME_MIN,
    FPS,
)

screen: pygame.Surface
delta_time: float = 1.0 / FPS


def main() -> None:
    global screen, delta_time
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    running = True
    while running:
        event_queue = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                event_queue.append(event)
        if pygame.key.get_pressed()[K_ESCAPE]:
            running = False
        if game.paused:
            continue
        screen.fill((0, 0, 0))
        game.update(screen, event_queue, delta_time)
        pygame.display.flip()
        delta_time = max(float(clock.tick(FPS)) / 1000.0, DELTA_TIME_MIN)


if __name__ == "__main__":
    main()
