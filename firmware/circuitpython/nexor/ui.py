from .display import clear, show, text
from .buttons import get_button
import time


SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

VISIBLE_ITEMS = 5


def header(title):
    """Draw the NexorOS header."""

    clear()

    text(title, 45, 0)
    text("----------------", 8, 9)


def menu(items, selected=0):
    """
    Draw a scrollable menu.

    items:
        List of menu item names.

    selected:
        Currently selected item index.
    """

    # Empty menu
    if len(items) == 0:
        clear()
        text("EMPTY MENU", 32, 28)
        show()
        return


    # Keep selection valid
    if selected < 0:
        selected = 0

    if selected >= len(items):
        selected = len(items) - 1


    # -----------------------------------------------------
    # Calculate scrolling position
    # -----------------------------------------------------

    if len(items) <= VISIBLE_ITEMS:

        start = 0

    else:

        start = selected - (VISIBLE_ITEMS // 2)

        if start < 0:
            start = 0

        maximum_start = len(items) - VISIBLE_ITEMS

        if start > maximum_start:
            start = maximum_start


    # -----------------------------------------------------
    # Draw menu
    # -----------------------------------------------------

    header("MENU")


    for row in range(VISIBLE_ITEMS):

        index = start + row

        if index >= len(items):
            break

        y = 15 + (row * 9)


        # Selection arrow
        if index == selected:
            text(">", 2, y)


        # Item text
        text(items[index], 12, y)


    # -----------------------------------------------------
    # Scroll indicators
    # -----------------------------------------------------

    if start > 0:
        text("^", 122, 15)

    if start + VISIBLE_ITEMS < len(items):
        text("v", 122, 51)


    show()


def run_menu(items):
    """
    Run an interactive menu.

    Returns:
        Selected item index when OK is pressed.
        None when BACK is pressed.
    """

    # Empty menu
    if len(items) == 0:
        return None


    selected = 0

    menu(items, selected)


    while True:

        button = get_button()


        if button is None:
            time.sleep(0.01)
            continue


        # -------------------------------------------------
        # UP
        # -------------------------------------------------

        if button == "UP":

            selected -= 1

            if selected < 0:
                selected = len(items) - 1

            menu(items, selected)


        # -------------------------------------------------
        # DOWN
        # -------------------------------------------------

        elif button == "DOWN":

            selected += 1

            if selected >= len(items):
                selected = 0

            menu(items, selected)


        # -------------------------------------------------
        # OK
        # -------------------------------------------------

        elif button == "OK":

            return selected


        # -------------------------------------------------
        # BACK
        # -------------------------------------------------

        elif button == "BACK":

            return None