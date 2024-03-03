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

## Requirements
- Python 3.x
- Linux environment with UFW logs available through `dmesg`

Enjoy monitoring your network traffic and identifying potential security threats with `FirewallFalcon`!

This updated README provides a comprehensive overview of `FirewallFalcon`, including its purpose, setup instructions, usage, features, and requirements, tailored for users interested in analyzing UFW block events.