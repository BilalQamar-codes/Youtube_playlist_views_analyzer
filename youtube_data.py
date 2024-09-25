import requests as re
from bs4 import BeautifulSoup 


html_text = re.get('https://www.youtube.com/playlist?list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s').text
# soup = BeautifulSoup(html_text, 'lxml')
print(html_text)
# vedios_list = soup.find('div', class_= ' style-scope ytd-playlist-video-list-renderer style-scope ytd-playlist-video-list-renderer')

# print(vedios_list)