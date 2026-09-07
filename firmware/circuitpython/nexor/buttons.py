import board
import digitalio
import time


BUTTON_PINS = {
    "UP": board.GPIO4,
    "DOWN": board.GPIO5,
    "LEFT": board.GPIO6,
    "RIGHT": board.GPIO7,
    "OK": board.GPIO15,
    "BACK": board.GPIO16
}


buttons = {}

for name, pin in BUTTON_PINS.items():
    button = digitalio.DigitalInOut(pin)
    button.switch_to_input(pull=digitalio.Pull.UP)
    buttons[name] = button


def get_button():
    """
    Return one button press.

    Returns:
        "UP"
        "DOWN"
        "LEFT"
        "RIGHT"
        "OK"
        "BACK"
        None
    """

    for name, button in buttons.items():

        if not button.value:

            # Small debounce delay
            time.sleep(0.03)

            # Make sure it was a real press
            if not button.value:
                
                # Wait until released
                while not button.value:
                    time.sleep(0.01)

                # Small release debounce
                time.sleep(0.03)

                return name

    return None