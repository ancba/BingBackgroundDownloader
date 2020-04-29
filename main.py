import time
import urllib.request as request

def get_link ():
	bing = request.urlopen('https://www.bing.com')
	html = str(bing.read())
	postion1 = html.find('href="/')
	postion2 = html.find('" as="image"')
	link = 'https://www.bing.com' + html[postion1 + 6:postion2]
	print ('已获取到背景链接地址' + link)
	download(link)

def download (link):
	print('开始下载')
	bg = request.urlopen(link)
	write = bg.read()
	f = open('Bingimage' + str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2]) + '.jpg','wb')
	f.write(write)
	print('下载已完毕')

if __name__ == '__main__':
	get_link()
