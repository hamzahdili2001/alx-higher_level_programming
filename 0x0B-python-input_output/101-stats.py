#!/usr/bin/python3

import sys

totalFileSize = 0
statusCodeCounts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
lineCount = 0


def print_info():
    print("File size: {}".format(totalFileSize))
    for code in sorted(statusCodeCounts.keys()):
        if statusCodeCounts[code] > 0:
            print("{}: {}".format(code, statusCodeCounts[code]))


def add_status_code(status):
    if status in statusCodeCounts:
        statusCodeCounts[status] += 1


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 9:
            statusCode = parts[-2]
            fileSize = int(parts[-1])

            totalFileSize += fileSize
            add_status_code(statusCode)
            lineCount += 1

        if lineCount % 10 == 0:
            print_info()

except KeyboardInterrupt:
    print_info()
    raise
