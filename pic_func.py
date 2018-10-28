#  _*_ coding:utf-8 _*_
"""
@author: Zahi
@contact: xu_zixu@outlook.com
@file: pic_func.py
@time: 2018/10/23 12:39
"""

'''
可以转换格式： gif bmp jpg png tga tif
'''


def change_format(img_path, output_dir, f_to_t):
    from PIL import Image
    import os

    if f_to_t != "jpg" and f_to_t != "png" and f_to_t != "gif" \
            and f_to_t != "bmp" and f_to_t != "tif" and f_to_t != "tga":
        return False

    im = Image.open(img_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    (file_path, temp_filename) = os.path.split(img_path)
    (filename, extension) = os.path.splitext(temp_filename)
    out_path = output_dir + "/" + filename + "." + f_to_t
    im.save(out_path)
    return


'''
添加水印
'''


def add_watermark(pic, mark, output_dir):
    import cv2
    import numpy as np
    import random
    import os

    alpha = 5  # 水印添加时的一个权重系数
    img = cv2.imread(pic)
    img_f = np.fft.fft2(img)  # 对图像做傅里叶变换，在频域加入水印
    height, width, channel = np.shape(img)
    watermark = cv2.imread(mark)
    wm_height, wm_width = watermark.shape[0], watermark.shape[1]
    x = [i for i in range(height // 2)]
    y = [i for i in range(width // 2)]
    random.seed(height + width)  # seed为height+width的随机数
    random.shuffle(x)  # 对整数列表进行随机排列
    random.shuffle(y)
    tmp = np.zeros(img.shape)
    for i in range(height // 2):
        for j in range(width // 2):
            if x[i] < wm_height and y[j] < wm_width:
                tmp[i][j] = watermark[x[i]][y[j]]
                tmp[height - 1 - i][width - 1 - j] = tmp[i][j]
    res_f = img_f + alpha * tmp
    res = np.fft.ifft2(res_f)
    res = np.real(res)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    (file_path, temp_filename) = os.path.split(pic)
    (filename, extension) = os.path.splitext(temp_filename)
    out_path = output_dir + "/wm_" + filename + ".png"
    cv2.imwrite(out_path, res)
    return


'''
检测水印
'''


def decode_watermark(image_path, ori_path, output_dir):
    import cv2
    import numpy as np
    import random
    import os
    alpha = 5
    img = cv2.imread(image_path)
    ori = cv2.imread(ori_path)
    img_f = np.fft.fft2(img)
    ori_f = np.fft.fft2(ori)
    height, width = img.shape[0], img.shape[1]
    watermark = (img_f - ori_f) / alpha
    watermark = np.real(watermark)
    res = np.zeros(watermark.shape)
    random.seed(height + width)
    x = [i for i in range(height // 2)]
    y = [i for i in range(width // 2)]
    random.shuffle(x)
    random.shuffle(y)
    for i in range(height // 2):
        for j in range(width // 2):
            res[x[i]][y[j]] = watermark[i][j]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    (file_path, temp_filename) = os.path.split(ori_path)
    (filename, extension) = os.path.splitext(temp_filename)
    out_path = output_dir + "/dwm_" + filename + ".png"
    cv2.imwrite(out_path, res)
    return
