# -*- coding:utf-8 -*-
import uuid,random,time,datetime
# for i in range(0,5):
#     uid = uuid.uuid1()
#     suid = ''.join(str(uid).split('-'))
#     print(suid)
#     print(type(suid) == str)

# new_list = {'/ch/news_regimen':'养生','/ch/news_entertainment':'娱乐','':'推荐','/ch/news_world':'社会','/ch/news_hot':'热点','/ch/news_fashion':'时尚'}
#
# for item in new_list.keys():
#     url = 'https://www.toutiao.com'
#     url = url + item + '/'
#     print(url)
#     print(new_list[item])
#     # 页面元素查找，隐式等待
# for i in range(0,100):
#     print(random.randint(5555,99999))

# a = '//p1.pstatp.com/list/190x124/pgc-image/RJjOGye2rbG5DD'
# aa = 'http://' + a[2:]
# print(aa)

# start_time =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#
# end_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print(end_time-start_time)

# date_str = "2016-11-30 13:53:59"
# print(datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S"))
# print(type(datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")))


# -*- coding: utf-8 -*-
# flake8: noqa
# from qiniu import Auth, put_file, etag
# import qiniu.config
# #需要填写你的 Access Key 和 Secret Key
# access_key = 'DkVNPmXYft7QGCcNweHviR04Jfq7KyaHiOtnQpva'
# secret_key = 'mm3WDobgGhHsJkadkRLqrDBWzLynJsEt8MXMKQpH'
# #构建鉴权对象
# q = Auth(access_key, secret_key)
# #要上传的空间
# bucket_name = 'testspace'
# #上传后保存的文件名
# key = 'my-python-logo.png'
# #生成上传 Token，可以指定过期时间等
# token = q.upload_token(bucket_name, key, 3600)
# #要上传文件的本地路径
# localfile = './20190307005413687195.jpg'
# ret, info = put_file(token, key, localfile)
# print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)
# url = 'http://pnvqejtth.bkt.clouddn.com/'
# print(url + key)
#
# import os
#
# def readFilename(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         return files,dirs,root
# def deleteFilesEndWithPYC(files,dirs,root):
#     for ii in files:
#         if ii.endswith('.jpg'):
#             print('delete:',ii)
#             os.remove(os.path.join(root,ii))
#     for jj in dirs:
#         fi,di,ro = readFilename(root+"\\"+jj)
#         deleteFilesEndWithPYC(fi,di,ro)
#
# files,dirs,root = readFilename("E:\\Work\\program\\toutiao")
# deleteFilesEndWithPYC(files,dirs,root)
#
# rootcategoryName = {'1':'养生','2':'娱乐','3':'社会','4':'时尚','5':'热点'}
# a = '1'
# print(categoryName[a])
b = '<a href="/group/6665850007456842251/" target="_blank" class="img-wrap"><img class="lazy-load-img" src="//p1.pstatp.com/list/190x124/pgc-image/RK5lBCs9PPh0Xq" lazy="loaded"> <!----></a>'
a = ['http://pnvqejtth.bkt.clouddn.com/20190308172704102122_533ee674418411e9938b38baf8d20c25_1.jpg?imageView2/2/h/70','http://pnvqejtth.bkt.clouddn.com/20190308172700180049_533ee674418411e9938b38baf8d20c25_1.jpg?imageView2/2/h/70']
a[0] = 'http://pnvqejtth.bkt.clouddn.com'
print(a[3])
