#!/usr/bin/python3
import sys

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Print accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    # Process input line by line
    for line in sys.stdin:
        parts = line.split()

        # Validate input format (should have at least 7 components)
        if len(parts) < 7:
            continue
        
        # Extract file size (last element) and status code (second last element)
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
        except ValueError:
            continue  # Skip lines with invalid integers

        # Update metrics
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_stats()
    sys.exit(0)
