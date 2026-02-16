# 
#=========================================
# Exercises XP Gold
#-----------------------------------------
#
#=========================================
# #Exercise 1 : Hello World-I love Python
#=========================================
# Instructions
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python

print(("Hello world\n"* 4) + ("I love python\n") * 4)

#==========================================
#Exercise 2 : What is the Season ?
#==========================================
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

month_input = int(input("Please type a month(1-12) to know the season: "))

if 3 <= month_input <= 5:
    print("It's Spring")
elif 6 <= month_input <= 8:
    print("It's Summer")
elif 9 <= month_input <= 11:
    print("It's Autumn")
elif month_input in [12, 1, 2]:
    print("It's Winter")
    
   