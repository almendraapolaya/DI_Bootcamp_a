#
#Exercise 4 : Scrape and Categorize News Articles from a JavaScript-Enabled News Site
#

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print("Navigating to BBC Technology...")
    url = "https://www.bbc.com/technology"
    driver.get(url)
    time.sleep(5) 

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    articles_data = []
    
    containers = soup.find_all(['div', 'section'], class_=lambda x: x and 'promo' in x)

    for item in containers:
        title_tag = item.find(['h2', 'h3'])
        time_tag = item.find('time')
        
        if title_tag and time_tag:
            title = title_tag.text.strip()
            date_str = time_tag.get('datetime')
            if title and date_str:
                articles_data.append((title, date_str))

    categorized = {}
    for title, date_str in articles_data:
        try:
            clean_date = datetime.strptime(date_str[:10], '%Y-%m-%d')
            month = clean_date.strftime('%B')
            
            if month not in categorized:
                categorized[month] = []
            categorized[month].append(title)
        except:
            continue

    if not categorized:
        print("Still 0 articles?")
        for h in soup.find_all(['h2', 'h3']):
            print(f"Found headline: {h.text.strip()}")
    else:
        for month, titles in categorized.items():
            print(f"\n {month.upper()}")
            for t in set(titles): 
                print(f" - {t}")

finally:
    driver.quit()