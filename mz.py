__author__ = 'church-father'
from bs4 import BeautifulSoup
import requests
import time


def download_image(pic_class_list):
    for a in pic_class_list:
        href=a.get("href")

        req=requests.get(href)
        path="./image/"+href.split("/")[-1]
        with open(path,"wb") as f:
            f.write(req.content)


if __name__ == '__main__':
    url="http://jandan.net/ooxx"
    headers={
        'User-Agent': 'Mozilla/5.0 (X11, Linux i686; rv:44.0; Gecko/20100101 Firefox/44.0',
        'Accept':'text/html,application/xhtml+xml,application/xml,q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language':'en-US,en,q=0.5',
        'Connection':'keep-alive',
    }
    while True:
        html_content=requests.get(url,headers=headers).content
        soup=BeautifulSoup(html_content,"lxml")

        pic_class_list=soup.find_all("a",{"class":"view_img_link"})
        download_image(pic_class_list)

        url=soup.find("a",{"class":"previous-comment-page"}).get("href")
        time.sleep(2)
        print("downloading")
