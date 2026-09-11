import time

from nexor.boot import boot
from nexor.display import clear, show, text, center_text
from nexor.system import run_os

OS_NAME = "NexorOS"
OS_VERSION = "0.3.0"


def boot_screen():
    clear()
    center_text("Esp Deck",20)
    #text("Starting...", 30, 28)
    text("Powered by",11,44)
    center_text("Next Core",56)
    
    show()
    time.sleep(2)


boot_screen()

if boot():
    run_os()
else:
    while True:
        time.sleep(1)