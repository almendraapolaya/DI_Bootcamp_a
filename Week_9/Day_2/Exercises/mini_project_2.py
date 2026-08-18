##=========================
## Mini-Project 2: Scraping “Scrape This Site” - Frames Page
#==========================

# Task
#---------
# Initialize Selenium WebDriver
# Navigate to the Web Page : scrapethissite
# Since the page contains frames, identify each frame and switch to it to access its content.
# Use Selenium to navigate through frames and extract necessary data.
# After switching to a frame, use BeautifulSoup to parse and extract data.
# Focus on extracting specific information like text, links, or any other relevant content from each frame.
# Structure the extracted data into a structured format like a list of dictionaries or a pandas DataFrame.
# Save the data to a CSV file for further analysis or use.
# Properly close the Selenium WebDriver session.

# Expected Deliverables
#----------
# A Python script that successfully navigates the frames and scrapes data from the “Scrape This Site” Frames page.
# A CSV file or similar containing the structured data you extracted.

# Python Scraping Script

import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

# 1. Setup Chrome WebDriver automatically
chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

target_url = "https://www.scrapethissite.com/pages/frames/"
driver.get(target_url)
time.sleep(2)

extracted_data = []

try:
    # Get the inner iframe URL
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    frame_url = iframe.get_attribute("src")
    
    if frame_url:
        # Navigate directly into the iframe's target URL
        driver.get(frame_url)
        time.sleep(2)

        # Parse content inside the frame URL
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract titles, paragraphs, and headings inside the frame
        heading = soup.find(["h1", "h2", "h3", "h4"])
        heading_text = heading.get_text(strip=True) if heading else "N/A"
        
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
        body_text = " ".join(paragraphs) if paragraphs else soup.get_text(separator=" ", strip=True)

        links = [a["href"] for a in soup.find_all("a", href=True)]

        extracted_data.append({
            "frame_index": 0,
            "frame_url": frame_url,
            "heading": heading_text,
            "text_content": body_text[:300],
            "link_count": len(links),
            "links": "; ".join(links)
        })

finally:
    driver.quit()

# Exporting to CSV
csv_filename = "frames_scraped_data.csv"
if extracted_data:
    fieldnames = list(extracted_data[0].keys())
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(extracted_data)
    print(f"Scraping complete! Data saved to '{csv_filename}'.")