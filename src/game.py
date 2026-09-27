import pygame
import random
import src.player as player
import src.enemies as enemies
import src.superpos as superpos
import src.const as const
import src.interfierence as noise
from typing import List
from src.const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ENEMY_SPAWN_INTERVAL_MS,
    GAMEOVER_PAUSE_INTERVAL_MS,
    OBSERVE_TEXT_INTERVAL_MS,
    CHEAT_INVULNARABLE,
)

paused: bool = False
all_sprites: pygame.sprite.Group = pygame.sprite.Group()
player.sprite = player.create()
all_sprites.add(player.sprite)
gameover_font = pygame.font.SysFont("Comic Sans MS", 48)
observed_font = pygame.font.SysFont("Comic Sans MS", 24)
observed_text: pygame.Surface
observed_active: bool = False

ADDENEMY: int = pygame.USEREVENT + 1
REMOVETXT: int = pygame.USEREVENT + 2
pygame.time.set_timer(ADDENEMY, ENEMY_SPAWN_INTERVAL_MS)


def observe(screen: pygame.Surface) -> None:
    # Handle someone gets observed in superposition
    if player.split and (
        pygame.sprite.spritecollideany(player.sprite, enemies.sprites)
        or pygame.sprite.spritecollideany(player.twin, enemies.sprites)
    ):
        first_was_obeserved: bool = (
            bool(pygame.sprite.spritecollideany(player.sprite, enemies.sprites))
            == player.inverted
        )
        observed_state: str = "1" if first_was_obeserved else "0"
        global observed_text, observed_active
        observed_text = observed_font.render(
            f"{observed_state} was observed", False, (255, 255, 0)
        )
        observed_active = True
        pygame.time.set_timer(REMOVETXT, OBSERVE_TEXT_INTERVAL_MS, 1)
        player.twin.kill()
        player.split = False
        if player.inverted != (random.randint(0, 1) == 1):
            player.sprite.rect.move_ip(
                0, (-SCREEN_HEIGHT if player.inverted else SCREEN_HEIGHT) // 2
            )
            player.inverted = not player.inverted

    # Handle player colliding with enemy
    if pygame.sprite.spritecollideany(player.sprite, enemies.sprites):
        if CHEAT_INVULNARABLE:
            return
        global paused
        text_surface = gameover_font.render(
            "Game Over! ", False, (255, 0, 0), (0, 0, 0)
        )
        screen.blit(text_surface, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3))
        pygame.time.set_timer(pygame.QUIT, GAMEOVER_PAUSE_INTERVAL_MS, 1)
        paused = True


def update(
    screen: pygame.Surface, event_queue: List[pygame.event.Event], delta_time: float
) -> None:
    global observed_active
    for event in event_queue:
        if event.type == ADDENEMY:
            all_sprites.add(enemies.create())
        if event.type == REMOVETXT:
            observed_active = False
    enemies.update(pygame.key.get_pressed(), delta_time)
    player.update(pygame.key.get_pressed(), event_queue, delta_time)
    noise.update()
    observe(screen)
    pygame.draw.line(
        screen, (0, 0, 255), (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2)
    )
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if observed_active:
        screen.blit(observed_text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2))
    superpos.update(screen)
