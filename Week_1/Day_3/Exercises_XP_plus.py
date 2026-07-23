######################
# EXERCISES XP +
######################

# Exercise 1: Student Grade Summary
#========================================
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# 1. Calculate the average grade for each student and store the results in a new dictionary called student_averages
student_averages = {}
student_letter_grades = {}

# 2. Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
for name, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    student_averages[name] = avg
    
    if avg >= 90:
        letter = 'A'
    elif avg >= 80:
        letter = 'B'
    elif avg >= 70:
        letter = 'C'
    elif avg >= 60:
        letter = 'D'
    else:
        letter = 'F'
        
    student_letter_grades[name] = letter

# 3. Calculate class average
class_average = sum(student_averages.values()) / len(student_averages)

# 4. Print the name of each student, their average grade, and their letter grade.
print("--- Student Grade Summary ---")
for name in student_grades:
    avg = student_averages[name]
    letter = student_letter_grades[name]
    print(f"{name}: Average = {avg:.2f}, Grade = {letter}")

print("-" * 29)
print(f"Class Average: {class_average:.2f}")

#=========================================
#  Exercise 2 : Advanced Data Manipulation and Analysis
#=========================================

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# Task 1: Total Sales Calculation
for transaction in sales_data:
    transaction["total_price"] = transaction["price"] * transaction["quantity"]

# Task 2: Total Sales by Product Category 
category_sales = {}
for transaction in sales_data:
    product = transaction["product"]
    category_sales[product] = category_sales.get(product, 0) + transaction["total_price"]

# Task 3: Customer Spending Profile 
customer_spending = {}
for transaction in sales_data:
    customer = transaction["customer_id"]
    customer_spending[customer] = customer_spending.get(customer, 0) + transaction["total_price"]

# Task 4: High-Value Transactions 
high_value_transactions = [
    tx for tx in sales_data if tx["total_price"] > 500
]
high_value_transactions.sort(key=lambda tx: tx["total_price"], reverse=True)

# Task 5: Customer Loyalty Identification 
purchase_counts = {}
for transaction in sales_data:
    customer = transaction["customer_id"]
    purchase_counts[customer] = purchase_counts.get(customer, 0) + 1

loyal_customers = [cust for cust, count in purchase_counts.items() if count > 1]

#  Bonus: Insights and Analysis 
# A) Average transaction value per product category
product_tx_counts = {}
for transaction in sales_data:
    product = transaction["product"]
    product_tx_counts[product] = product_tx_counts.get(product, 0) + 1

avg_tx_value_per_category = {
    product: category_sales[product] / product_tx_counts[product]
    for product in category_sales
}

# B) Most popular product based on total quantity sold
product_quantities = {}
for transaction in sales_data:
    product = transaction["product"]
    product_quantities[product] = product_quantities.get(product, 0) + transaction["quantity"]

most_popular_product = max(product_quantities, key=product_quantities.get)

print("=== RETAIL SALES ANALYSIS SUMMARY ===")
print("\n1. Total Sales per Category:")
for product, total in category_sales.items():
    print(f"   - {product}: ${total:,.2f}")

print("\n2. Customer Spending Profile:")
for customer_id, total in customer_spending.items():
    print(f"   - Customer {customer_id}: ${total:,.2f}")

print("\n3. High-Value Transactions (> $500):")
for tx in high_value_transactions:
    print(f"   - Customer {tx['customer_id']} bought {tx['product']} for ${tx['total_price']:,.2f} on {tx['date']}")

print("\n4. Loyal Customers (More than 1 purchase):")
print(f"   - Customer IDs: {', '.join(map(str, loyal_customers))}")

print("\n5. Bonus Metrics:")
print("   - Average Transaction Value per Category:")
for product, avg_val in avg_tx_value_per_category.items():
    print(f"     * {product}: ${avg_val:,.2f}")
print(f"   - Most Popular Product (by Quantity): {most_popular_product} ({product_quantities[most_popular_product]} units)")