import multiprocessing
import os
import time

from PIL import Image

if not os.path.exists('i'):
    os.mkdir('i')  # 拼接后的图片存放路径
path = 'img'  # 分类后图片的存放目录 需更改
    # if not os.path.exists(path):
    #     os.mkdir(path)

def pinjie():

    ll = []
    for f in os.listdir(path):
        # print(f) #起风了
        aa = os.path.join(path, f).replace('\\', '/')
        # print(aa) # video/起风了
        # print(b)
        #     # print(b)
        #     # print(aa)
        ll.append(aa)
        new_l = list(set(ll))
        new_l.sort(key=ll.index)
    # print(new_l)
    for e in range(len(new_l)):
        # print(e)
        im_list = []
        #     # path = "de"
        for fn in os.listdir(new_l[e]):
            # print(fn)
            # print(fn[:-5])  # 截取图片名称
            # h = os.path.split(fn)[-1][:-5]
            #         # if fn.endswith('.jpg'):
            #         # print(fn[:-5])  # 阿珍爱上了阿强
            im_list.append(Image.open(new_l[e] + os.sep + fn))
        # print(im_list)
        width = 0
        height = 0
        for img in im_list:
            # print(de)
            # 单幅图像尺寸
            w, h = img.size
            height += h
            # 取最大的宽度作为拼接图的宽度
            width = max(width, w)
        # 创建空白长图
        # print(im_list[0].mode)
        # if im_list[0].mode =="L":
        #     pass
        if im_list[0].mode != "RGB":
            im_list[0] = im_list[0].convert('RGB')
            print(im_list[0].mode)
        else:
            pass
        result = Image.new(im_list[0].mode, (width, height), 0xffffff)
        # print(result.mode)
        # 拼接图片
        height = 0
        for img in im_list:
            w, h = img.size
            # 图片水平居中
            result.paste(img, box=(round(width / 2 - w / 2), height))
            # print(result.mode)
            # result.paste(de, box=(0, i * height))
            height += h
        # 保存图片
        # result.save(f"de\\{b}.png")
        # if result.mode == "P":
        #     result.save(f"de\\{b}.png")
        # if result.mode == "RGB":
        #     result.save(f"de\\{b}.jpg")
        try:
            h = os.path.split(fn)[-1][:-5]
            if fn.endswith('.jpg'):
                result.save(f"i\\{h}.jpg")
            if fn.endswith('.png'):
                result.save(f"i\\{h}.png")
            if fn.endswith('.gif'):
                result.save(f"i\\{h}.gif")
            # if fn.endswith('.jpg'):
            #     result.save(f"de\\{h}.jpg")
            # if fn.endswith('.png'):
            #     result.save(f"de\\{h}.png")
            # if fn.endswith('.gif'):
            #     result.save(f"de\\{h}.gif")
        except BaseException:
            pass


if __name__ == '__main__':
    start = time.time()
    pinjie()
    # multiprocessing.Process(target=pinjie).start()
    end = time.time()
    print("总共耗时：%f" % (end - start))
