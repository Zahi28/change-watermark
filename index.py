#  _*_ coding:utf-8 _*_
"""
@author: Zahi
@contact: xu_zixu@outlook.com
@file: index.py
@time: 2018/10/25 17:01
"""

import pic_func

pic_func.change_format("./src/demo1.jpg", "./change", "tga")
pic_func.add_watermark("./src/demo1.jpg", "./src/watermark.png", "./wm_out")
pic_func.decode_watermark("./wm_out/wm_demo1.png", "./src/demo1.jpg", "./dwm_out")
