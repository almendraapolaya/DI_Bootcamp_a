
#======================================
# 🌟 Exercise 6: Birthday and minutes
#======================================
# Key Python Topics:
# datetime module
# datetime.datetime.strptime() (parsing dates)
# Time difference calculations
# .total_seconds() method

# Instructions:
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.


from datetime import datetime


def calculate_minutes_lived(birthday_str):

    date_format = "%d/%m/%Y %H:%M:%S"
    now = datetime.now()
    birth_date = datetime.strptime(birthday_str, date_format)
    delta = now - birth_date
    minutes = int(delta.total_seconds() / 60)
    print(f"You have lived for approximately {minutes:,} minutes!")


my_birthday = "02/10/1993 19:30:10"
calculate_minutes_lived(my_birthday)








