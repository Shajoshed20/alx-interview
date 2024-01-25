#!/usr/bin/python3

import sys
from collections import defaultdict

def print_statistics(total_size, status_codes):
    print(f'Total file size: {total_size}')
    for code in sorted(status_codes):
        print(f'{code}: {status_codes[code]}')

def process_line(line, total_size, status_codes):
    try:
        parts = line.split()
        size = int(parts[-1])
        status_code = int(parts[-2])

        total_size += size
        status_codes[status_code] += 1

    except (ValueError, IndexError):
        # Skip lines with invalid format
        pass

    return total_size, status_codes

def main():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_codes = process_line(line.strip(), total_size, status_codes)
            line_count += 1

            if line_count == 10:
                print_statistics(total_size, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()
