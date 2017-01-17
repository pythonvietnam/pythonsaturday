import urllib
import urllib2
import os

def get_link(url, key1, key2):
    img_links   = []
    cursor      = urllib2.urlopen(url)
    webContent  =  cursor.read()

    while 1:
        if webContent.find(key1) < 0:
            break
        webContent = webContent[webContent.find(key1) + len(key1):]
        position_end = webContent.find(key2)
        if position_end > -1 and position_end < webContent.find(key1):
            img_links.append(webContent[:position_end])

    return list(set(img_links))

def store_image(img_links, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for index, src in enumerate(img_links):
        img_name = src.split('/')[-1]
        print img_name
        urllib.urlretrieve(src, '{}/{}'.format(folder_name, img_name))

url             = 'http://congtruyen24h.com/truyentranh/Fairy-Tail/Chap-516/'
root_folder     = 'FairyTail'
key1            = """<div class='text-center' style='margin-bottom:5px'><img src='"""
key2            = """' class='img-responsive'"""

if not os.path.exists(root_folder):
    os.makedirs(root_folder)

key3    = "<option value='"
key4    = "/'>Chap"

list_url = get_link(url, key3, key4)

for url in list_url:
    print url
    img_links = get_link(url + '/', key1, key2)
    folder_name = url.split('/')[-1]
    store_image(img_links, root_folder + '/' + folder_name)