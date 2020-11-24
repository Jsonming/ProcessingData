#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 17:34
# @Author  : yangmingming
# @Site    : 
# @File    : APY161201424.py
# @Software: PyCharm
from ProjectsProcess.base import Base


class AsianCelebrityFace(Base):
    def __init__(self):
        pass

    def count_img(self):
        i = 0
        work_dir = r"\\10.10.30.14\e\图像数据\图像数据2016\APY161201424_10,470人亚洲名人脸图像数据\完整数据包_processed - 新\data\category01"
        for file in self.find_file_by_suffix(work_dir, "g"):
            print(file)
            i += 1
            if i > 320000:
                print(file)
                break


if __name__ == '__main__':
    acf = AsianCelebrityFace()
    acf.count_img()
