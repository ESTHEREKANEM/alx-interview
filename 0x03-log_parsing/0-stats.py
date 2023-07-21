#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics"""


import sys


def print_output(status_code, total_size):
    """prints stdout output"""
    print("File size: {}".format(total_size))
    for code in sorted(status_code.keys()):
        if status_code[code] != 0:
            print("{}: {}".format(code, status_code[code]))


status_code_obj = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}
summation = 0
count = 0

try:
    for line in sys.stdin:
        data = line.split(" ")
        status_c = data[7]
        file_size = data[8]
        status_code = int(status_c)
        size = int(file_size)
        if status_code in status_code_obj:
            status_code_obj[status_code] += 1
        summation += size
        count += 1
        if count % 10 == 0:
            print_output(status_code_obj, summation)
    print_output(status_code_obj, summation)

except KeyboardInterrupt:
    print_output(status_code_obj, summation)
