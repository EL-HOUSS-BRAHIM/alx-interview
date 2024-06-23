#!/usr/bin/python3
import sys
import re
import signal

# Initialize counters
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_file_size = 0
line_count = 0

# Define the regex pattern for the log line format
pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

def print_stats():
    """Print the accumulated metrics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption signal"""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
try:
    for line in sys.stdin:
        line = line.strip()
        match = pattern.match(line)
        if match:
            ip_address, timestamp, status_code, file_size = match.groups()
            file_size = int(file_size)

            # Update counters
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print final stats after the loop
print_stats()
