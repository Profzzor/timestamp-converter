import datetime, sys

def convert_hex_timestamp(hex_timestamp):
    # Convert hex to integer (milliseconds since Unix epoch)
    timestamp_ms = int(hex_timestamp, 16)
    
    # Convert to human-readable UTC format
    timestamp_utc = datetime.datetime.utcfromtimestamp(timestamp_ms / 1000)
    
    return timestamp_utc

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <timestamp>")
    print(f"Example: python {sys.argv[0]} 1909fa2050b")
    exit()

hex_timestamp = sys.argv[1]  # Replace with your hex timestamp
install_time_utc = convert_hex_timestamp(hex_timestamp)
print("Installation Time (UTC):", install_time_utc)
