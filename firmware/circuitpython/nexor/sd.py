import board
import sdcardio
import storage

from .spi import spi


# =========================================================
# NEXOR SD CONFIGURATION
# =========================================================

SD_MOUNT = "/sd"
SD_CS = board.GPIO14

sd = None
vfs = None
initialized = False


# =========================================================
# INITIALIZE SD
# =========================================================

def init_sd():

    global sd
    global vfs
    global initialized

    # Already initialized
    if initialized:
        return True

    # Create SD card
    sd = sdcardio.SDCard(
        spi,
        SD_CS
    )

    # Create filesystem
    vfs = storage.VfsFat(sd)

    # Mount SD card
    storage.mount(
        vfs,
        SD_MOUNT
    )

    initialized = True

    return True


# =========================================================
# CHECK SD
# =========================================================

def exists():

    try:

        import os

        os.listdir(SD_MOUNT)

        return True

    except OSError:

        return False