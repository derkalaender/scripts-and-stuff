from datetime import datetime, timedelta


def get_advent_number():
    # first advent is always the first sunday after the 26th of november
    before_advent = datetime(datetime.today().year, 11, 26)

    # calculate first advent by adding the missing days till sunday
    first_advent = before_advent + timedelta(days=6 - before_advent.weekday())

    # calculate all the advents
    advents = [first_advent+timedelta(days=days) for days in range(0, 4*7, 7)]

    num = 0
    for x in advents:
        if datetime.today() == x:
            num = advents.index(x) + 1

    return num


advent_number = get_advent_number()
print(f"It's the #{get_advent_number()} Advent everybody!" if advent_number != 0 else f"No Advent today.")
