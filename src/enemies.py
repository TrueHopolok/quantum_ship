import pygame
import random
from src.const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ENEMY_MIN_SPEED,
    ENEMY_MAX_SPEED,
)

sprites = pygame.sprite.Group()


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


def update(delta_time: float) -> None:
    for enemy in sprites:
        enemy.rect.move_ip(-enemy.speed * delta_time, 0)
        if enemy.rect.right < 0:
            enemy.kill()
