import time
import urllib.request as request

def get_link ():
	bing = request.urlopen('https://www.bing.com')
	html = str(bing.read())
	postion1 = html.find('href="/')
	postion2 = html.find('" as="image"') #获取壁纸链接
	link = 'https://www.bing.com' + html[postion1 + 6:postion2]

def download (link):
	bg = request.urlopen(link)
	image = bg.read()
	f = open('Bingimage' + str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2]) + '.jpg','wb')
	f.write(image)

def start ():
    try:
        get_link()
        download(link)
    except OSError as error:
            print(error)
            get_link()
