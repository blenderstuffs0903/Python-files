def is_leap(entered_year):
    if entered_year % 4 == 0:
        if entered_year % 100 == 0:
            if entered_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(entered_year, entered_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(entered_year):
        month_days[1] = 29
    return month_days[entered_month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
