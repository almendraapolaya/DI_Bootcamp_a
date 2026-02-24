#
#===================================================
#🌟 Exercise 5: Amount of time left until January 1st
#===================================================
# Goal: Create a function that displays the amount of time left until January 1st.

# Instructions:
# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module
# Step 2: Get the current date and time
# Step 3: Create a datetime object for January 1st of the next year
# Step 4: Calculate the time difference
# Step 5: Display the time difference






import datetime

today = datetime.date.today()
january_1 = datetime.date(2027, 1, 1)

# def time_left():
time_left = january_1 - today
print(time_left)



