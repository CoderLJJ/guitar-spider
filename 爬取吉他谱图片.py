import multiprocessing
import os
import time

import requests
import xlrd
from bs4 import BeautifulSoup
import pandas as pd
# url = 'http://www.gtpso.com/index.php/home/index/newtabs'
# def get_url(url):
# 自动创建qupu文件夹
if not os.path.exists('qupu'):
    os.mkdir('qupu')
d = []
data = xlrd.open_workbook('guitar_hottabs(101-120).xlsx')  # 读取爬取的网址
table = data.sheets()[0]
links = table.col_values(int(1))


def get_img():
    for url in links[1:]:
        html = requests.get(
            url,
            headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'},
            timeout=30)  # 获取网页
        time.sleep(1)
        soup = BeautifulSoup(
            html.content,
            "lxml",
            from_encoding='utf-8')  # 获取lxml树
        try:
            title = soup.find(
                'h3',
                attrs={
                    'class': 'mb-4'}).text.replace(
                ' ',
                '').replace(
                '（',
                '(').replace(
                    '）',
                    ')').replace(
                        '-',
                        '').replace(
                            '，',
                '')
            print(title)

        except BaseException:
            # title='找不到这个标题'
            print('没有找到这个标题')
        qp = soup.select('body > main > div > img')
        n = 1
        for q in qp:
            u = q.get('src')
            print(u)
            try:
                r = requests.get(u)
                if u[-4:] == '.png':
                    path = f"qupu/{title}{n}.png"
                elif u[-4:] == '.jpg':
                    path = f"qupu/{title}{n}.png"
                else:
                    path = f"qupu/{title}{n}.gif"
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print('下载完成!')
                n += 1
            except BaseException:
                print('error:')


if __name__ == '__main__':
    start = time.time()
    multiprocessing.Process(target=get_img).start()
    end = time.time()
    print("总共耗时：%f" % (end - start))
