#!/usr/bin/env python
"""
This script reads from stdin line by line and computes metrics
based on the input log data.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code>
<file size>

After every 10 lines and/or a keyboard interruption (CTRL + C), it prints the
following statistics from the beginning:
- Total file size: File size: <total size>
- Number of lines by status code in ascending order of status code

Possible status codes: 200, 301, 400, 401, 403, 404, 405, 500
"""

import sys
import signal
import re

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Define a regular expression pattern to match the log lines
log_pattern = re.compile(
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)

# Signal handler for keyboard interruption


def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)


def print_metrics():
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


# Read lines from stdin
try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            total_size += file_size

            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_metrics()
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
finally:
    print_metrics()
