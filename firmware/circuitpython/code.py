import time

from nexora.boot import boot
from nexora.display import clear, show, text
from nexora.system import run_os

OS_NAME = "NEXORA"
OS_VERSION = "0.1.0"


def boot_screen():
    clear()
    text("NEXORA", 45, 8)
    text("Starting...", 30, 28)
    text("OS v0.1.0", 38, 45)
    show()
    time.sleep(2)


boot_screen()

if boot():
    run_os()
else:
    while True:
        time.sleep(1)