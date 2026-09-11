from .display import clear, show, text, inverted_text, rounded_rect, fill_rounded_rect, hline
from .buttons import get_button
import time

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64
VISIBLE_ITEMS = 4


def header(title):
    clear()
    # Thin rounded device-style frame.
    rounded_rect(1, 1, 126, 62, 5, 1)
    text(title, 8, 3)
    hline(4, 13, 120, 1)


def menu(items, selected=0):
    if not items:
        header("Menu")
        text("EMPTY", 49, 30)
        show()
        return

    selected = max(0, min(selected, len(items) - 1))

    # Keep the selected item visible while showing four clean rows.
    if len(items) <= VISIBLE_ITEMS:
        start = 0
    else:
        start = min(max(0, selected - 1), len(items) - VISIBLE_ITEMS)

    header("Menu")

    # 128x64 / 5x8 font: four rows with generous spacing.
    row_y = (18, 30, 42, 54)
    card_x = 10
    card_w = 110
    card_h = 10

    for row, y in enumerate(row_y):
        index = start + row
        if index >= len(items):
            break

        label = items[index]
        label_w = len(label) * 6
        x = max(5, (SCREEN_WIDTH - label_w) // 2)

        if index == selected:
            # Solid selection bar, matching the reference design.
            fill_rounded_rect(card_x, y - 2, card_w, card_h, 3, 1)
            inverted_text(label, x, y - 1)
        else:
            text(label, x, y)

    show()


def run_menu(items):
    if not items:
        return None

    selected = 0
    menu(items, selected)

    while True:
        button = get_button()

        if button is None:
            time.sleep(0.01)
            continue

        if button == "UP":
            selected = (selected - 1) % len(items)
            menu(items, selected)
        elif button == "DOWN":
            selected = (selected + 1) % len(items)
            menu(items, selected)
        elif button == "OK":
            return selected
        elif button == "BACK":
            return None
