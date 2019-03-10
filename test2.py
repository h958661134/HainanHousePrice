#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: test2.py
@time: 2018/5/25 23:23
'''

import urllib
import re
from bs4 import BeautifulSoup

url='http://tjj.sanya.gov.cn/tjsj/ydsj/ydsj/czsz/201802/t20180209_2549942.html'
page = urllib.request.urlopen(url)
html=page.read().decode(encoding='utf-8',errors='strict')

# print(html)


def earse(strline, ch):
    right = strline.find(ch)
    while right != -1:
        strline = strline.replace(ch, '')
        right = strline.find(ch)
    return strline

def getTable(html):
    reg=''
    tablere=re.compile(reg)
    tablelist=re.findall(tablere,html)


soup = BeautifulSoup(html)
min_salary = []
min_salary_rows = []
# print(soup('title')[0].string)

tab = soup.findAll('table')

trs = tab[len(tab) - 1].findAll('tr')

for trIter in trs:
    tds = trIter.findAll('span')
    for tdIter in tds:
        p = tdIter('p')
        for i in range(len(p)):
            if p[i].string:
                min_salary_rows.append((earse(p[i].string, ' ').strip()))
                print(earse(p[i].string, ' ').strip()),
            else:
                pass
        min_salary.append(min_salary_rows)
print(min_salary)