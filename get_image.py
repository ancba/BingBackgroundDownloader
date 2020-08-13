import time
import urllib.request as request

def get_link ():
    bing = request.urlopen('https://www.bing.com')
    html = str(bing.read())
    postion1 = html.find('href="/')
    postion2 = html.find('" as="image"') #获取壁纸链接两端位置
    link = 'https://www.bing.com' + html[postion1 + 6:postion2] #合成链接
    print (link)
    return link

def download (path,link):
    bg = request.urlopen(link)
    image = bg.read()
    #判断路径
    if path == 0 or path == '0':
        f = open('Bingimage' + str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2]) + '.jpg','wb')
    else:
        f = open(path + 'Bingimage' + str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2]) + '.jpg','wb')
    f.write(image) #写入
    f.close()

def start (path=0):
    try:
        link = get_link()
        download(path,link)
    except OSError as error:
         print(error)
         exit()