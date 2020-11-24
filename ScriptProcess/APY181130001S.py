#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 15:43
# @Author  : yangmingming
# @Site    : 
# @File    : APY181130001S.py
# @Software: PyCharm
import os


class EighteenKindGestures(object):
    def __init__(self):
        pass

    def extract_img(self, work_dir, dest_dir):
        """
        提取图片， 生成文件路径文件
        :return:
        """
        for gesture in os.listdir(work_dir):
            gesture_path = os.path.join(work_dir, gesture)
            for file in os.listdir(gesture_path):
                if file.endswith(".jpg"):
                    print(file)

    def run(self):
        work_dir = r"\\10.10.30.14\d\图像\APY181130001_314178张18种手势识别数据\完整数据包_processed\data"
        dest_dir = r"\\10.10.30.14\数据提取\张嘉静\APY181130001_314178张18种手势识别数据"
        self.extract_img(work_dir, dest_dir)


if __name__ == '__main__':
    ekg = EighteenKindGestures()
    ekg.run()
