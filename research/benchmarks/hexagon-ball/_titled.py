"""Launch a pygame script with a forced window title.
Usage: python3 _titled.py "Label" game.py
Monkeypatches set_mode/set_caption so the window title is always the label,
without editing the generated game file.
"""
import sys
import pygame

LABEL = sys.argv[1]
GAME = sys.argv[2]

_orig_set_mode = pygame.display.set_mode
_orig_set_caption = pygame.display.set_caption


def set_mode(*a, **k):
    surf = _orig_set_mode(*a, **k)
    _orig_set_caption(LABEL)
    return surf


def set_caption(*a, **k):
    _orig_set_caption(LABEL)


pygame.display.set_mode = set_mode
pygame.display.set_caption = set_caption

sys.argv = [GAME]
with open(GAME) as f:
    code = compile(f.read(), GAME, "exec")
exec(code, {"__name__": "__main__", "__file__": GAME})
