import os
import random
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup


import socket
socket.setdefaulttimeout(30)

ARTS_LIST = 'query_results.csv' # query results from google bigquery
DIR = 'data'

ID, CULTURE, URL = range(0, 3)

with open(ARTS_LIST) as f:
    arts_to_download = f.readlines()
    arts_to_download = [line.strip() for line in arts_to_download]


data = []
for line in arts_to_download:
    object_id, *culture, url = line.split(',')
    culture = ' '.join(culture)
    data.append((object_id, culture, url))


def get_download_link(art_page):
    '''
    find the download links of the art given the museum page
    
    :type str: art_page
    :rtype list of str
    '''
    
    ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.8.0 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.8.0 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (LHTML, like Gecko) Chrome/17"
    ]
    
    user_agent = random.choice(ua_list)
    request = urllib.request.Request(art_page)
    request.add_header("User-Agent", user_agent)

    try:
        response = urllib.request.urlopen(request, timeout=5)
        encoding = response.headers.get_content_charset()
    
        if not encoding:
            return []
    
        html = response.read().decode(encoding)
        soup = BeautifulSoup(html)
        finds_list = soup.find_all("a", class_="gtm__download__image")
    
        return [a['href'] for a in finds_list]
    
    except:
        return []


for index, row in enumerate(data[88:]):
    print("processing image {} ...".format(index))
    i = 0
    
    for img_link in get_download_link(row[URL]):
        print('image linked retrived, ', img_link)
        
        save_folder = os.path.join(DIR, row[CULTURE])
        file_name = os.path.join(save_folder, "{}-{}.jpg".format(row[ID], i))
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        print(file_name)
    
        try:
            urllib.request.urlretrieve(img_link, file_name)
            print('file saved.')
            print('-' * 20)
            i += 1
        
        except:
            pass




