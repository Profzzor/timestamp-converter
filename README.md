# Unix Timestamp Converter

This Python script converts Unix timestamps (in milliseconds) to a human-readable date and time format. The script is designed to handle large timestamps, and if the timestamp exceeds Python's `datetime` limits, it will scale the value down to ensure the conversion works.

## Features

- Converts **Unix timestamps** in **milliseconds** to a human-readable date and time.
- Automatically scales down timestamps that exceed Python's `datetime` limits (timestamps that go beyond the year 9999).
- Handles very large timestamps efficiently.
- Outputs the converted timestamp in the format `YYYY-MM-DD HH:MM:SS`.

## Requirements

- Python 3.x

## How to Use

### Step 1: Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/unixtimestamp-converter.git
cd unixtimestamp-converter
```

### Step 2: Run the Script
To run the script, use the following command:

```bash
python3 unixtimestamp.py <timestamp_in_milliseconds>
```
For example, if you want to convert the timestamp 1710326777474000, you would run:

```bash
python3 unixtimestamp.py 1710326777474000
2024-03-10 13:19:37
```
