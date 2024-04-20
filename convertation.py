
def convert_datetime_to_float(text):
    minutes_str, seconds_str, microseconds_str = text.split('.')
    minutes = int(minutes_str)
    seconds = int(seconds_str)
    microseconds = int(microseconds_str)
    total_microseconds = (minutes * 60 * 10**6) + (seconds * 10**6) + microseconds
    return total_microseconds