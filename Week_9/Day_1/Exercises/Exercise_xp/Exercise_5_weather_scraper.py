## 
### Exercise 5 : Scrape and Analyze Weather Data from a JavaScript-Enabled Weather Website


import time
from statistics import mean
from collections import Counter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print("Navigating to AccuWeather...")
    url = "https://www.accuweather.com/en/us/attica/30607/weather-forecast/2139413"
    driver.get(url)
    
    time.sleep(7)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    forecast_cards = soup.find_all('div', class_='forecast-list-card')
    
    temps = []
    conditions = []

    print(f"Scraping {len(forecast_cards)} days of data...\n")

    for card in forecast_cards:
        temp_tag = card.find('span', class_='high')
        if temp_tag:
            temp_val = int(temp_tag.text.replace('°', '').strip())
            temps.append(temp_val)

        cond_tag = card.find('span', class_='phrase')
        if cond_tag:
            conditions.append(cond_tag.text.strip())

    # --- Analysis ---
    if temps:
        avg_temp = mean(temps)
        most_common_cond = Counter(conditions).most_common(1)[0][0]

        print("--- WEATHER ANALYSIS RESULTS ---")
        print(f"Average High Temp: {avg_temp:.1f}°")
        print(f"Most Common Condition: {most_common_cond}")
        print(f"Temperature Range: {min(temps)}° to {max(temps)}°")
        print("-" * 30)
    else:
        print("Could not find forecast data. Check if the page layout changed.")

finally:
    driver.quit()