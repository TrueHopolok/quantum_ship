import pygame
import src.player as player
import src.enemies as enemies
import src.const as const
from typing import List
from src.const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ENEMY_SPAWN_INTERVAL_MS,
    GAMEOVER_PAUSE_INTERVAL_MS,
)

paused: bool = False
all_sprites = pygame.sprite.Group()
all_sprites.add(player.create())


ADDENEMY: int = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, ENEMY_SPAWN_INTERVAL_MS)


def update(
    screen: pygame.Surface, event_queue: List[pygame.event.Event], delta_time: float
) -> None:
    for event in event_queue:
        if event.type == ADDENEMY:
            all_sprites.add(enemies.create())
    enemies.update(delta_time)
    player.update(pygame.key.get_pressed(), delta_time)
    if pygame.sprite.spritecollideany(player.sprite, enemies.sprites):
        player.sprite.kill()
        my_font = pygame.font.SysFont("Comic Sans MS", 48)  # create a font object\
        text_surface = my_font.render("Game Over! ", False, (255, 0, 0), (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3))
        pygame.time.set_timer(pygame.QUIT, GAMEOVER_PAUSE_INTERVAL_MS, 1)
        global paused
        paused = True
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
