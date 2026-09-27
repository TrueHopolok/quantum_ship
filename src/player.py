import pygame
import src.game as game
from typing import List
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_s,
    K_a,
    K_d,
    K_x,
    K_h,
    K_z,
)
from src.const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_SPEED,
    EASIER_SUPERPOS,
)


sprite: pygame.sprite.Sprite
twin: pygame.sprite.Sprite
inverted: bool = False
split: bool = False


def create(x: int = 0, y: int = 0) -> pygame.sprite.Sprite:
    sprite = pygame.sprite.Sprite()
    sprite.surf = pygame.Surface((60, 20))
    sprite.surf.fill((170, 255, 0))
    sprite.rect = sprite.surf.get_rect()
    sprite.rect.move_ip(x, y)
    return sprite


def update(
    pressed_keys: pygame.key.ScancodeWrapper,
    event_queue: List[pygame.event.Event],
    delta_time: float,
) -> None:
    global inverted, split, twin
    for event in event_queue:
        if event.type == pygame.KEYDOWN:
            if event.key == K_h:
                if split:
                    twin.kill()
                else:
                    twin = create(
                        sprite.rect.left,
                        sprite.rect.top
                        + (-SCREEN_HEIGHT // 2 if inverted else SCREEN_HEIGHT // 2),
                    )
                    if EASIER_SUPERPOS:
                        twin.surf.fill((0, 170, 170))
                    game.all_sprites.add(twin)
                split = not split
            if event.key == K_x and not split:
                sprite.rect.move_ip(
                    0, (-SCREEN_HEIGHT if inverted else SCREEN_HEIGHT) // 2
                )
                inverted = not inverted
            if event.key == K_z and split:
                sprite.rect.move_ip(
                    0, (-SCREEN_HEIGHT if inverted else SCREEN_HEIGHT) // 2
                )
                twin.rect.move_ip(
                    0, (SCREEN_HEIGHT if inverted else -SCREEN_HEIGHT) // 2
                )
                inverted = not inverted
    if not split:
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            sprite.rect.move_ip(0, -PLAYER_SPEED * delta_time)
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            sprite.rect.move_ip(0, PLAYER_SPEED * delta_time)
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            sprite.rect.move_ip(-PLAYER_SPEED * delta_time, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            sprite.rect.move_ip(PLAYER_SPEED * delta_time, 0)

    if sprite.rect.left < 0:
        sprite.rect.left = 0
    if sprite.rect.right > SCREEN_WIDTH:
        sprite.rect.right = SCREEN_WIDTH
    HEIGHT_LIM: int = SCREEN_HEIGHT // 2 if inverted else 0
    if sprite.rect.top <= HEIGHT_LIM:
        sprite.rect.top = HEIGHT_LIM
    if sprite.rect.bottom >= HEIGHT_LIM + SCREEN_HEIGHT // 2:
        sprite.rect.bottom = HEIGHT_LIM + SCREEN_HEIGHT // 2
