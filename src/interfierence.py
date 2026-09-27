import pygame
import random
from typing import List
from src.const import (
    RANDOM_INTERFIERENCE_ENABLED,
    FPS,
    INTERFIERENCE_OVERALL_FREQUENCY,
    INTERFIERENCE_X_CHANCE,
    INTERFIERENCE_Z_CHANCE,
    INTERFIERENCE_H_CHANCE,
)


## Will be applied into the next frame
def update() -> None:
    if not RANDOM_INTERFIERENCE_ENABLED:
        return
    chance: int = random.randint(
        1,
        INTERFIERENCE_OVERALL_FREQUENCY
        * (INTERFIERENCE_X_CHANCE + INTERFIERENCE_Z_CHANCE + INTERFIERENCE_H_CHANCE)
        * int(FPS),
    )
    if chance <= INTERFIERENCE_X_CHANCE:
        newevent = pygame.event.Event(
            pygame.locals.KEYDOWN,
            key=pygame.locals.K_x,
        )
        pygame.event.post(newevent)
    elif chance <= INTERFIERENCE_X_CHANCE + INTERFIERENCE_Z_CHANCE:
        newevent = pygame.event.Event(
            pygame.locals.KEYDOWN,
            key=pygame.locals.K_z,
        )
        pygame.event.post(newevent)
    elif (
        chance
        <= INTERFIERENCE_X_CHANCE + INTERFIERENCE_Z_CHANCE + INTERFIERENCE_H_CHANCE
    ):
        newevent = pygame.event.Event(
            pygame.locals.KEYDOWN,
            key=pygame.locals.K_h,
        )
        pygame.event.post(newevent)
