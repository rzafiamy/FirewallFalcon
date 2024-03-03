import subprocess
import re
from datetime import datetime, timedelta
from collections import Counter
from config import LOCALE_LANG, DATE_FORMAT

import locale

locale.setlocale(locale.LC_TIME, LOCALE_LANG)

class ReportGenerator:
    def __init__(self):
        self.ufw_log_pattern = re.compile(r'\[.*?\s(\w+\s+\d+\s+\d+:\d+:\d+\s+\d+)\].*\[UFW BLOCK\].*SRC=(\S+)')

    def _get_dmesg_output(self):
        try:
            return subprocess.check_output(['dmesg'], stderr=subprocess.STDOUT).decode('utf-8')
        except subprocess.CalledProcessError as e:
            print("Failed to execute dmesg. Please ensure you have the necessary permissions.")
            print("Consider running the script with sudo or providing a file with dmesg output.")
            exit(1)

    def _parse_logs(self):
        logs = self._get_dmesg_output()
        parsed_logs = []
        for line in logs.splitlines():
            match = self.ufw_log_pattern.search(line)
            if match:
                # Ensure that both date and IP are captured before adding to the list
                parsed_logs.append((match.group(1), match.group(2)))
        return parsed_logs

    def _filter_logs_by_period(self, logs, period):
        now = datetime.now()
        filtered_logs = []
        for log in logs:
            log_date, ip = log[0], log[1]
            log_datetime = datetime.strptime(log_date, DATE_FORMAT)
            if period == 'day' and now.date() == log_datetime.date():
                filtered_logs.append(ip)
            elif period == 'month' and now.month == log_datetime.month and now.year == log_datetime.year:
                filtered_logs.append(ip)
            elif period == 'week':
                week_start = now - timedelta(days=now.weekday())
                week_end = week_start + timedelta(days=6)
                if week_start <= log_datetime <= week_end:
                    filtered_logs.append(ip)
            elif period == 'year' and now.year == log_datetime.year:
                filtered_logs.append(ip)
        return filtered_logs

    def generate_report(self, period):
        logs = self._parse_logs()
        filtered_ips = self._filter_logs_by_period(logs, period)
        ip_count = Counter(filtered_ips)
        for ip, count in ip_count.items():
            print(f'{ip}: {count}')
