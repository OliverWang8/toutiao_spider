# -*- coding:utf-8 -*-
import os
path = "E:\\Work\\program\\toutiao"
# 删除本地图片函数
def readFilename(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files,dirs,root
def deleteFilesEndWithPYC(files,dirs,root):
    for ii in files:
        if ii.endswith('.jpg'):
            print('delete:',ii)
            os.remove(os.path.join(root,ii))
    for jj in dirs:
        fi,di,ro = readFilename(root+"\\"+jj)
        deleteFilesEndWithPYC(fi,di,ro)
files,dirs,root = readFilename(path)
deleteFilesEndWithPYC(files,dirs,root)