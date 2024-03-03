import subprocess
import re
from datetime import datetime, timedelta
from collections import Counter
from prettytable import PrettyTable
from config import LOCALE_LANG, DATE_FORMAT

import locale

locale.setlocale(locale.LC_TIME, LOCALE_LANG)

class ReportGenerator:
    def __init__(self):
        # Updated regex to also capture the destination port (DPT)
        self.ufw_log_pattern = re.compile(r'\[.*?\s(\w+\s+\d+\s+\d+:\d+:\d+\s+\d+)\].*\[UFW BLOCK\].*SRC=(\S+).*DPT=(\d+)')

    def _get_dmesg_output(self):
        try:
            return subprocess.check_output(['dmesg', '-T'], stderr=subprocess.STDOUT).decode('utf-8')
        except subprocess.CalledProcessError:
            print("Failed to execute dmesg. Please ensure you have the necessary permissions.")
            print("Consider running the script with sudo or providing a file with dmesg output.")
            exit(1)

    def _parse_logs(self):
        logs = self._get_dmesg_output()
        parsed_logs = []
        for line in logs.splitlines():
            match = self.ufw_log_pattern.search(line)
            if match:
                # Now capturing date, IP, and destination port
                parsed_logs.append((match.group(1), match.group(2), match.group(3)))
        return parsed_logs

    def _filter_logs_by_period(self, logs, period):
        now = datetime.now()
        filtered_logs = []
        for log in logs:
            log_date, ip, dpt = log
            log_datetime = datetime.strptime(log_date, DATE_FORMAT)
            if self._is_in_period(log_datetime, period, now):
                filtered_logs.append((log_date, ip, dpt))
        return filtered_logs

    def _is_in_period(self, log_datetime, period, now):
        if period == 'day' and now.date() == log_datetime.date():
            return True
        elif period == 'month' and now.month == log_datetime.month and now.year == log_datetime.year:
            return True
        elif period == 'week':
            week_start = now - timedelta(days=now.weekday())
            week_end = week_start + timedelta(days=6)
            if week_start <= log_datetime <= week_end:
                return True
        elif period == 'year' and now.year == log_datetime.year:
            return True
        return False

    def generate_report(self, period):
        logs = self._parse_logs()
        filtered_logs = self._filter_logs_by_period(logs, period)
        counts = Counter(filtered_logs)

        # Sort by IP address; convert IP to a tuple of integers for correct numerical sorting
        sorted_counts = sorted(counts.items(), key=lambda x: tuple(int(part) for part in x[0][1].split('.')))

        table = PrettyTable()
        table.field_names = ["Date", "IP", "Destination Port", "Count"]
        for log, count in sorted_counts:
            date, ip, dpt = log
            table.add_row([date, ip, dpt, count])

        print(table)