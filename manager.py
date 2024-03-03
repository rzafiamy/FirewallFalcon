import argparse
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description='Generate a report of IP blocked by UFW by Day/Month/Week/Year.')
    parser.add_argument('--period', type=str, choices=['day', 'month', 'week', 'year'], required=True,
                        help='The period to generate the report for (day, month, week, year)')
    args = parser.parse_args()

    report_generator = ReportGenerator()
    report_generator.generate_report(args.period)

if __name__ == "__main__":
    main()