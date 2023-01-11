import sys
import signal

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    print("Total file size: ", total_size)
    for status_code in sorted(status_codes.keys()):
        print(status_code, ": ", status_codes[status_code])

total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

line_count = 0

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    # Parse the line to get the information
    ip, timestamp, request, status_code, file_size = line.strip().split(" ")
    status_code = int(status_code)
    file_size = int(file_size)
    
    # Update the statistics
    total_size += file_size
    if status_code in status_codes:
        status_codes[status_code] += 1
    
    line_count += 1
    if line_count % 10 == 0:
        print_stats()
