import requests
from bs4 import BeautifulSoup

# Step 1: URL
url = "https://books.toscrape.com/"

# Step 2: Get page
response = requests.get(url)

print("Status Code:", response.status_code)

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find all book titles
books = soup.find_all("h3")

print("\n--- BOOK TITLES ---")

for i, book in enumerate(books, start=1):
    title = book.find("a")["title"]
    print(f"{i}. {title}")

books = soup.find_all("article", class_="product_pod")

print("\n--- BOOK DATA ---")

for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text

    print("Title:", title)
    print("Price:", price)
    print("-" * 30)




import csv

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])

    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text

        writer.writerow([title, price])

print("✅ Data saved to books.csv")

import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

for page in range(1, 6):   # scrape first 5 pages
    url = base_url.format(page)
    print(f"Scraping Page {page}...")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text

        all_books.append([title, price])

# Save to CSV
with open("all_books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    writer.writerows(all_books)

print("✅ Scraped multiple pages successfully!")

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.amazon.in/s?k=phones"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
#     "Accept-Language": "en-US,en;q=0.9"
# }

# response = requests.get(url, headers=headers)
# print("Status:", response.status_code)
# soup = BeautifulSoup(response.text, "html.parser")

# print(soup.title.text)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import csv

# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in/s?k=phones")

# time.sleep(10)

# print("\n--- AMAZON PRODUCTS ---")

# # ✅ Get each product block
# items = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

# data = []

# for item in items[:10]:   # first 10 products
#     try:
#         title = item.find_element(By.XPATH, ".//h2//span").text
#     except:
#         title = "N/A"

#     try:
#         price = item.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
#     except:
#         price = "N/A"

#     print("Title:", title)
#     print("Price:", price)
#     print("-" * 40)

#     data.append([title, price])

# # ✅ Save to CSV
# with open("amazon_products.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Title", "Price"])
#     writer.writerows(data)

# print("✅ Clean data saved!")

# input("Press Enter to close browser...")
# driver.quit()

