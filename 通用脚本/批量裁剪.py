import os
from PIL import Image

# 前期准备，找到纸张坐标，有多少个像素容差，左：最多2.5，上：最多3cm，右边最多2cm，下边最多1.8cm
# 左上角容差
dx1 = 0
dy1 = 0
# 右下角容差
dx2 = 500
dy2 = 0

# 以下四个角点由人工识别得出，OpenCV不会用
base_x1 = 87  # 左上角，切割到纸张边缘固定参数
base_y1 = 607 # 右上角，切割到纸张边缘固定参数
base_x2 = 2680 # 同理
base_y2 = 2940

# 最后一刀(左，上，右，下)
def main():
    files = os.listdir()
    for file in files:
        if not os.path.isdir(file):
            if not file.endswith(".py"):
                if not file.endswith(".html"):
                    print(file)
                    image = Image.open(file)
                    cropped = image.crop((base_x1+dx1, base_y1+dy1, base_x2+dx2, base_y2+dy2))
                    cropped.save(file)
pass

main()