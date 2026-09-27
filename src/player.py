import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_s,
    K_a,
    K_d,
)
from src.const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_SPEED,
)

sprite: pygame.sprite.Sprite()


def create() -> pygame.sprite.Sprite:
    global sprite
    sprite = pygame.sprite.Sprite()
    sprite.surf = pygame.Surface((60, 20))
    sprite.surf.fill((170, 255, 0))
    sprite.rect = sprite.surf.get_rect()
    return sprite


def update(pressed_keys: pygame.key.ScancodeWrapper, delta_time: float) -> None:
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
    if sprite.rect.top <= 0:
        sprite.rect.top = 0
    if sprite.rect.bottom >= SCREEN_HEIGHT:
        sprite.rect.bottom = SCREEN_HEIGHT
