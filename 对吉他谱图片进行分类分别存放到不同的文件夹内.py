import multiprocessing
import re
import time

import pandas as pd
import numpy as np
import os
import shutil

'''
file_path 爬取的图片所在文件夹
target_path 存放分类图片的文件夹
'''


def classifation(file_path, target_path):
    # 获取所有图片名称
    c = []
    names = os.listdir(file_path)  # 路径
    for name in names:
        index = name.rfind('.')
        name = name[:index][0:-1]
        c.append(name)
        new_list = list(set(c))
        new_list.sort(key=c.index)
    # print(len(new_list)) # 去重后的文件名，有几个名字，就有几类
    ll = []
    for l in new_list:
        aa = os.path.join(target_path, l).replace('\\', '/')
        if not os.path.exists(aa):
            os.mkdir(aa)
        # print(aa)
        ll.append(aa)
        new_l = list(set(ll))
        new_l.sort(key=ll.index)
    # print(new_l) # 文件夹列表
    # print(len(new_l))
    pp = []
    for p in names:
        bb = os.path.join(file_path, p).replace('\\', '/')
        pp.append(bb)
        new_ll = list(set(pp))
        new_ll.sort(key=pp.index)
    # print(new_ll)  # 文件夹下的图片文件
    # print(len(new_ll))
    for i in new_ll:
        h = os.path.split(i)[-1][:-5]
        # print(i[30:-5])  # 文件夹名称
        try:
            for e in range(len(new_list)):
                # print(e)
                if h in new_list[e]:
                    # print(i[15:5])
                    shutil.move(i, new_l[e])
        except BaseException:
            print("没有这个图片")


if __name__ == '__main__':
    start = time.time()
    if not os.path.exists('img'):
        os.mkdir('img')
    file_path = r'../httpwww.gtpso.com/qupu' # 需更改
    target_path = r'../httpwww.gtpso.com/img' # 需更改
    # multiprocessing.Process(
    #     target=classifation, args=(
    #         file_path, target_path)).start()
    classifation(file_path, target_path)
    end = time.time()
    print("总共耗时：%f" % (end - start))


# classifation(r'../AI系统测试/qupu', r'../AI系统测试/img')
# r'../AI系统测试/qupu' 爬取的图片所在路径 qupu文件夹
# r'../AI系统测试/img' 分类的图片文件和文件夹存放的文件夹 img文件夹
