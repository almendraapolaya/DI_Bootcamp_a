import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # 1. Navigate to the page:
    print("Opening Rotten Tomatoes...")
    url = "https://www.rottentomatoes.com/browse/movies_at_home/critics:certified_fresh"
    driver.get(url)
    
    # 2. Wait for JavaScript to load the movie list:
    time.sleep(5) 

    # 3. Get the fully rendered HTML:
    html = driver.page_source

    # 4. Use BeautifulSoup:
    soup = BeautifulSoup(html, 'html.parser')

    movie_tiles = soup.find_all('div', class_='js-tile-link')

    print(f"Success! Found {len(movie_tiles)} movies.\n")
    print("-" * 30)

    for tile in movie_tiles:
        title = tile.find('span', class_='p--small').text.strip() if tile.find('span', class_='p--small') else "Unknown Title"
        
        # Get Critics Score:
        score = tile.find('rt-text', slot='criticsScore').text.strip() if tile.find('rt-text', slot='criticsScore') else "N/A"
        
        # Get Release Date:
        date = tile.find('span', class_='smaller').text.strip() if tile.find('span', class_='smaller') else "N/A"

        print(f"🎬 {title}")
        print(f"   Score: {score} | Release: {date}")
        print("-" * 30)

finally:
    driver.quit()