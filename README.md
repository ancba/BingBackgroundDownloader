# BingBackgroundDownloader

## 简要说明
一个Bing主页背景的下载器(爬虫)
爬取当天bing主页的背景

## 特点
* 体积小
* 占用少
* 运行速度快

## 系统要求
* 需要具有完整的Python环境，版本必须>=3.0，最好为Python 3.8

* 一个良好的网络链接，且能够流畅访问bing.com

## 启动
```
git clone https://github.com/ancba/BingBackgroundDownloader.git
cd BingBackgroundDownloader
python main.py
```
或

```
python3 main.py
```

## 注意
* 有时bing国际版和国内版的背景并不相同，所爬取到的图片由使用时的网络环境所决定
* 只能爬取当天的背景，无法爬取过去的图片以及提前爬取以后的图片
