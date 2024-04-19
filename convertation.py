import datetime


def convert_str_to_float(text):
    seconds_str, microseconds_str = text.split('.')
    seconds = int(seconds_str)
    microseconds = int(microseconds_str)
    total_microseconds = seconds * 10 ** 6 + microseconds
    return total_microseconds