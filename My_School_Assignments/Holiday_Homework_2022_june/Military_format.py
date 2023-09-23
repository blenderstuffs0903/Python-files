def mod(value):
    if value < 0:
        '''returns the absolute value'''
        value = -1 * value
    return value


m_time1 = input("Enter 1st M_time\n")
m_time2 = input("Enter 2nd M_time\n")

# Converts both times to minutes
mins_1 = int(m_time1[:2]) * 60 + int(m_time1[2:])
mins_2 = int(m_time2[:2]) * 60 + int(m_time2[2:])

# Subtracting the minutes
diff = mod(mins_2 - mins_1)

# Convert the difference to hours & mins
hrs = diff // 60
mins = diff % 60

print(hrs, "hours", mins, "minutes")
