# Gets data
# webscrappes images from file
# by Ashna Dureja
# 9/17/22

import requests
from bs4 import BeautifulSoup

def get_image_links(html, query):

    #parse html of website
    html_content = BeautifulSoup(html, 'html.parser')

    #scan for img tags
    img_tags = html_content.find_all('img', alt=query)

    #take source url for pics
    img_links = []
    for img in img_tags:
        img_links.append(img.attrs['src'])

    return img_links