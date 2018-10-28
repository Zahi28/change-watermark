# change-watermark

主要涉及图片格式转换以及添加数字水印和数字水印解码

## 图片格式转换：

可以转换格式： gif bmp jpg png tga tif

使用方法（示例）：

>import pic_func #导入包

>pic_func.change_format("./src/demo1.jpg", "./change", "tga")

其中第一个参数为原始图片路径

第二个参数为输出图片文件夹

第三个参数为所要的格式

## 添加数字水印

所要添加的水印为src文件夹的watermark.png

使用方法（示例）：

>import pic_func #导入包

>pic_func.add_watermark("./src/demo1.jpg", "./src/watermark.png", "./wm_out")

其中第一个参数为原始图片路径

第二个参数为水印的路径

第三个参数为输出的文件夹

输出的文件命名格式为wm_原始图片名，格式为.png

## 解码数字水印

使用方法（示例）：

>import pic_func #导入包

>pic_func.decode_watermark("./wm_out/wm_demo1.png", "./src/demo1.jpg", "./dwm_out")

其中第一个参数为添加了水印的图片

第二个参数为原始图片的路径

第三个参数为输出的文件夹

输出的文件命名格式为dwm_原始图片名，格式为.png
