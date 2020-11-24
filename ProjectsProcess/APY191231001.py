#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 11:12
# @Author  : yangmingming
# @Site    : 
# @File    : APY191231001.py
# @Software: PyCharm
import os
import shutil
from multiprocessing import Pool
from ProjectsProcess.base import Base


def copy_img(img_info):
    """
    拷贝图像文件
    :param img_info: 图片信息，包含要拷贝的图片目的路径
    :return:
    """
    src_img, dest_img = img_info
    shutil.copy(src_img, dest_img)
    src_json, dest_json = src_img.replace(".jpg", ".json"), dest_img.replace(".jpg", ".json")
    shutil.copy(src_json, dest_json)


class MillionLicensePlateDate(Base):
    """
    处理,提取, 统计百万车牌数据代码
    目录结构 省份/颜色/ 图片和json

    """

    def __init__(self):
        pass

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

    def view_count(self):
        work_dir = r"\\10.10.30.14\刘晓东\数据提取\吴驰\1,036,580张车牌标注及转写数据\第一批交付\各个省份"
        for folder in os.listdir(work_dir):
            if folder not in ["黑牌", "白牌"]:
                folder_path = os.path.join(work_dir, folder)
                imgs, sum_num = {}, 0
                for color_plate in os.listdir(folder_path):
                    color_plate_path = os.path.join(folder_path, color_plate)
                    color_plate_path = [file for file in os.listdir(color_plate_path)if file.endswith(".jpg")]
                    img_num = len(color_plate_path)
                    imgs[color_plate] = img_num
                    sum_num += img_num
                if sum_num < 6000:
                    print("\t".join([folder, ", ".join(["{}:{}".format(k, v) for k, v in imgs.items()]), str(sum_num)]))

    def extract(self):
        """
        提取数据
        1.每个省份6000 张   黄牌2000  蓝牌2000 绿牌 2000
        2.颜色不够从其他颜色抽取，
        3.省份不够从其他省份抽取
        :return:
        """

        def count_img(img_folder):
            """
            统计图片数据数据
            :param img_folder:
            :return:
            """
            if os.path.exists(img_folder):
                # imgs = [os.path.join(img_folder, file) for file in os.listdir(img_folder) if file.endswith(".jpg") and file not in file_set]
                imgs = [os.path.join(img_folder, file) for file in os.listdir(img_folder) if file.endswith(".jpg")]
                if imgs:
                    dest_foler = os.path.split(imgs[0].replace(work_dir, dest_dir))[0]
                    if not os.path.exists(dest_foler):
                        os.makedirs(dest_foler)
            else:
                imgs = []
            return imgs

        # file_set = set()
        # old_dir = r"\\10.10.30.14\刘晓东\数据提取\吴驰\1,036,580张车牌标注及转写数据\第一批交付"
        # for root, dirs, files in os.walk(old_dir):
        #     for file in files:
        #         file_set.add(file)
        #
        # dest_dir = r"\\10.10.30.14\刘晓东\数据提取\吴驰\1,036,580张车牌标注及转写数据\补充"
        # work_dir = r"\\10.10.8.123\自采全国车牌数据\客户数据\format_all\data_0818_liuxd_result_result_shen_20200831\最终数据（无措）"
        # count, limit = 0, 30000
        # for province in os.listdir(work_dir):
        #     province_path = os.path.join(work_dir, province)
        #     province_yellow_path = os.path.join(province_path, "yellow_card")
        #     province_yellow_double_path = os.path.join(province_path, "yellow_double_card")
        #     province_blue_path = os.path.join(province_path, "blue_card")
        #     province_green_path = os.path.join(province_path, "green_card")
        #     yellow_imgs = count_img(province_yellow_path)
        #     yellow_double_imgs = count_img(province_yellow_double_path)
        #     blue_imgs = count_img(province_blue_path)
        #     green_imgs = count_img(province_green_path)
        #     total = []
        #     total.extend(yellow_imgs)
        #     total.extend(yellow_double_imgs)
        #     total.extend(green_imgs)
        #     total.extend(blue_imgs)
        #
        #     for file in total[:6000]:
        #         if count < limit:
        #             dest_folder = os.path.split(file.replace(work_dir, dest_dir))[0]
        #             if not os.path.exists(dest_folder):
        #                 os.makedirs(dest_folder)
        #             item_info = [file, file.replace(work_dir, dest_dir)]
        #             copy_img(item_info)
        #             count += 1
        #         else:
        #             break
        #     else:
        #         continue
        #     break

        dest_dir = r"\\10.10.30.14\刘晓东\数据提取\吴驰\1,036,580张车牌标注及转写数据\第一批交付\各个省份"
        work_dir = r"\\10.10.8.123\自采全国车牌数据\客户数据\format_all\data_0818_liuxd_result_result_shen_20200831\最终数据（无措）"
        # work_dir = r"\\10.10.8.123\自采全国车牌数据\客户数据\format_all\data_0818_liuxd_result_result_shen_20200831\港澳粤"
        for province in os.listdir(work_dir):
            if province == "浙":
                province_path = os.path.join(work_dir, province)
                province_yellow_path = os.path.join(province_path, "yellow_card")
                province_yellow_double_path = os.path.join(province_path, "yellow_double_card")
                province_blue_path = os.path.join(province_path, "blue_card")
                province_green_path = os.path.join(province_path, "green_card")

                yellow_imgs = count_img(province_yellow_path)
                yellow_double_imgs = count_img(province_yellow_double_path)
                blue_imgs = count_img(province_blue_path)
                green_imgs = count_img(province_green_path)

                yellow_num, yellow_double_num, blue_num, green_num = len(yellow_imgs), len(yellow_double_imgs), \
                                                                     len(blue_imgs), len(green_imgs)

                sum_lack = 0

                # 黄牌子
                yellow_need_copy, lack_num = [], 0
                if yellow_num < 2000:
                    yellow_need_copy = yellow_imgs
                    lack_num = 2000 - yellow_num
                    if yellow_double_num < lack_num:
                        yellow_need_copy.extend(yellow_double_imgs)
                        lack_num = lack_num - yellow_double_num
                    else:
                        yellow_need_copy.extend(yellow_double_imgs[:lack_num])
                        lack_num = 0
                else:
                    yellow_need_copy = yellow_imgs[:2000]
                yellow_copy_info = [[file, file.replace(work_dir, dest_dir)] for file in yellow_need_copy]
                self.async_executive(copy_img, yellow_copy_info)

                # 绿牌子
                green_need_copy, green_lack_num = [], 0
                if green_num < 2000:
                    green_need_copy = green_imgs
                    green_lack_num = 2000 - green_num
                else:
                    green_need_copy = green_imgs[:2000]
                green_copy_info = [[file, file.replace(work_dir, dest_dir)] for file in green_need_copy]
                self.async_executive(copy_img, green_copy_info)

                # 蓝牌子
                blue_need_copy, blue_lack_num = [], 0
                if blue_num < 2000:
                    blue_need_copy = blue_imgs
                    blue_lack_num = 2000 - blue_num
                else:
                    blue_need = 2000 + green_lack_num + lack_num
                    if blue_num < blue_need:
                        sum_lack = blue_need - blue_num
                    else:
                        blue_need_copy = blue_imgs[:blue_need]

                blue_copy_info = [[file, file.replace(work_dir, dest_dir)] for file in blue_need_copy]
                self.async_executive(copy_img, blue_copy_info)
                print(province, lack_num, green_lack_num, blue_lack_num, sum_lack)


if __name__ == '__main__':
    mlpd = MillionLicensePlateDate()
    mlpd.view_count()
