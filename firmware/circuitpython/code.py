import time

from nexor.boot import boot
from nexor.display import clear, show, text
from nexor.system import run_os

OS_NAME = "NexorOS"
OS_VERSION = "0.2.0"


def boot_screen():
    clear()
    text("NEXOROS", 43, 8)
    text("Starting...", 30, 28)
    text("NexorOS v0.2.0", 31, 45)
    show()
    time.sleep(2)


boot_screen()

if boot():
    run_os()
else:
    while True:
        time.sleep(1)