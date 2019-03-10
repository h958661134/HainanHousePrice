#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: test3.py
@time: 2018/5/26 11:01
'''

from bs4 import BeautifulSoup
import requests
import xlrd
import xlwt
import bs4

def check_link(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('无法连接服务器')

def get_as(ulist1,ulist2,ulist3,rurl):
    soup=BeautifulSoup(rurl,'lxml')
    trs=soup.find('div', class_ = 'jdsj_cl').find_all('a')
    trs1 = soup.find('div', class_='jdsj_cl').find_all('td',class_='td_t')
    ui = []
    for tr in trs:
        print('http://tjj.sanya.gov.cn/tjsj/ydsj/ydsj/'+tr['href'])
        ulist1.append('http://tjj.sanya.gov.cn/tjsj/ydsj/ydsj/'+tr['href'])
        ulist3.append(tr.text)
    for tr in trs1:
        print(tr.text)
        ulist2.append(tr.text)

if __name__ == "__main__":
    ulist=[]
    ulist1=[]
    ulist2=[]
    url = 'http://tjj.sanya.gov.cn/tjsj/ydsj/ydsj/'
    rs=check_link(url)
    get_as(ulist,ulist1,ulist2,rs)
