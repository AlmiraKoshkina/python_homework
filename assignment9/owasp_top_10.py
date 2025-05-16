from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os

# Ensure folder exists
os.makedirs("assignment9", exist_ok=True)

# Setup browser (can enable headless if you want)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the OWASP Top 10 page
url = "https://owasp.org/www-project-top-ten/"
driver.get(url)
time.sleep(5)

# Find all <li> elements that contain a link with a strong tag inside (the Top 10 items)
elements = driver.find_elements(By.XPATH, "//li[a/strong[starts-with(text(), 'A0')]]")

print(f"Found {len(elements)} OWASP items")

data = []
for li in elements:
    try:
        a_tag = li.find_element(By.TAG_NAME, "a")
        title = a_tag.text.strip()
        link = a_tag.get_attribute("href")
        data.append({"Title": title, "Link": link})
        print(f"{title} → {link}")
    except:
        continue

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("assignment9/owasp_top_10.csv", index=False)
print("\nCSV saved.")
print(df)

driver.quit()
