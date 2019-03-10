#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: test1.py
@time: 2018/5/25 18:00
'''

# http://bj.ganji.com/fang1/ditie/o2l6/

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

def get_contents(ulist,rurl):
    soup = BeautifulSoup(rurl,'html.parser')
    try:
        trs=soup.find('div', class_ = 'f-list').find_all('span')
        for tr in trs:
            ulist.append(tr.text)
    except:
        pass

def get_as(ulist1,ulist2,ulist3,rurl,uuu):
    soup=BeautifulSoup(rurl,'lxml')
    trs=soup.find('div', class_ = 'jdsj_cl').find_all('span')
    trs1 = soup.find('div', class_='jdsj_cl').find_all('td',class_='td_t')
    ui = []
    for tr in trs:
        # print('http://tjj.sanya.gov.cn/tjsj/ydsj/ydsj/'+tr['href'])
        ulist1.append(uuu+tr['href'])
        ulist3.append(tr.text)
    for tr in trs1:
        # print(tr.text)
        ulist2.append(tr.text)

def save_c(urlist,name):
    wbk = xlwt.Workbook(encoding='ascii')
    sheet = wbk.add_sheet("wordCount")
    i=0
    w=0
    for k in urlist:
        w=0
        for kk in k:
            # if kk.find('#') != -1:
            #     continue
            sheet.write(i,w,kk)
            w+=1
        i+=1
    wbk.save(name+'.xls')



if __name__ == "__main__":
    url=[]
    with open("open.txt", "w") as f:
        for i in range(2, 1000):
            urla = "http://bj.ganji.com/fang1/ditie/o" + str(i) + "l6/"
        # url='http://tjj.sanya.gov.cn/tjsj/ydsj/ydsj/czsz/201802/t20180209_2549942.html'
            rs=check_link(urla)
            get_contents(url,rs)
            for x in url:
                f.write(x+" ")
