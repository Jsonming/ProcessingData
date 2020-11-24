import os


def to_walk_dir(work_dir):
    # 全局变量 person_info
    global person_info
    # 遍历当前文件夹的所有文件
    print(work_dir)
    for work_d in os.listdir(work_dir):
        work_di = os.path.join(work_dir, work_d)
        for d in os.listdir(work_di):
            # 以  _  切分文件名，获得性别，年龄
            print(d)
            if '__' in d:
                os.chdir(work_dir)
                new_name = d.replace('__', '_')
                os.rename(d, new_name)
            num, sex, n, age = d.split('_')

            # 获取年龄后，需要将字符串类型转换为 整数类型
            age = int(age)
            if age < 3:
                person_info['<3'][sex] += 1
            if age >= 3 and age < 6:
                person_info['3-6'][sex] += 1
            if age >= 6 and age < 9:
                person_info['6-9'][sex] += 1
            if age >= 9 and age < 12:
                person_info['9-12'][sex] += 1
            if age >= 12 and age < 15:
                person_info['12-15'][sex] += 1
            if age >= 15 and age < 20:
                person_info['15-20'][sex] += 1
            if age >= 20 and age < 40:
                person_info['20-40'][sex] += 1
            if age >= 40 and age < 60:
                person_info['40-60'][sex] += 1
            if age >= 60:
                person_info['>60'][sex] += 1


if __name__ == '__main__':

    person_info = dict()
    person_info['<3'] = {}
    person_info['3-6'] = {}
    person_info['6-9'] = {}
    person_info['9-12'] = {}
    person_info['12-15'] = {}
    person_info['15-20'] = {}
    person_info['20-40'] = {}
    person_info['40-60'] = {}
    person_info['>60'] = {}

    # 有的数据的用的是Male，Female，注意大小写
    person_info['<3']['male'] = 0
    person_info['<3']['female'] = 0

    person_info['3-6']['male'] = 0
    person_info['3-6']['female'] = 0

    person_info['6-9']['male'] = 0
    person_info['6-9']['female'] = 0

    person_info['9-12']['male'] = 0
    person_info['9-12']['female'] = 0

    person_info['12-15']['male'] = 0
    person_info['12-15']['female'] = 0

    person_info['15-20']['male'] = 0
    person_info['15-20']['female'] = 0

    person_info['20-40']['male'] = 0
    person_info['20-40']['female'] = 0

    person_info['40-60']['male'] = 0
    person_info['40-60']['female'] = 0

    person_info['>60']['male'] = 0
    person_info['>60']['female'] = 0

    work_dir = r'\\10.10.30.14\d\图像\APY190530001_26,129人多人种7种表情识别数据\完整数据包\data\Yellow_race\Chinese'
    work_dir = r'\\10.10.30.14\d\图像\APY190530001_26,129人多人种7种表情识别数据\完整数据包\data\Yellow_race\Southeast_Asians'
    to_walk_dir(work_dir)
    # 输出结果
    for item in person_info:
        print(item, person_info[item]['male'], person_info[item]['female'])
