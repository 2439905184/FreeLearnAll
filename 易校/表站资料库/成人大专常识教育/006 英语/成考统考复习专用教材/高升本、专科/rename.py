# 无顺序，用于录入数据库
# todo 排除文件功能
# todo 利用机械学习模型，实现自动识别图像的书页，并按照图片的书页进行命名
exclude = [".py",".html"]
import os
files = os.listdir()
index = 0
for file in files:
    if not os.path.isdir(file):
        if not file.endswith(".py"):
            print(file)
            os.rename(file,str(index)+".jpg")
            index +=1