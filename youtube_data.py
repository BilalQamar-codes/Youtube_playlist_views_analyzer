from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.youtube.com/playlist?list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s'
browser= webdriver.Chrome()
browser.get(url)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'html.parser')
# print(html_text)
vedios_list = soup.find('div', class_= 'style-scope ytd-playlist-video-renderer')
meta_data = vedios_list.find('h3', class_= 'style-scope ytd-playlist-video-renderer')

print(meta_data['aria-label'])