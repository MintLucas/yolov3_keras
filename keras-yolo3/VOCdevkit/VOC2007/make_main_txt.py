import os
import random


def make_main_txt(trainval_percent, train_percent, filepath, txtsavepath, format):
	files = os.listdir(filepath)
	print(files)
	num = len(files)
	list=range(num)
	tv = int(num * trainval_percent)
	tr = int(tv * train_percent)
	trainval = random.sample(list, tv)
	train = random.sample(trainval, tr)

	ftrainval = open('%s/trainval.txt' % txtsavepath, 'w')
	ftest = open('%s/test.txt' % txtsavepath, 'w')
	ftrain = open('%s/train.txt' % txtsavepath, 'w')
	fval = open('%s/val.txt' % txtsavepath, 'w')
	 
	for i in list:
		if files[i][-3:] == format:
		    name = files[i][:-4]+'\n'
		    if i in trainval:
		        ftrainval.write(name)
		        if i in train:
		            ftrain.write(name)
		        else:
		            fval.write(name)
		    else:
		        ftest.write(name)
	 
	ftrainval.close()
	ftrain.close()
	fval.close()
	ftest .close()


def main():
	jpgfilepath = 'JPGImages'
	pngfilepath = 'PNGImages'
	make_main_txt(1, 1, jpgfilepath, 'ImageSets/Main/jpg', 'jpg')
	make_main_txt(1, 1, pngfilepath, 'ImageSets/Main/png', 'png')


if __name__ == '__main__':
	main()
