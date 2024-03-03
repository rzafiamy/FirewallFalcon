# FirewallFalcon

## Description
`FirewallFalcon` is a Python-based tool designed to generate reports of IP addresses blocked by UFW (Uncomplicated Firewall) over specified periods: day, month, week, or year. It parses the system's `dmesg` output to identify and summarize firewall block events, offering insights into the frequency and distribution of attacks over time.

## Setup
- Ensure Python 3 is installed on your system.
- No external Python packages are required as `FirewallFalcon` uses the standard Python library.

## Usage
To use `FirewallFalcon`, run the script with the period parameter to specify the time frame for the report:

```bash
python manager.py --period [day|month|week|year]
```

This command will parse the `dmesg` log for UFW block entries and generate a summary report for the specified time period, displaying the count of blocks per IP address.

## Features
- Easy to use: Simple command-line interface.
- Versatile reporting: Generate summaries by day, month, week, or year.
- No external dependencies: Utilizes Python’s standard library.

## Configuration

Edit `config.py` for Locale and Date formatting 

## Requirements
- Python 3.x
- Linux environment with UFW logs available through `dmesg`

Enjoy monitoring your network traffic and identifying potential security threats with `FirewallFalcon`!

This updated README provides a comprehensive overview of `FirewallFalcon`, including its purpose, setup instructions, usage, features, and requirements, tailored for users interested in analyzing UFW block events.


## Output examples 


----------------------------------------------------------------------
|          Date         |        IP       | Destination Port | Count |
|-----------------------|-----------------|------------------|-------|
| mars  3 06:29:56 2024 |   1.14.250.37   |       8088       |   1   |
| mars  3 05:02:38 2024 |    1.24.16.71   |       8443       |   1   |
| mars  3 06:51:21 2024 |  1.117.219.226  |       8090       |   1   |
| mars  3 07:37:54 2024 |    3.9.16.57    |       1988       |   1   |
| mars  3 05:42:19 2024 |   5.10.250.241  |       3389       |   1   |
| mars  3 03:14:59 2024 |   5.188.206.14  |       7815       |   1   |
| mars  3 03:25:38 2024 |   5.188.206.14  |      18134       |   1   |
| mars  3 03:50:38 2024 |   5.188.206.14  |      24187       |   1   |
| mars  3 03:54:54 2024 |   5.188.206.14  |      10924       |   1   |
| mars  3 03:58:24 2024 |   5.188.206.14  |      26868       |   1   |
| mars  3 04:56:16 2024 |   5.188.206.14  |      15059       |   1   |
| mars  3 05:47:18 2024 |   5.188.206.14  |      33297       |   1   |
