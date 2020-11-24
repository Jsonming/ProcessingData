#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 18:58
# @Author  : yangmingming
# @Site    : 
# @File    : APY161101014_G.py
# @Software: PyCharm
import os
import re
from ProjectsProcess.base import Base


class MandarinStrongAccent132(Base):
    """
    132小时重口音普通话 处理
    """

    def __init__(self):
        pass

    def view_info(self):
        work_dir = r"\\10.10.30.14\d\语音\APY190422003_1025小时重口音普通话手机采集语音数据\完整数据包_processed\data\category"
        for person in os.listdir(work_dir):
            session_path = os.path.join(work_dir, person)
            meta_file = [os.path.join(session_path, file) for file in os.listdir(session_path) if file.endswith(".metadata")][0]

            province = "Guangdong"
            with open(meta_file, 'r', encoding="utf8")as f:
                content = f.read()
                act = re.findall(r"ACC\t(.*?)\n", content)[0]
                if province in act:
                    print(person, act)
                    break


if __name__ == '__main__':
    msa = MandarinStrongAccent132()
    msa.view_info()
