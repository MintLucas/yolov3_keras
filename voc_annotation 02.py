import xml.etree.ElementTree as ET
from os import getcwd
'''
make x_label_map
import os
classes = ["laptop", "smallelectronicequipmen", "powerbank", "glassbottle","winebottle","umbrella","metalcup","lighter","pressure","drinkbottle","scissor",
           "defibrillator","gun","magazine_clip","fingerlock","slingshot","expandablebaton","zippooil","nailpolish","binghu","handcuffs","fireworks_crackers","knife"]
x_label_map = open('./x_label_map.txt','w')
for i in range(len(classes)):
    x_label_map.write("item {\n  id: %d\n  name: '%s'\n}\n" %(i+1,classes[i]))
x_label_map.close()
'''


sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["laptop", "smallelectronicequipmen", "powerbank", "glassbottle","winebottle","umbrella","metalcup","lighter","pressure","drinkbottle","scissor",
           "defibrillator","gun","magazine_clip","fingerlock","slingshot","expandablebaton","zippooil","nailpolish","binghu","handcuffs","fireworks_crackers","knife"]
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

wd = getcwd()

for year, image_set in sets:
    image_ids = open('VOCdevkit%s/VOC%s/ImageSets/Main/%s.txt'%(trainingset_name, year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit%s/VOC%s/JPEGImages/%s.jpg'%(wd, trainingset_name, year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

