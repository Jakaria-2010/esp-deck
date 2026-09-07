import os
import time

from .clock import edit_datetime, load_datetime
from .display import clear, show, text
from .sd import init_sd


# =========================================================
# NEXORA CONFIGURATION
# =========================================================

NEXORA_DIR = "/sd/NEXORA"
CONFIG_DIR = "/sd/NEXORA/config"
CONFIG_FILE = "/sd/NEXORA/config/system.cfg"


# =========================================================
# SD INITIALIZATION
# =========================================================

_sd_ready = False


def initialize_storage():

    global _sd_ready

    if _sd_ready:
        return True

    try:
        init_sd()
        _sd_ready = True
        return True

    except OSError:
        _sd_ready = False
        return False


# =========================================================
# CREATE DIRECTORIES
# =========================================================

def create_directories():

    try:
        os.mkdir(NEXORA_DIR)
    except OSError:
        pass

    try:
        os.mkdir(CONFIG_DIR)
    except OSError:
        pass


# =========================================================
# CHECK CONFIGURATION
# =========================================================

def is_configured():

    try:

        with open(CONFIG_FILE, "r") as f:
            data = f.read().strip()

        if data == "NEXORA_CONFIGURED":
            return True

    except OSError:
        pass

    return False


# =========================================================
# SAVE CONFIGURATION
# =========================================================

def save_configuration():

    create_directories()

    with open(CONFIG_FILE, "w") as f:
        f.write("NEXORA_CONFIGURED")


# =========================================================
# FIRST BOOT
# =========================================================

def first_boot():

    # -----------------------------------------------------
    # Initialize SD
    # -----------------------------------------------------

    if not initialize_storage():

        clear()

        text(
            "SD ERROR",
            45,
            18
        )

        text(
            "CHECK CARD",
            35,
            38
        )

        show()

        time.sleep(3)

        return False


    # -----------------------------------------------------
    # Welcome screen
    # -----------------------------------------------------

    clear()

    text(
        "WELCOME TO",
        32,
        12
    )

    text(
        "NexorOS",
        45,
        25
    )

    text(
        "FIRST SETUP",
        32,
        42
    )

    show()

    time.sleep(2)


    # -----------------------------------------------------
    # DATE / TIME SETUP
    # -----------------------------------------------------

    result = edit_datetime()


    # -----------------------------------------------------
    # USER CANCELLED
    # -----------------------------------------------------

    if result is False:

        return False


    # -----------------------------------------------------
    # SAVE CONFIGURATION
    # -----------------------------------------------------

    try:

        save_configuration()

    except OSError:

        clear()

        text(
            "SAVE ERROR",
            38,
            18
        )

        text(
            "SD WRITE FAIL",
            25,
            38
        )

        show()

        time.sleep(3)

        return False


    # -----------------------------------------------------
    # SETUP COMPLETE
    # -----------------------------------------------------

    clear()

    text(
        "SETUP COMPLETE",
        20,
        20
    )

    text(
        "WELCOME!",
        35,
        35
    )

    show()

    time.sleep(2)

    return True


# =========================================================
# NEXORA BOOT
# =========================================================

def boot():

    # -----------------------------------------------------
    # Initialize storage
    # -----------------------------------------------------

    if not initialize_storage():

        return False


    # -----------------------------------------------------
    # Check configuration
    # -----------------------------------------------------

    if is_configured():
        load_datetime()
        return True


    # -----------------------------------------------------
    # First boot
    # -----------------------------------------------------

    return first_boot()