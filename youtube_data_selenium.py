import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests as re

# Initialize the WebDriver
browser = webdriver.Chrome()

try:
    browser.get('https://www.youtube.com/playlist?list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s')
    wait = WebDriverWait(browser, 100)

except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")