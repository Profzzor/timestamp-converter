import time
import sys

# Example timestamp: 1710326777474000 (in milliseconds)
if len(sys.argv) != 2:
    print(f"Example: python3 {sys.argv[0]} 1710326777474000")
    exit()

# Timestamp in milliseconds
timestamp_ms = int(sys.argv[1])

# Convert milliseconds to seconds (downscale for large timestamps)
timestamp_s = timestamp_ms / 1000

# If the timestamp is too large, scale it down by dividing by a factor (e.g., 1000) or handle accordingly
if timestamp_s > 253402300799:  # Limit defined by the datetime module
    timestamp_s = timestamp_s / 1000  # Scale down (divide by 1000)

# Use time.gmtime() to handle the scaled timestamp
time_struct = time.gmtime(timestamp_s)

# Convert time_struct to a human-readable format
human_readable = time.strftime('%Y-%m-%d %H:%M:%S', time_struct)

# Print the date in a human-readable format
print(human_readable)
