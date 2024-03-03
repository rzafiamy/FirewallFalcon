import subprocess
import re
from datetime import datetime, timedelta
from collections import Counter

class ReportGenerator:
    def __init__(self):
        self.ufw_log_pattern = re.compile(r'\[(.*?)\].*\[UFW BLOCK\].*SRC=(\S+)')

    def _get_dmesg_output(self):
        return subprocess.check_output(['dmesg']).decode('utf-8')

    def _parse_logs(self):
        logs = self._get_dmesg_output()
        return [self.ufw_log_pattern.findall(line) for line in logs.splitlines() if '[UFW BLOCK]' in line]

    def _filter_logs_by_period(self, logs, period):
        now = datetime.now()
        filtered_logs = []
        for log in logs:
            log_date, ip = log[0], log[1]
            log_datetime = datetime.strptime(log_date, '%a %b %d %H:%M:%S %Y')
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
