days = ("sunday", "monday", "tuesday", "wednesday", "thursday",
        "friday", "saturday")

f_day = int(input("""Enter the first day of the year
1 for sunday, 2 for monday and so on.\n"""))

day_of = int(input("which day number's day you wanna know?\n"))

day_index = (((day_of % 7) + (days.index(days[f_day - 1]))) % 7) - 1
print("It's", days[day_index])
