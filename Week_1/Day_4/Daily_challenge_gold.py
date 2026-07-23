#=======================
# Daily challenge Gold: Solve the Matrix
#=======================

import re

#  Matrix String
MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

#  STEP 1: Transform String into a 2D List (Matrix) 
lines = [line for line in MATRIX_STR.split('\n') if line != '']

# Convert each line into a list of characters (representing rows)
matrix = [list(line) for line in lines]


#  STEP 2 and 3: Process Columns & Filter Characters 
num_rows = len(matrix)
num_cols = len(matrix[0])  

raw_column_text = ""
# Iterate column by column (left to right, top to bottom)
for col in range(num_cols):
    for row in range(num_rows):
        if col < len(matrix[row]):
            raw_column_text += matrix[row][col]


#  STEP 4 and 5: Replace Symbols between Letters with Spaces & Print 
# Using regular expressions (re.sub) to target groups of non-alpha characters
# (?<=[a-zA-Z]) checks that a letter comes BEFORE the non-alpha group
# (?=[a-zA-Z])  checks that a letter comes AFTER the non-alpha group
clean_middle = re.sub(r'(?<=[a-zA-Z])[^a-zA-Z]+(?=[a-zA-Z])', ' ', raw_column_text)
decoded_message = re.sub(r'^[^a-zA-Z]+|[^a-zA-Z]+$', '', clean_middle)


print("=== MATRIX DECODED MESSAGE ===")
print(decoded_message)