import board
import digitalio
import adafruit_ssd1306

from .spi import spi

OLED_CS = board.GPIO10
OLED_DC = board.GPIO9
OLED_RESET = board.GPIO8

cs = digitalio.DigitalInOut(OLED_CS)
dc = digitalio.DigitalInOut(OLED_DC)
reset = digitalio.DigitalInOut(OLED_RESET)

oled = adafruit_ssd1306.SSD1306_SPI(
    128,
    64,
    spi,
    dc,
    reset,
    cs
)


# -------------------------
# Basic display functions
# -------------------------

def clear():
    oled.fill(0)


def show():
    oled.show()


def text(message, x, y):
    oled.text(message, x, y, 1)


def clear_and_show():
    oled.fill(0)
    oled.show()


# -------------------------
# Graphics helpers
# -------------------------

def pixel(x, y, value=1):
    oled.pixel(x, y, value)


def fill_rect(x, y, width, height, value=1):
    oled.fill_rect(x, y, width, height, value)


def rect(x, y, width, height, value=1):
    oled.rect(x, y, width, height, value)


# -------------------------
# Centered text
# -------------------------

def center_text(message, y):
    width = len(message) * 6
    x = (128 - width) // 2
    text(message, x, y)


# -------------------------
# Big clock digits
# 5 x 7 pixel font
# -------------------------

DIGITS = {
    "0": [
        "11111",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "11111"
    ],

    "1": [
        "00100",
        "01100",
        "00100",
        "00100",
        "00100",
        "00100",
        "01110"
    ],

    "2": [
        "11111",
        "00001",
        "00001",
        "11111",
        "10000",
        "10000",
        "11111"
    ],

    "3": [
        "11111",
        "00001",
        "00001",
        "11111",
        "00001",
        "00001",
        "11111"
    ],

    "4": [
        "10001",
        "10001",
        "10001",
        "11111",
        "00001",
        "00001",
        "00001"
    ],

    "5": [
        "11111",
        "10000",
        "10000",
        "11111",
        "00001",
        "00001",
        "11111"
    ],

    "6": [
        "11111",
        "10000",
        "10000",
        "11111",
        "10001",
        "10001",
        "11111"
    ],

    "7": [
        "11111",
        "00001",
        "00010",
        "00100",
        "01000",
        "01000",
        "01000"
    ],

    "8": [
        "11111",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "11111"
    ],

    "9": [
        "11111",
        "10001",
        "10001",
        "11111",
        "00001",
        "00001",
        "11111"
    ]
}


def draw_big_digit(digit, x, y, scale=3):
    pattern = DIGITS.get(digit)

    if pattern is None:
        return

    for row in range(7):
        for col in range(5):

            if pattern[row][col] == "1":
                fill_rect(
                    x + col * scale,
                    y + row * scale,
                    scale,
                    scale,
                    1
                )


def draw_big_time(time_string):
    """
    Draw HH:MM centered on the OLED.
    """

    scale = 3

    digit_width = 5 * scale
    spacing = 3

    colon_width = 3

    total_width = (
        digit_width * 4
        + spacing * 4
        + colon_width
    )

    x = (128 - total_width) // 2
    y = 20

    for char in time_string:

        if char == ":":
            fill_rect(x, y + 6, 3, 3, 1)
            fill_rect(x, y + 15, 3, 3, 1)

            x += colon_width + spacing

        else:
            draw_big_digit(char, x, y, scale)
            x += digit_width + spacing

# -------------------------
# Menu graphics helpers
# -------------------------

def hline(x, y, width, value=1):
    """Draw a horizontal line."""
    oled.hline(x, y, width, value)


def inverted_text(message, x, y):
    """Draw white text on the black selection card."""
    width = len(message) * 6
    height = 8
    oled.fill_rect(x, y, width, height, 0)
    oled.text(message, x, y, 1)


def _rounded_corners(x, y, width, height, radius, value=1):
    """Draw the corner pixels for a small rounded rectangle."""
    # radius 2/3 is enough for the 128x64 menu without expensive circles.
    if radius <= 1:
        return

    for offset in range(1, radius):
        # Simple symmetric corner approximation.
        oled.pixel(x + offset, y + (radius - offset), value)
        oled.pixel(x + width - 1 - offset, y + (radius - offset), value)
        oled.pixel(x + offset, y + height - 1 - (radius - offset), value)
        oled.pixel(x + width - 1 - offset, y + height - 1 - (radius - offset), value)


def rounded_rect(x, y, width, height, radius=3, value=1):
    """Draw a lightweight rounded rectangle outline."""
    if width <= 0 or height <= 0:
        return

    if radius < 1:
        oled.rect(x, y, width, height, value)
        return

    # Main straight sections.
    oled.hline(x + radius, y, width - (2 * radius), value)
    oled.hline(x + radius, y + height - 1, width - (2 * radius), value)
    oled.vline(x, y + radius, height - (2 * radius), value)
    oled.vline(x + width - 1, y + radius, height - (2 * radius), value)

    # Rounded corners using small pixel steps.
    _rounded_corners(x, y, width, height, radius, value)


def fill_rounded_rect(x, y, width, height, radius=3, value=1):
    """Draw a lightweight filled rounded rectangle."""
    if width <= 0 or height <= 0:
        return

    if radius < 1:
        oled.fill_rect(x, y, width, height, value)
        return

    # Fill the center first.
    oled.fill_rect(x + radius, y, width - (2 * radius), height, value)
    oled.fill_rect(x, y + radius, width, height - (2 * radius), value)

    # Fill the small corner regions.
    for offset in range(radius):
        inset = radius - offset
        oled.hline(
            x + inset,
            y + offset,
            width - (2 * inset),
            value
        )
        oled.hline(
            x + inset,
            y + height - 1 - offset,
            width - (2 * inset),
            value
        )
