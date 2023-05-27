#批量旋转图片
import os
import shutil
import os.path
from PIL import Image
# 筛选
def xs(p_txt_dir):
    files = os.listdir()
    # print(files)
    for file in files:
        if os.path.isfile(file):
            print(file)
            # 排除脚本自己
            if not file.endswith(".py"):
                each_img = Image.open(file)
                if p_txt_dir == "1":
                    if each_img.height > each_img.width:
                        shutil.move(file,"正常朝向")
                if p_txt_dir == "2":
                    if each_img.width > each_img.height:
                        shutil.move(file,"正常朝向")
                if p_txt_dir == "3":
                    break
# 左右翻转
def flip_h(p_txt_dir):
    files = os.listdir()
    # print(files)
    for file in files:
        if os.path.isfile(file):
            print(file)
            # 排除脚本自己
            if not file.endswith(".py"):
                each_img = Image.open(file)
                if p_txt_dir == "1":
                    each_img = each_img.transpose(Image.ROTATE_270)
                    each_img.save(file)
                if p_txt_dir == "2":
                    each_img = each_img.transpose(Image.ROTATE_90)
                    each_img.save(file)
                if p_txt_dir == "3":
                    break
    pass

# 筛选 左右转正 上下颠倒转正
def main():
    dirs = ["正常朝向"]
    print("欢迎使用")
    print("1: 纵向, px:height>width")
    print("2: 横向, px:width>height")
    print("3: 跳过")
    zc_txt_dir = input("筛选步骤：请选择正常文字朝向图片\n")
    if not os.path.isdir("正常朝向"):
        os.mkdir("正常朝向")
    xs(zc_txt_dir)

    print("1: 朝左")
    print("2: 朝右")
    print("3: 跳过")
    flip_txt_dir = input("请选择大部分错误方向图片的文字朝向")
    flip_h(flip_txt_dir)


main()
# 测试通过
# img = Image.open("test.jpg")

# 核心技术
# 文字左朝向对应270度
# 文字右边朝对应90度
# 文字下朝向对应180度 #一般手机拍照 不会出现这种情况，暂时不写代码
# img = img.transpose(Image.ROTATE_180)
# img.save("test_trans.jpg")
# book_paiban_dirs = ['v',"h"]
#A4 = [29.7,21]
# img_text_dirs = ["left","up","right","bottom"]

# 如果宽度>高度，为左右文字朝向
# 如果宽度<高度，为上下朝向
#-1 输入文字宽度高度朝向，先提取正常文件，转存一个文件夹，剩下错误图像，给机器处理
# 第0步：人工神经网络识别，大部分错误的图像的文字朝向，如果大部分朝左，输入左，机器内部操作符号为向右90度。
#     如果大部分错误的图像朝右，输入右，机器内部   向左90度
#     如果大部分错误的图像向下，输入文字朝向为下，往某个方向转动180度

# 第一步：如果遇到左右朝向，就旋转图片，直到图片变成上下任意朝向