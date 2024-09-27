from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt

url = 'https://www.youtube.com/playlist?list=PLn55kp0ywMLyOHdWGYxjwwyxufUFQ2Uds'
browser= webdriver.Chrome()
browser.get(url)
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'html.parser')
# print(html_text)
views = []
lablels = []
vedio = soup.find_all('ytd-playlist-video-renderer', class_ = 'style-scope ytd-playlist-video-list-renderer')
if len(vedio) > 1:
    browser.close()
    i = 1
    for v in vedio:
        info = v.find('div', class_= 'style-scope ytd-playlist-video-renderer')
        meta_data = info.find('h3', class_= 'style-scope ytd-playlist-video-renderer')
        l1 = list(meta_data['aria-label'].split(' views'))
        l2 = list(l1[0].split())
        views.append(int(l2[len(l2)-1].replace(',','')))
        lablels.append('vedio ' + str(i))
        i += 1
print(views)

plt.plot(views)
plt.show()
# for vedio in vedios_list:
#     meta_data = vedio.find('h3', class_= 'style-scope ytd-playlist-video-renderer')
#     l = list(meta_data['aria-label'].split())
#     views.append(int(l[13].replace(',','')))
# print(views)