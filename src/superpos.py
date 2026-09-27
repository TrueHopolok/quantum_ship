import pygame
import src.player as player
from src.const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)


inverted: bool = False
split: bool = False
superpos_font = pygame.font.SysFont("Calibri", 24)


def update(screen: pygame.Surface) -> None:
    symbol: str
    if not player.split:
        symbol = "1" if player.inverted else "0"
    else:
        symbol = "-" if player.inverted else "+"
    text_surface = superpos_font.render(
        f"|{symbol}>", pygame.font.Font.bold, (255, 255, 255), (0, 0, 0)
    )
    screen.blit(text_surface, (SCREEN_WIDTH * 7 // 8, 10))
