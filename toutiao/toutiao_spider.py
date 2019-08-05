# -*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import time,random,os,urllib.request,datetime,uuid,pymongo
from qiniu import Auth, put_file, etag

# 处理文章内容图片，下载到本地，上传到七牛云函数
def getImg(html,uuid,categoryId):
    # 本地路径
    path = 'E:\\Work\\program\\toutiao\\'
    if not os.path.isdir(path):
        os.mkdir(path)
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img')
    for img in images:
        link = img.get('src')
        #name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + '_' + uuid + '_' + categoryId
        urllib.request.urlretrieve(link, '{}{}.jpg'.format(path, name))
        fileName = name + '.jpg'
        localFale = './' + fileName
        token = q.upload_token(bucket_name, fileName, 3600)
        ret, info = put_file(token, fileName, localFale)
        assert ret['key'] == fileName
        assert ret['hash'] == etag(localFale)
        url = 'http://pnvqejtth.bkt.clouddn.com/'
        newUrl = url + fileName
        img['src'] = newUrl

        print(newUrl)
    print(soup)
    return str(soup)

# 处理缩略图，上传到七牛云函数
def getImg1(image,uuid,categoryId):
    path = 'E:\\Work\\program\\toutiao\\'
    if not os.path.isdir(path):
        os.mkdir(path)
    name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + '_' + uuid + '_' + categoryId
    urllib.request.urlretrieve(image, '{}{}.jpg'.format(path, name))
    fileName = name + '.jpg'
    localFale = './' + fileName
    token = q.upload_token(bucket_name, fileName, 3600)
    ret, info = put_file(token, fileName, localFale)
    assert ret['key'] == fileName
    assert ret['hash'] == etag(localFale)
    url = 'http://pnvqejtth.bkt.clouddn.com/'
    newUrl = url + fileName + '?imageView2/2/h/70'
    # img['src'] = newUrl
    print(newUrl)
    return newUrl

# 七牛云设置
access_key = 'DkVNPmXYft7QGCcNweHviR04Jfq7KyaHiOtnQpva'
secret_key = 'mm3WDobgGhHsJkadkRLqrDBWzLynJsEt8MXMKQpH'
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 要上传的空间
bucket_name = 'testspace'

# 连mongo数据库
host_test = "182.92.1.27"
host_usa = '156.233.64.146'
port = 27017
user = 'admin'
password = 'a1b2c3d4'
myclient = pymongo.MongoClient(host_test,port)
mydb = myclient.news# news数据库
mydb.authenticate(user,password)
collection = mydb.article
start_time =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
is_web = input("请输入是否开启浏览器（1.开启 2.不开启）：")
if is_web == '1':
    # 开启浏览器爬虫
    wd = webdriver.Chrome()  # helloword
else:
# 不开启浏览器爬虫
    option = webdriver.ChromeOptions()
    option.set_headless()
    wd = webdriver.Chrome(chrome_options=option)


# new_list = {'/ch/news_regimen':'1','/ch/news_entertainment':'2','/ch/news_world':'3','/ch/news_hot':'5','/ch/news_fashion':'4'}
new_list = {'/ch/news_regimen':'1'}
categoryName = {'1':'养生','2':'娱乐','3':'社会','4':'时尚','5':'热点'}

for item in new_list.keys():
    url = 'https://www.toutiao.com'
    url = url + item + '/'
    print(url)
    # 页面元素查找，隐式等待
    wd.implicitly_wait(10)
    wd.get(url)
    time.sleep(1)
    wd.maximize_window()

    # 页面下拉加载
    drop = 1
    for i in range(0,drop):
        wd.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        i += 1
        time.sleep(random.randint(3,6))

    # 查找页面元素
    list_new = wd.find_element_by_class_name('wcommonFeed')#feed-infinite-wrapper,wcommonFeed
    list_news = list_new.find_elements_by_class_name('link')
    print(len(list_news))

    for new in range(0,len(list_news)):
        # 文章id:uuid
        uid = uuid.uuid1()
        article_id = ''.join(str(uid).split('-'))
        # 文章备注
        article_memo = ''
        # 文章分类
        article_category = new_list[item]
        # 文章分类名字
        article_categoryName = categoryName[article_category]
        # 文章阅读量
        article_readcount = random.randint(5555, 99999)
        list_new = wd.find_element_by_class_name('wcommonFeed')
        list_news = list_new.find_elements_by_class_name('link')
        list_wrap = list_new.find_elements_by_class_name('img-wrap')
        time.sleep(2)
        wrap1 = list_wrap[new].find_elements_by_tag_name('img')
        print(len(wrap1))
        if len(wrap1) > 0:
            link = []
            for a in range(0,len(wrap1)):
                img_url = wrap1[a].get_attribute('src')
                link.append(img_url)
            print(link)
            if len(link) == 1:
                article_thumb1 = getImg1(link[0],article_id,article_category)
                article_thumb2 = ''
                article_thumb3 = ''
            elif len(link) == 2:
                article_thumb1 = getImg1(link[0],article_id,article_category)
                article_thumb2 = getImg1(link[1],article_id,article_category)
                article_thumb3 = ''
            else:
                article_thumb1 = getImg1(link[0],article_id,article_category)
                article_thumb2 = getImg1(link[1],article_id,article_category)
                article_thumb3 = getImg1(link[2],article_id,article_category)
            list_news[new].click()
            time.sleep(2)
            handles = wd.window_handles
            wd.switch_to.window(handles[1])

            # 文章标题
            article_title = wd.find_elements_by_class_name('article-title')
            if len(article_title) > 0:
                # 文章标题
                article_title = wd.find_element_by_class_name('article-title').text
                # 文章图文详情
                content = wd.find_element_by_class_name('article-content').get_attribute('innerHTML')
                article_content = getImg(content, article_id, article_category)

                # 文章来源/创建时间
                sub = wd.find_element_by_class_name('article-sub')
                subs = sub.find_elements_by_tag_name('span')
                if len(subs) == 3:
                    article_from = subs[1].text
                    article_createtime = datetime.datetime.strptime(subs[2].text, "%Y-%m-%d %H:%M:%S")
                else:
                    article_from = subs[0].text
                    article_createtime = datetime.datetime.strptime(subs[1].text, "%Y-%m-%d %H:%M:%S")

                # 插入数据库字段结构
                inser_dict = {
                    '_id': article_id,
                    'title': article_title,
                    'content': article_content,
                    'memo': article_memo,
                    'category': article_category,
                    'categoryName': article_categoryName,
                    'readCount': article_readcount,
                    'from': article_from,
                    'createTime': article_createtime,
                    'thumb1': article_thumb1,
                    'thumb2': article_thumb2,
                    'thumb3': article_thumb3,
                    'platFormFlag': '1',
                }

                collection.insert_one(inser_dict)
            wd.close()
            wd.switch_to.window(handles[0])
            time.sleep(2)
        else:
            pass

    wd.quit()
myclient.close()
end_time =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

print(start_time)
print(end_time)