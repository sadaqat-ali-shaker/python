# Author: Sadaqat
# Date Calculator in Python without using datetime or any built-in libraries

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def parse_date(date_str):
    year, month, day = map(int, date_str.split('-'))
    return year, month, day

def total_days_since_start(year, month, day):
    days = 0
    for y in range(1, year):
        days += 366 if is_leap_year(y) else 365
    for m in range(1, month):
        days += days_in_month(m, year)
    days += day
    return days

def days_between(start_date, end_date):
    y1, m1, d1 = parse_date(start_date)
    y2, m2, d2 = parse_date(end_date)

    days1 = total_days_since_start(y1, m1, d1)
    days2 = total_days_since_start(y2, m2, d2)

    return abs(days2 - days1)

def estimate_months_days(total_days):
    months = total_days // 30
    days = total_days % 30
    return months, days

def estimate_weeks_days(total_days):
    weeks = total_days // 7
    days = total_days % 7
    return weeks, days

def show_difference(start_date, end_date):
    total = days_between(start_date, end_date)
    months, mdays = estimate_months_days(total)
    weeks, wdays = estimate_weeks_days(total)
    print(f"\nDifference between {start_date} and {end_date}:\n")
    print(f"{months} months {mdays} days")
    print(f"or {weeks} weeks {wdays} days")
    print(f"or {total} calendar days")

if __name__ == "__main__":
    print("Date Difference Calculator (No built-in libraries)")
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    show_difference(start, end)
