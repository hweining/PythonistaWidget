# -*- coding: utf-8 -*-
__author__ = 'hweining'

import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
url = "http://www.weather.com.cn/weather1d/101280101.shtml#search"

web_data = requests.get(url, headers=headers)

# 设置web_data.text会采用web_data.encoding指定的编码，一般情况下不需要设置，requests会自动推断
# 鉴于网页大部分都是采取utf-8编码的，所以设置一下，省去一些麻烦
web_data.encoding = 'utf-8'
# 得到网页源代码
content = web_data.text

# 使用lxml解析器来创建Soup对象
soup = BeautifulSoup(content, 'lxml')

# 为什么要创建一个Soup对象，还记得浏览器中的检查元素功能嘛
# Soup对象可以方便和浏览器中检查元素看到的内容建立联系，下面会有动画演示
# 使用css selector语法，获取白天和夜间温度，下面有动画演示
tag_list = soup.select('p.tem span')

# tag_list[0]是一个bs4.element.Tag对象
# tag_list[0].text获得这个标签里的文本
day_temp = tag_list[0].text
night_temp = tag_list[1].text

print('白天温度为{0}℃\n晚上温度为{1}℃'.format(day_temp, night_temp))
