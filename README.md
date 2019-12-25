# 使用yolov3_keras模型进行实时目标检测（基于Penn-Fudan Database行人数据集）

## 使用方法：
1. 通过以下命令将源项目克隆到本地工作目录
```cpp
git clone https://github.com/qqwweee/keras-yolo3
```
2. 下载此修改过的项目，复制到上面项目的文件夹，全部替换:是

3. 把数据集更改成你要训练的数据集

4. `keras-yolo3/VOCdevkit/VOC2007`文件make_main_txt01.py脚本和根目录下voc_annotation02.py相继执行将xml转为voc要求的格式

5. config配置后执行traing
