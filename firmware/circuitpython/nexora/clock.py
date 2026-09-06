import rtc
import time
import os

from .display import clear, show, text
from .buttons import get_button


# =========================================================
# NEXORA CLOCK
# =========================================================

_rtc = rtc.RTC()

DATETIME_FILE = "/sd/NEXORA/config/datetime.cfg"


# =========================================================
# GET DATE / TIME
# =========================================================

def get_datetime():
    return _rtc.datetime


def get_time_string():
    dt = _rtc.datetime

    return "{:02d}:{:02d}".format(
        dt.tm_hour,
        dt.tm_min
    )


def get_date_string():
    dt = _rtc.datetime

    return "{:02d}/{:02d}/{:04d}".format(
        dt.tm_mday,
        dt.tm_mon,
        dt.tm_year
    )


# =========================================================
# SAVE DATE / TIME
# =========================================================
def ensure_config_directory():
    try:
        os.mkdir("/sd/NEXORA")
    except OSError:
        pass

    try:
        os.mkdir("/sd/NEXORA/config")
    except OSError:
        pass

def save_datetime():
    ensure_config_directory()

    dt = _rtc.datetime

    try:
        with open("/sd/NEXORA/config/datetime.cfg", "w") as f:
            f.write("{},{},{},{},{},{}".format(
                dt.tm_year,
                dt.tm_mon,
                dt.tm_mday,
                dt.tm_hour,
                dt.tm_min,
                dt.tm_sec
            ))

        return True

    except OSError:
        return False


# =========================================================
# LOAD DATE / TIME
# =========================================================

def load_datetime():
    try:
        with open(DATETIME_FILE, "r") as f:
            data = f.read().strip()

        values = data.split(",")

        if len(values) != 6:
            return False

        year = int(values[0])
        month = int(values[1])
        day = int(values[2])
        hour = int(values[3])
        minute = int(values[4])
        second = int(values[5])

        _rtc.datetime = time.struct_time(
            (
                year,
                month,
                day,
                hour,
                minute,
                second,
                0,
                -1,
                -1
            )
        )

        return True

    except (OSError, ValueError, IndexError):
        return False


# =========================================================
# SET DATE / TIME
# =========================================================

def set_datetime(
    day,
    month,
    year,
    hour,
    minute,
    second=0
):

    _rtc.datetime = time.struct_time(
        (
            year,
            month,
            day,
            hour,
            minute,
            second,
            0,
            -1,
            -1
        )
    )


def set_time(hour, minute, second=0):

    dt = _rtc.datetime

    set_datetime(
        dt.tm_mday,
        dt.tm_mon,
        dt.tm_year,
        hour,
        minute,
        second
    )


def set_date(year, month, day):

    dt = _rtc.datetime

    set_datetime(
        day,
        month,
        year,
        dt.tm_hour,
        dt.tm_min,
        dt.tm_sec
    )


# =========================================================
# DAYS IN MONTH
# =========================================================

def days_in_month(year, month):

    if month == 2:

        if (
            year % 4 == 0
            and (year % 100 != 0 or year % 400 == 0)
        ):
            return 29

        return 28

    if month in (4, 6, 9, 11):
        return 30

    return 31


# =========================================================
# EDIT DATE / TIME
# =========================================================

def edit_datetime():

    # Get current RTC value
    dt = _rtc.datetime

    # Editable values
    #
    # 0 = DAY
    # 1 = MONTH
    # 2 = YEAR
    # 3 = HOUR
    # 4 = MINUTE

    values = [
        dt.tm_mday,
        dt.tm_mon,
        dt.tm_year,
        dt.tm_hour,
        dt.tm_min
    ]

    selected = 0

    while True:

        # =================================================
        # DRAW SCREEN
        # =================================================

        clear()

        text(
            "SET DATE & TIME",
            18,
            1
        )

        # DATE

        date_text = "{:02d}/{:02d}/{:04d}".format(
            values[0],
            values[1],
            values[2]
        )

        text(
            date_text,
            28,
            20
        )

        # TIME

        time_text = "{:02d}:{:02d}".format(
            values[3],
            values[4]
        )

        text(
            time_text,
            43,
            34
        )

        # CURSOR

        cursor_x = [
            31,     # DAY
            47,     # MONTH
            65,     # YEAR
            46,     # HOUR
            64      # MINUTE
        ]

        cursor_y = [
            29,     # DAY
            29,     # MONTH
            29,     # YEAR
            43,     # HOUR
            43      # MINUTE
        ]

        text(
            "^",
            cursor_x[selected],
            cursor_y[selected]
        )

        text(
            "UP/DN CHANGE",
            20,
            49
        )

        show()

        # =================================================
        # READ BUTTON
        # =================================================

        button = get_button()

        if button is None:
            time.sleep(0.02)
            continue

        # =================================================
        # UP
        # =================================================

        if button == "UP":
            values[selected] += 1

        # =================================================
        # DOWN
        # =================================================

        elif button == "DOWN":
            values[selected] -= 1

        # =================================================
        # LEFT
        # =================================================

        elif button == "LEFT":

            selected -= 1

            if selected < 0:
                selected = 4

        # =================================================
        # RIGHT
        # =================================================

        elif button == "RIGHT":

            selected += 1

            if selected > 4:
                selected = 0

        # =================================================
        # BACK
        # =================================================

        elif button == "BACK":

            return False

        # =================================================
        # OK
        # =================================================

        elif button == "OK":

            # Set RTC
            set_datetime(
                values[0],
                values[1],
                values[2],
                values[3],
                values[4],
                0
            )

            # Save to SD
            if save_datetime():
                return True

            # SD save failed
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

        # =================================================
        # VALIDATE YEAR
        # =================================================

        if values[2] < 2000:
            values[2] = 2000

        if values[2] > 2099:
            values[2] = 2099

        # =================================================
        # VALIDATE MONTH
        # =================================================

        if values[1] < 1:
            values[1] = 12

        if values[1] > 12:
            values[1] = 1

        # =================================================
        # VALIDATE DAY
        # =================================================

        max_day = days_in_month(
            values[2],
            values[1]
        )

        if values[0] < 1:
            values[0] = max_day

        if values[0] > max_day:
            values[0] = 1

        # =================================================
        # VALIDATE HOUR
        # =================================================

        if values[3] < 0:
            values[3] = 23

        if values[3] > 23:
            values[3] = 0

        # =================================================
        # VALIDATE MINUTE
        # =================================================

        if values[4] < 0:
            values[4] = 59

        if values[4] > 59:
            values[4] = 0

        # =================================================
        # BUTTON DEBOUNCE
        # =================================================

        time.sleep(0.15)
