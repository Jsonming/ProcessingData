#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 15:55
# @Author  : yangmingming
# @Site    : 
# @File    : APY200830001.py
# @Software: PyCharm
import os
import shutil


class BehaviorForeignDrivers(object):
    def __init__(self):
        pass

    def drop_camera(self):
        """
        删除一个镜头的数据
        :return:
        """
        work_dir = r"\\10.10.30.14\数据提取\JueNi\4套图像部分自有数据集\251人中控台上方和后视镜中央的视频\data"
        for time_slot in os.listdir(work_dir):
            time_slot_path = os.path.join(work_dir, time_slot)
            for person in os.listdir(time_slot_path):
                person_path = os.path.join(time_slot_path, person)
                camera_path = os.path.join(person_path, "01")
                shutil.rmtree(camera_path)


if __name__ == '__main__':
    bfd = BehaviorForeignDrivers()
    bfd.drop_camera()
