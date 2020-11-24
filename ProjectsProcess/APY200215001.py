#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 15:57
# @Author  : yangmingming
# @Site    : 
# @File    : APY200215001.py
# @Software: PyCharm
import os
import shutil
from ProjectsProcess.base import Base


def img_copy(info):
    """
    拷贝图片文件
    :param info:
    :return:
    """
    src_img, dest_img = info
    shutil.copyfile(src_img, dest_img)


class OccludedFaceMultipleGestures(Base):
    """
    1,058人面部遮挡多姿态人脸识别数据
    """

    def __init__(self):
        pass

    def extract_img(self):
        imgs_name = ["C1", "glasses_near", "glasses_left", "glasses_right", "nomask_near", 'nomask_right',
                     'nomask_left']
        work_dir = r"\\10.10.30.14\d\图像\APY200215001_1,058人面部遮挡多姿态人脸识别数据\完整数据包\data"
        dest_dir = r"\\10.10.30.14\数据提取\王程晨\APY200215001_1,058人面部遮挡多姿态人脸识别数据\data"

        src_imgs = []
        for person in os.listdir(work_dir):
            person_path = os.path.join(work_dir, person)
            for img_name in imgs_name:
                img_path = os.path.join(person_path, "{}.jpg".format(img_name))
                src_imgs.append(img_path)

        copy_info = []
        for src_img in src_imgs:
            dest_img = src_img.replace(work_dir, dest_dir)
            dest_folder = os.path.split(dest_img)[0]
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            copy_info.append((src_img, dest_img))

        self.async_executive(img_copy, copy_info)

        return dest_dir

    def run(self):
        dest_dir = r"\\10.10.30.14\数据提取\王程晨\APY200215001_1,058人面部遮挡多姿态人脸识别数据"
        # self.gen_path_file(dest_dir)
        self.make_zip(dest_dir)


if __name__ == '__main__':
    ofmg = OccludedFaceMultipleGestures()
    ofmg.run()
