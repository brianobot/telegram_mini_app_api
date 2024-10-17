from datetime import datetime, timedelta


def seconds_until_next_day() -> int:
    now = datetime.now()
    next_day = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    time_difference = next_day - now
    return int(time_difference.total_seconds())

