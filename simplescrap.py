from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

# ✅ Connect to Chrome (debug mode)
options = Options()
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)

time.sleep(5)

print("\n--- BOOKS DATA ---")

# ✅ Get all rows
rows = driver.find_elements(By.XPATH, "//table//tr[td]")
print("Books found:", len(rows))

data = []

for row in rows:
    try:
        # ✅ Extract title
        title = row.find_element(
            By.XPATH, ".//td[contains(@class,'title')]//a"
        ).get_attribute("textContent").strip()

        # ✅ Extract author
        author = row.find_element(
            By.XPATH, ".//td[contains(@class,'author')]//a"
        ).get_attribute("textContent").strip()

        # ✅ Debug print
        print("Title:", title)
        print("Author:", author)
        print("-" * 40)

        # ✅ Save to list
        if title and author:
            data.append([title, author])

    except Exception as e:
        print("Error:", e)
        continue

# ✅ Save to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author"])  # header
    writer.writerows(data)

print("✅ Data saved to books.csv")

driver.quit()