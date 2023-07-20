#!/usr/bin/python3
"""
    A script that reads stdin line by line and computes metrics
"""
import sys
import signal

def print_statistics(file_sizes, status_codes):
    total_size = sum(file_sizes)
    print(f"Total file size: File size: {total_size}")

    for status_code in sorted(status_codes):
        if status_code in valid_status_codes:
            print(f"{status_code}: {status_codes[status_code]}")

def parse_line(line):
    parts = line.split()
    if len(parts) != 10 or not parts[6].isdigit():
        return None, None

    ip_address = parts[0]
    status_code = int(parts[8])
    file_size = int(parts[9])

    return status_code, file_size

valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
file_sizes = []
status_codes = {}

try:
    line_count = 0
    for line in sys.stdin:
        status_code, file_size = parse_line(line.strip())
        if status_code is None:
            continue

        file_sizes.append(file_size)
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics(file_sizes, status_codes)

except KeyboardInterrupt:
    print_statistics(file_sizes, status_codes)
    sys.exit(0)
