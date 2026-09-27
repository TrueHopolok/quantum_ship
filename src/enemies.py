import pygame
import random
import src.player as player
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_w,
    K_s,
)
from src.const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ENEMY_MIN_SPEED,
    ENEMY_MAX_SPEED,
    PLAYER_SPEED,
)

sprites: pygame.sprite.Group = pygame.sprite.Group()


def create() -> pygame.sprite.Sprite:
    enemy = pygame.sprite.Sprite()
    enemy.surf = pygame.Surface((20, 10))
    enemy.surf.fill((255, 0, 0))
    enemy_X = random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100)
    enemy_Y = random.randint(0, SCREEN_HEIGHT)
    enemy.rect = enemy.surf.get_rect(center=(enemy_X, enemy_Y))
    enemy.speed = random.uniform(ENEMY_MIN_SPEED, ENEMY_MAX_SPEED)
    sprites.add(enemy)
    return enemy


def update(pressed_keys: pygame.key.ScancodeWrapper, delta_time: float) -> None:
    for enemy in sprites:
        enemy.rect.move_ip(-enemy.speed * delta_time, 0)
        if player.split:
            if pressed_keys[K_UP] or pressed_keys[K_w]:
                enemy.rect.move_ip(0, -PLAYER_SPEED * delta_time)
            if pressed_keys[K_DOWN] or pressed_keys[K_s]:
                enemy.rect.move_ip(0, PLAYER_SPEED * delta_time)
        if enemy.rect.right < 0:
            enemy.kill()
