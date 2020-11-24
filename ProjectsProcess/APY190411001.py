#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 20:07
# @Author  : yangmingming
# @Site    : 
# @File    : APY190411001.py
# @Software: PyCharm
import os
import shutil
from ProjectsProcess.base import VideoBase


class MandarinDialogue(VideoBase):
    src_dir = r"C:\Users\Administrator\Desktop"
    dest_zip = r"C:\Users\Administrator\Desktop\李昺\APY190411001_1351小时普通话自然对话语音数据.zip"

    def __init__(self):
        pass

    def extract_video(self):
        """
        提取 需要的数据
        :return:
        """
        wavs = []
        work_dir = r"C:\Users\Administrator\Desktop\tem"
        for root, dirs, files in os.walk(work_dir):
            for file in files:
                if file.endswith('wav'):
                    file_path = os.path.join(root, file)
                    wavs.append(file_path)
        return wavs

    def gen_copy_info(self, src_wavs):
        copy_infos = []
        dest_folder = os.path.dirname(self.dest_zip)
        dest_folder = os.path.join(dest_folder, "temp")
        for src_wav in src_wavs:
            dest_wav = src_wav.replace(self.src_dir, dest_folder)
            copy_infos.append((src_wav, dest_wav))
        return copy_infos

    def record_src(self, src_wavs):
        src_path_txt = self.dest_zip.replace(".zip", ".txt")
        dest_folder = os.path.dirname(self.dest_zip)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        with open(src_path_txt, 'a', encoding='utf8')as f:
            for src_wav in src_wavs:
                f.write(src_wav + "\n")

    def gen_dest_folder(self, copy_info):
        folder_set = set()
        for info in copy_info:
            _, dest = info
            folder_set.add(os.path.dirname(dest))
        for folder in folder_set:
            if not os.path.exists(folder):
                os.makedirs(folder)

    @staticmethod
    def copy_video(info):
        src_wav, dest_wav = info
        src_txt = src_wav.replace(".wav", ".txt")
        dest_txt = dest_wav.replace(".wav", ".txt")
        src_metadata = src_wav.replace(".wav", ".metadata")
        dest_metadata = dest_wav.replace(".wav", ".metadata")
        shutil.copy(src_wav, dest_wav)
        shutil.copy(src_txt, dest_txt)
        shutil.copy(src_metadata, dest_metadata)

    def run(self):
        """
        主逻辑入口
        :return:
        """
        wavs = self.extract_video()
        self.record_src(wavs)
        copy_infos = self.gen_copy_info(wavs)
        self.gen_dest_folder(copy_infos)
        flag = self.async_executive(self.copy_video, copy_infos)
        if flag:
            dest_folder = os.path.dirname(self.dest_zip)
            dest_folder = os.path.join(dest_folder, "temp")
            self.make_zip(dest_folder, self.dest_zip)
            # shutil.rmtree(dest_folder)


if __name__ == '__main__':
    md = MandarinDialogue()
    md.run()
