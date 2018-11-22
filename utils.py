import time

def log_debug(message):
    print time.ctime(), ":", message

def log_warning(message):
    print time.ctime(), ":", message

def log_error(message):
    print time.ctime(), ":", message

def parse_time(time_str):
    return time.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%f')

def format_time(time_obj):
    return time_obj.strftime('%Y-%m-%dT%H:%M:%S.%f')

def format_time_pretty(time_obj):
    return time_obj.strftime('%Y/%m/%d %H:%M:%S')
