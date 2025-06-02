from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time

# Set up the Chrome driver (headless mode = no browser window)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # run in background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the search results page
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)
time.sleep(2)  # wait a bit to allow page to load

# Find all <li> elements representing individual books
book_items = driver.find_elements(By.CLASS_NAME, "cp-search-result-item")
print(f"Found {len(book_items)} books")

results = []

# Loop through each book item
for li in book_items:
    try:
        # Get the book title
        title = li.find_element(By.CLASS_NAME, "title-content").text.strip()
    except:
        title = "N/A"

    try:
        # Get the authors
        author_elements = li.find_elements(By.CLASS_NAME, "author-link")
        authors = "; ".join([a.text.strip() for a in author_elements])
    except:
        authors = "N/A"

    try:
        # Get the format and year info
        format_year = li.find_element(By.CLASS_NAME, "display-info-primary").text.strip()
    except:
        format_year = "N/A"

    # Add the collected data to the results list
    results.append({
        "Title": title,
        "Author": authors,
        "Format-Year": format_year
    })

# Create a DataFrame and print it
df = pd.DataFrame(results)
print(df)

# Write the DataFrame to CSV
df.to_csv("assignment9/get_books.csv", index=False)

# Write the raw data to JSON
with open("assignment9/get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

# Close the browser session
driver.quit()
