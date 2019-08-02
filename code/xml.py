# ! /usr/bin/python
# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image

# VEDAI 图像存储位置
src_img_dir = os.path.abspath('.')+'/13'
# VEDAI 图像的 ground truth 的 xml 文件存放位置
src_xml_dir = '/home/henry/File/URPC2018/all_train_data_0829/111'


# 遍历目录读取图片
img_Lists = []
def get_img_list(dir_path):
    if os.path.isdir(dir_path):
        for x in os.listdir(dir_path):
            get_img_list(os.path.join(dir_path, x))
    elif os.path.isfile(dir_path) and dir_path.split('.')[-1] == 'jpg':
        img_Lists.append(dir_path)

get_img_list(src_img_dir)
img_Lists.sort(key=lambda x:x[-10:])
# for i in img_Lists:
#     print(i)

# 创建xml文件，存入图片信息
for img_item in img_Lists:
    im = Image.open(img_item)  #打开图片 为了记录图片的长宽数据
    img = os.path.split(img_item)[1].split('.')[0]
    width, height = im.size

    # write in xml file
    # os.mknod(src_xml_dir + '/' + img + '.xml')
    xml_file = open((src_xml_dir + '/' + img + '.xml'), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('    <folder>VOC2007</folder>\n')
    xml_file.write('    <filename>' + str(img) + '.jpg' + '</filename>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>3</depth>\n')
    xml_file.write('    </size>\n')
    xml_file.close()
# 读取全部信息
txt_file = open('YDXJ0013.txt')

for line in txt_file.readlines():
    gt = line.splitlines()
    # print(gt)
#     gt = txt_file.readline().splitlines()
#     # gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()

    # write the region of image on xml file
    for img_each_label in gt:
        spt = img_each_label.split(' ')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。

        # 判断是否需要写入xml
        if spt[6] == '0':
            # print (gt)

            # 打开相应xml文件
            # print(spt[5].zfill(6))
            xml_file = open((src_xml_dir + '/' + spt[5].zfill(6) + '.xml'), 'a')
            xml_file.write('    <object>\n')
            xml_file.write('        <name>' + str(spt[9]) + '</name>\n')
            xml_file.write('        <pose>Unspecified</pose>\n')
            xml_file.write('        <truncated>0</truncated>\n')
            xml_file.write('        <difficult>0</difficult>\n')
            xml_file.write('        <bndbox>\n')
            xml_file.write('            <xmin>' + str(spt[1]) + '</xmin>\n')
            xml_file.write('            <ymin>' + str(spt[2]) + '</ymin>\n')
            xml_file.write('            <xmax>' + str(spt[3]) + '</xmax>\n')
            xml_file.write('            <ymax>' + str(spt[4]) + '</ymax>\n')
            xml_file.write('        </bndbox>\n')
            xml_file.write('    </object>\n')
            xml_file.close()

# 补上结尾
for i in range(4500):
    xml_file = open((src_xml_dir + '/' + str(i).zfill(6) + '.xml'), 'a')
    xml_file.write('</annotation>')
    xml_file.close()