# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 09:55:43 2018

@author: zhaof
"""

from urllib.request import urlopen
url="http://www.baidu.com"
response=urlopen(url)
content=response.read()
content=content.decode('utf-8')
print(content)


import urllib.request
url="http://www.baidu.com"
request=urllib.request.Request(url)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(response.geturl())
print(response.info())

#requests请求库
import requests
res=requests.get("http://www.baidu.com")
print(res.text)
print(res.status_code)

#解析库BeautifulSoup

import requests
from bs4 import BeautifulSoup
headers={}
url="http://news.qq.com"
Soup=BeautifulSoup(requests.get(url).text,'lxml')
em=Soup.find_all('em',attrs={'class':'f14 l24'})
for i in em:
    title=i.a.get_text()
    link=i.a['href']
    print({'标题':title,'链接':link})
    
#解析库lxml
import requests
from lxml import etree
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
        }
url="http://news.qq.com"
html=requests.get(url)
con=etree.HTML(html.text)
title=con.xpath('//em[@class="f14 l24"]/a/text()')
link=con.xpath('//em[@class="f14 l24"]/a/@href')
for i in zip(title,link):
    print({"标题":i[0],"链接":i[1]})
    
    
#信息提取
#css选择器 标签之间通过空格来区分
# xpath 通过/来区分
    
import requests
from bs4 import BeautifulSoup
headers={}
url="http://news.qq.com"
Soup=BeautifulSoup(requests.get(url).text,'lxml')
em=Soup.select('em[class="f14 l24"]')
for i in em:    
    title=i.a.get_text()
    link=i.a['href']
    print({'标题':title,'链接':link})
    
    
    
# ===============数据清洗============
import pandas as pd
import numpy as np

#缺失值处理
dates=pd.date_range('20160101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df1=df.reindex(index=dates[0:4],columns=list(df.columns)+['E'])
df1.loc[dates[0]:dates[1],'E']=1
#删除包含缺失的行
df1.dropna(how='any')
#对确实值进行填充
df1.fillna(value=5)
#均值填充
df1.fillna(df['A'].mean())

#小文本和字符串处理
#python字符串处理函数
#正则表达式 https://www.jb51.net/tools/regexsc.htm
"""
去除空格
字符串分割
拼接
字符串替换
"""
char1='  what is the time is it now   '
char1.strip()

char2='what,a,nice,day,today'
char2.split(',')

char3=char2.split(',')
','.join(char3)

char2.replace(","," ")

"""
正则表达式
"""
import re
"""
compile函数：编译正则表达式
re.compile(pattern,flag=0)
"""
text1=" wlbrom is a slight good person, he is cool"
rr=re.compile(r'\w*oo\w*')
print(rr.findall(text1))

#match函数，从字符串首开始匹配
#re.match(pattern,string,flag=0)
print(re.match('com','com.loudwill.com').group())





    
    
    
    
