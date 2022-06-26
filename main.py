import re
from datetime import datetime


def is_between_times(time, start_time, end_time):
    format_time = '%H:%M:%S'

    current_time = datetime.strptime(time, format_time)
    start_time = datetime.strptime(start_time, format_time)
    end_time = datetime.strptime(end_time, format_time)
    return start_time <= current_time <= end_time


def use_regex(pattern, string):
    result = re.search(pattern, string)
    if result:
        return result.group()


def filter_logs(word, day, start_time, end_time, file_path):
    regex_date = day + '/Jul/1995'
    regex_time = r'[0-9]{2}:[0-9]{2}:[0-9]{2} '
    results = []

    with open(file_path, 'r') as access_log_Jul95:
        for line in access_log_Jul95:
            if use_regex(word, line) and \
                    use_regex(regex_date, line) and \
                    is_between_times(use_regex(regex_time, line).strip(), start_time, end_time):
                results.append(line)
    return results


if __name__ == '__main__':
    filtered_logs = filter_logs('NASA', '01', '00:10:00', '00:20:00', 'access_log_Jul95')
    print(len(filtered_logs))
    print(filtered_logs)
