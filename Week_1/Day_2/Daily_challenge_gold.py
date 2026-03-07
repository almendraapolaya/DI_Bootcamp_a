#=============================
#Daily challenge GOLD : Happy birthday
#=============================
# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !

import calendar
from datetime import datetime

birth_str = input("Enter your birthdate (DD/MM/YYYY): ")
birth_date = datetime.strptime(birth_str, "%d/%m/%Y")
today = datetime.now()

age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

num_candles = age % 10 
candle_row = ("i" * num_candles).center(11, "_")

is_leap = calendar.isleap(birth_date.year)

cake_template = f"""
    
      _{candle_row}_
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

print(f"Age: {age}")
print(cake_template)

if is_leap:
    print("Leap year bonus!")
    print(cake_template)