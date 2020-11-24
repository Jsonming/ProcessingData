#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 11:13
# @Author  : yangmingming
# @Site    : 
# @File    : base.py
# @Software: PyCharm
import os
import zipfile
import shutil
from multiprocessing import Pool


class Base(object):
    def __init__(self):
        pass

    @staticmethod
    def find_file_by_suffix(work_dir, suffix):
        for root, dirs, files in os.walk(work_dir):
            for file in files:
                if file.endswith(suffix):
                    yield os.path.join(root, file)

    def async_executive(self, func, args):
        """
        多进程执行函数
        :param func: 函数
        :param args: 参数
        :return:
        """
        pool = Pool(processes=4)
        pool.map(func, args)
        pool.close()
        pool.join()
        return True

    @staticmethod
    def make_zip(src_dir, dest_dir, package_name):
        """
        将数据打压缩包 每80个G打一个压缩包
        :param src_dir:
        :param dest_dir:
        :param package_name:
        :return:
        """
        package_size = 70 * 1024 * 1024 * 1024  # 打包大小
        files_group, temp_group, temp_count = [], [], 0
        for root, dirs, files, in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                temp_count += file_size
                temp_group.append(file_path)
                if temp_count > package_size:
                    files_group.append(temp_group)
                    temp_group, temp_count = [], 0
        files_group.append(temp_group)

        for i, pack_files in enumerate(files_group):
            package_path = os.path.join(dest_dir, "{}_{}.zip".format(package_name, i))
            with zipfile.ZipFile(package_path, 'w') as zipf:
                pre_len = len(os.path.dirname(src_dir))
                for filename in pack_files:
                    arc_name = filename[pre_len:].strip(os.path.sep)  # 相对路径
                    zipf.write(filename, arc_name)

    @staticmethod
    def gen_path_file(files_dir):
        files_dir_txt = files_dir + ".txt"
        with open(files_dir_txt, 'a', encoding='utf8')as f:
            for root, dirs, files in os.walk(files_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    f.write(file_path + "\n")


class ImgBase(Base):
    @staticmethod
    def img_copy(info):
        """
        拷贝图片文件
        :param info:
        :return:
        """
        src_img, dest_img = info
        shutil.copyfile(src_img, dest_img)


class VideoBase(Base):
    def __init__(self):
        pass
