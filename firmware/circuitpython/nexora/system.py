import time

from .display import (
    clear,
    show,
    text,
    center_text,
    draw_big_time
)

from .buttons import get_button
from .ui import run_menu
from .clock import get_time_string, get_date_string, get_datetime


OS_NAME = "NEXORA"
OS_VERSION = "0.2.0"


MAIN_MENU = [
    "To-Do List",
    "Music Player",
    "Stopwatch",
    "File Manager",
    "Advanced Tools",
    "Settings"
]


# -------------------------
# HOME SCREEN
# -------------------------

def show_home():

    clear()

    # Status bar
    text("NEXORA", 2, 0)
    text("SD", 108, 0)

    # Top separator
    text("----------------------", 0, 9)

    # Large clock
    draw_big_time(get_time_string())

    # Date
    center_text(get_date_string(), 50)

    # Soft-key area
    # No separator here because there isn't enough
    # vertical space for both the line and text.

    text("MENU", 2, 57)
    text("OK", 113, 57)

    show()

# -------------------------
# Wait on home screen
# -------------------------

def wait_for_menu():

    last_second = -1

    while True:

        dt = get_datetime()
        current_second = dt.tm_sec

        if current_second != last_second:

            show_home()

            last_second = current_second

        button = get_button()

        if button == "OK":
            return

        time.sleep(0.01)


# -------------------------
# Temporary app screen
# -------------------------

def app_placeholder(name):

    clear()

    center_text(name, 18)
    center_text("APP NOT READY", 32)
    center_text("BACK = MENU", 50)

    show()

    while True:

        button = get_button()

        if button == "BACK":
            return

        time.sleep(0.01)


# -------------------------
# Launch application
# -------------------------

def launch_app(index):

    if index == 0:
        app_placeholder("To-Do List")

    elif index == 1:
        app_placeholder("Music Player")

    elif index == 2:
        app_placeholder("Stopwatch")

    elif index == 3:
        app_placeholder("File Manager")

    elif index == 4:
        app_placeholder("Advanced Tools")

    elif index == 5:
        app_placeholder("Settings")


# -------------------------
# Main menu
# -------------------------

def show_main_menu():

    return run_menu(MAIN_MENU)


# -------------------------
# NEXORA OS
# -------------------------

def run_os():

    while True:

        show_home()

        wait_for_menu()

        selected = show_main_menu()

        if selected is None:
            continue

        launch_app(selected)