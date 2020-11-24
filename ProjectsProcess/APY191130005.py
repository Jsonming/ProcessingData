#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 11:11
# @Author  : yangmingming
# @Site    : 
# @File    : APY191130005.py
# @Software: PyCharm
from ProjectsProcess.base import Base


class MultiracialIDAndPhoneContrast(Base):
    """
    提取数据 记录数据路径，打包数据
    """

    def __init__(self):
        pass

    def extract_img(self, work_dir, dest_dir):
        """
        提取图片数据
        :return:
        """

    def run(self):
        work_dir = r"\\10.10.30.14\d\图像\APY191130005_25,983人多人种人证比对数据\完整数据包\data"
        dest_dir = r"\\10.10.30.14\数据提取\王程晨\APY191130005_25,983人多人种人证比对数据"
        self.extract_img(work_dir, dest_dir)
        # self.gen_path_file(dest_dir)


if __name__ == '__main__':
    midp = MultiracialIDAndPhoneContrast()
    midp.run()
