from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
# import csv
import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="LK@2005",
    database="book_db"
)

cursor = conn.cursor()

# Connect to already opened Chrome
options = Options()
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)

time.sleep(5)

print("\n--- BOOKS DATA ---")

# ✅ Updated selector (more reliable)
rows = driver.find_elements(By.XPATH, "//table//tr[td]")

print("Books found:", len(rows))

data = []

for row in rows:
    try:
        title = row.find_element(By.XPATH, ".//td[contains(@class,'title')]//a").get_attribute("textContent").strip()
        author = row.find_element(By.XPATH, ".//td[contains(@class,'author')]//a").get_attribute("textContent").strip()

        print("DEBUG :", title, "|", author)

        if title and author:
            sql = "INSERT INTO books (title,author) VALUES (%s, %s)"
            values = (title,author)

            cursor.execute(sql,values)
            conn.commit()

            print("Inserted:" , title)
            print("-" *40)

    except Exception as e :
        print("Error:", e)
        continue

print("Data Inserted succesfully into mysql")

driver.quit()
cursor.close()
conn.close()

