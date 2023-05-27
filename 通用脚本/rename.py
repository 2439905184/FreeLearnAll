# 无顺序，用于录入数据库
import os
files = os.listdir()
index = 0
for file in files:
    if not os.path.isdir():
        if not file.endswith(".py"):
            print(file)
            os.rename(file,str(index)+".jpg")
            index +=1