import pygame
import random
import src.player as player
import src.enemies as enemies
import src.superpos as superpos
import src.const as const
from typing import List
from src.const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ENEMY_SPAWN_INTERVAL_MS,
    GAMEOVER_PAUSE_INTERVAL_MS,
)

paused: bool = False
all_sprites: pygame.sprite.Group = pygame.sprite.Group()
player.sprite = player.create()
all_sprites.add(player.sprite)

ADDENEMY: int = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, ENEMY_SPAWN_INTERVAL_MS)


def gameover(screen: pygame.Surface) -> None:
    global paused
    player.sprite.kill()
    my_font = pygame.font.SysFont("Comic Sans MS", 48)
    text_surface = my_font.render("Game Over! ", False, (255, 0, 0), (0, 0, 0))
    screen.blit(text_surface, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3))
    pygame.time.set_timer(pygame.QUIT, GAMEOVER_PAUSE_INTERVAL_MS, 1)
    paused = True


# TODO: add text who was observed
# TODO: rewrite so dying as a twin is also killable???
# TODO: add random gate execution via pygame events
def observe(screen: pygame.Surface) -> None:
    if player.split and pygame.sprite.spritecollideany(player.twin, enemies.sprites):
        player.twin.kill()
        player.split = False
    if pygame.sprite.spritecollideany(player.sprite, enemies.sprites):
        if player.split:
            player.twin.kill()
            player.split = False
            if random.randint(1, 100) % 2 == 1 if player.inverted else 0:
                gameover(screen)
        else:
            gameover(screen)


def update(
    screen: pygame.Surface, event_queue: List[pygame.event.Event], delta_time: float
) -> None:
    for event in event_queue:
        if event.type == ADDENEMY:
            all_sprites.add(enemies.create())
    enemies.update(pygame.key.get_pressed(), delta_time)
    player.update(pygame.key.get_pressed(), event_queue, delta_time)
    observe(screen)
    pygame.draw.line(
        screen, (0, 0, 255), (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2)
    )
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    superpos.update(screen)
