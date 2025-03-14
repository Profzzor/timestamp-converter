# Timestamp Converter

This Python scripts converts Unix timestamps (in milliseconds) and hex timestamps to a human-readable date and time format. The  `unixtimestamp.py` script is designed to handle large timestamps, and if the timestamp exceeds Python's `datetime` limits, it will scale the value down to ensure the conversion works.

## Features

- Converts **timestamps** into human-readable date and time.
- Automatically scales down timestamps that exceed Python's `datetime` limits (timestamps that go beyond the year 9999).
- Handles very large timestamps efficiently.
- Outputs the converted timestamp in the format `YYYY-MM-DD HH:MM:SS`.

## Requirements

- Python 3.x

## How to Use

### Step 1: Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/Profzzor/timestamp-converter.git
cd timestamp-converter
```

### Step 2: Run the Script
To run the script, use the following command:

```bash
python3 unixtimestamp.py <timestamp_in_milliseconds>
python3 hextoutc.py <timestamp_in_hex>
```
Example, if you want to convert the timestamp 1710326777474000, you would run:

```bash
python3 unixtimestamp.py 1710326777474000
2024-03-10 13:19:37
```
if you want to convert the timestamp 1710326777474000, you would run:

```bash
python3 hextoutc.py 1909fa2050b
Installation Time (UTC): 2024-07-11 02:31:53.867000
```
