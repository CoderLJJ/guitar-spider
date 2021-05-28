import multiprocessing
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd
'''
http://www.gtpso.com/index.php?m=home&c=index&a=hottabs&p=
http://www.gtpso.com/index.php?m=home&c=index&a=newtabs&p=
'''


def get_url():
    # start =time.time()
    d = []
    for i in range(
            101,
            121):  # 爬取 1 到 50 页的网址 尽量不要一次性爬太多  for i in range(51, 101) 51 到100页
        url = 'http://www.gtpso.com/index.php?m=home&c=index&a=hottabs&p=' + \
            str(i)
        html = requests.get(
            url,
            headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'},
            timeout=30)  # 获取网页
        soup = BeautifulSoup(
            html.content,
            "lxml",
            from_encoding='utf-8')  # 获取lxml树

        qupu = soup.select(
            '#in > div.col-xs-12.col-md-12.col-sm-12 > div > table > tr > td > a')
        # tf = pd.read_html(qupu.prettify(), header=0)  #
        # prettify():页面美化（整理成有格式的）
        for q in qupu:
            l = []
            if q.string == '在线预览':
                u = 'http://www.gtpso.com/' + q.get('href')
                # print(ur)
                l.append(u)
                d.append(l)
        df = pd.DataFrame(d, columns=['urls'])
    df.to_excel('guitar_hottabs(101-120).xlsx', encoding='utf-8')


    # end = time.time()
    # print("总共耗时：%f" % (end - start))
get_url()
'''
:execel文件的名称可以自己更改
'''
# get_url()
# if __name__ == '__main__':
#     start =time.time()
#     multiprocessing.Process(target=get_url).start()
#     end = time.time()
#     print("总共耗时：%f" % (end - start))
