#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 16:47
# @Author  : yangmingming
# @Site    : 
# @File    : APY191231001S.py
# @Software: PyCharm
import os
import random
import shutil
from collections import defaultdict


def run():
    """
    提取百万车牌的脚本，
    :return:
    """
    dest_dir = r"\\10.10.30.14\数据提取\刘达\1,036,580张车牌标注及转写数据样例\data"
    work_dir = r"\\10.10.8.123\自采全国车牌数据\客户数据\format_all\data_0818_liuxd_result_result_shen_20200831\最终数据（无措）"
    total_data = defaultdict(list)
    for province in os.listdir(work_dir)[:10]:
        province_path = os.path.join(work_dir, province)
        province_yellow_path = os.path.join(province_path, "yellow_card")
        province_yellow_double_path = os.path.join(province_path, "yellow_double_card")
        province_green_path = os.path.join(province_path, "green_card")
        province_black_card = os.path.join(province_path, "black_card")
        province_white_card = os.path.join(province_path, "green_card")

        for color_path in [province_yellow_path, province_yellow_double_path, province_green_path, province_black_card,
                           province_white_card]:
            color_type = color_path.split("\\")[-1]
            if os.path.exists(color_path):
                files = [os.path.join(color_path, file) for file in os.listdir(color_path) if file.endswith(".jpg")]
                total_data[color_type].extend(files)
    for color, files in total_data.items():
        need_copy = random.sample(files, 50)
        dest_folder = os.path.join(dest_dir, color)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        for img in need_copy:
            json_file = img.replace(".jpg", ".json")
            shutil.copy(img, dest_folder)
            shutil.copy(json_file, dest_folder)


if __name__ == '__main__':
    run()
