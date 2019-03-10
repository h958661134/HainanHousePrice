#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: test1.py
@time: 2018/5/25 18:00
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

def get_contents(ulist,rurl):
    soup=BeautifulSoup(rurl,'lxml')
    trs=soup.find('tbody').find_all('tr')
    for tr in trs:
        ui=[]
        tk=tr.find_all('span')
        for k in tk:
            ui.append(k.text)
        ulist.append(ui)

def get_as(ulist1,ulist2,ulist3,rurl,uuu):
    soup=BeautifulSoup(rurl,'lxml')
    trs=soup.find('div', class_ = 'jdsj_cl').find_all('a')
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
    uname1=[]
    uname2=[]
    # url='http://tjj.sanya.gov.cn/tjsj/ydsj/ydsj/czsz/201802/t20180209_2549942.html'
    rs=check_link('http://tjj.sanya.gov.cn/tjsj/ydsj/2016nydsj/')
    get_as(url,uname1,uname2,rs,'http://tjj.sanya.gov.cn/tjsj/ydsj/2016nydsj/')
    i=0
    count=0
    for (x,y) in zip(url,uname2):
        urli = []
        rs1=check_link(x)
        get_contents(urli, rs1)
        save_c(urli,uname1[i]+y)
        count+=1
        if count==11:
            count=0
            i+=1
