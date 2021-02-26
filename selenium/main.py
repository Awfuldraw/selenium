from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# .\main.py

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://google.com")

# 1.1
