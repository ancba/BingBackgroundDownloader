import time
import urllib.request as request

def get_link ():
    bing = request.urlopen('https://www.bing.com')
    html = str(bing.read())
    postion1 = html.find('href="/')
    postion2 = html.find('" as="image"') #获取壁纸链接
    global link
    link = 'https://www.bing.com' + html[postion1 + 6:postion2]

def download (path):
    bg = request.urlopen(link)
    image = bg.read()
    #判断路径
    if path == 0 or path == '0':
        f = open('Bingimage' + str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2]) + '.jpg','wb')
        f.write(image)
        f.close()
    else:
        f = open(path + 'Bingimage' + str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2]) + '.jpg','wb')
        f.write(image)
        f.close()

def start (path=0):
    try:
        get_link()
        download(path)
    except OSError as error:
            print(error)
            exit()