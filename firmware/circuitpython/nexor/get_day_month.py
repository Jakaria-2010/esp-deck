DAY_NAMES = ["Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat" , "Sun"]

MONTH_NAMES = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "JUl" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec"]

def get_home_date(dt):
    # Sakamoto weekday calculation. Sunday=0 ... Saturday=6.
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y = dt.tm_year - (1 if dt.tm_mon < 3 else 0)
    sunday_based = (y + y // 4 - y // 100 + y // 400 +
                    t[dt.tm_mon - 1] + dt.tm_mday) % 7
    weekday = (sunday_based - 1) % 7  # Monday=0 ... Sunday=6
    return "{}  {} {}".format(
        DAY_NAMES[weekday],
        dt.tm_mday,
        MONTH_NAMES[dt.tm_mon - 1]
    )

