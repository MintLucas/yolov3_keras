import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["face", "person", "red_light", "green_light"]
trainingset_name = ""

def convert_annotation(year, image_id, list_file):
    in_file = open('VOCdevkit%s/VOC%s/Annotations/%s.xml'%(trainingset_name, year, image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

def voc_annotation(format, open_method):
    wd = getcwd()
    for year, image_set in sets:
        image_ids = open('VOCdevkit%s/VOC%s/ImageSets/Main/%s/%s.txt'%(trainingset_name, year, format, image_set)).read().strip().split()
        list_file = open('%s_%s.txt'%(year, image_set), open_method)
        for image_id in image_ids:
            list_file.write('%s/VOCdevkit%s/VOC%s/%sImages/%s.%s'%(wd, trainingset_name, year, format.upper(), image_id, format))
            convert_annotation(year, image_id, list_file)
            list_file.write('\n')
        list_file.close()

def main():
    voc_annotation('jpg', 'w')
    voc_annotation('png', 'a')


if __name__ == '__main__':
    main()
