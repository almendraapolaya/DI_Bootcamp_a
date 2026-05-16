##========================
## Mini Project 1: Scraping Data from a Dynamic Webpage
##========================
#.      Task
# Initialize Selenium WebDriver
# Load the Web Page
# Identify the elements that contain hosting plan details.
# Extract necessary data such as plan names, features, and pricing.
# Store and Save the Data
# Close Selenium WebDriver



import csv
import time
import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup

# --- 1. Initialize Selenium WebDriver ---
chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    # --- 2. Load the Web Page ---
    print("Connecting to InMotion Hosting...")
    url = "https://www.inmotionhosting.com/shared-hosting"
    driver.get(url)
    
    time.sleep(6)

    # --- 3. Parse Content ---
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    plan_cards = soup.find_all(['div', 'section'], class_=lambda x: x and ('product-card' in x.lower() or 'pricing-card' in x.lower() or 'wp-block-column' in x.lower()))

    scraped_plans = []

    print(f"Analyzing webpage structures...")

    for card in plan_cards:
        name_tag = card.find(['h3', 'h4'])
        price_tag = card.find(class_=lambda x: x and ('price' in x.lower() or 'amount' in x.lower()))
        features_list = card.find('ul')
        features = [li.text.strip() for li in features_list.find_all('li')] if features_list else []
        
        if name_tag and price_tag:
            plan_name = name_tag.get_text(strip=True)
            price_value = price_tag.get_text(strip=True)
            
            if len(plan_name) > 30 or not price_value:
                continue
                
            scraped_plans.append({
                'Plan Name': plan_name,
                'Pricing': price_value,
                'Key Features': ", ".join(features[:3]) if features else "Standard Features"
            })

    if not scraped_plans:
        print("Using alternative parsing fallback...")
        for h3 in soup.find_all(['h3', 'h4']):
            parent = h3.find_parent(['div', 'section'])
            if parent:
                price = parent.find(class_=lambda x: x and 'price' in x.lower())
                if price:
                    scraped_plans.append({
                        'Plan Name': h3.get_text(strip=True),
                        'Pricing': price.get_text(strip=True),
                        'Key Features': "Included Features"
                    })

    # --- 4. Store and Save the Data ---
    if scraped_plans:
        unique_plans = [dict(t) for t in {tuple(d.items()) for d in scraped_plans}]
        
        keys = unique_plans[0].keys()
        with open('hosting_plans.csv', 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(unique_plans)
        
        print(f"\n Success! Extracted plans and saved them to 'hosting_plans.csv'.")
    else:
        print("\nLayout verification failed. Try using a simpler target page like 'https://www.inmotionhosting.com/' landing overview.")

finally:
    # --- 5. Close Selenium WebDriver ---
    driver.quit()