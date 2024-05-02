#!/usr/bin/env python3
""" a script that reads stdin line by line and computes metrics """

import sys
import re
import signal


pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\ - \[.*\] "GET /projects/\d+ HTTP/1\.1" \d{3} \d+$' 
count = 0
total_size = 0
status_code_counts = {}

def signal_handler(sig, frame):
    print('Ctrl+C pressed, exiting gracefully...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def print_stats():
    print(f"File size: {total_size}")
    print(sorted(status_code_counts))


try:
    for line in sys.stdin:
        if re.match(pattern, line):
            count += 1
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_size += file_size
            status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

            if count % 10 == 0:
                print_stats()
                count = 0
            
        else:
            continue

except KeyboardInterrupt:
    print_stats()
    sys.exit()
