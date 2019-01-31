import os
import random

trainval_percent = 0.9#全0即都划分为测试集
train_percent = 0.9#tv里的0.9作训练0.1来测试，用留出法直接划分训练集验证机和测试集，
#或tv作k-折交叉验证
xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets\\Main'
total_xml = os.listdir(xmlfilepath)#路径下所有文件名存进一个list

num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)#tv里train的比例，tv外为test
trainval= random.sample(list,tv)#list列表里随机取tv个值并打乱
train=random.sample(trainval,tr)

ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('ImageSets/Main/test.txt', 'w')
ftrain = open('ImageSets/Main/train.txt', 'w')
fval = open('ImageSets/Main/val.txt', 'w')

for i  in list:
    name=total_xml[i][:-4]+'\n'#舍去字符串后四位
    if i in trainval:#在tv里再分tr和val
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:#不在tv里写进test里
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()
