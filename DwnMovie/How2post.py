# coding = utf-8

import requests
import os
from bs4 import BeautifulSoup

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}


url1 = 'http://www.longbaidu.com/member.php?mod=logging&action=login'
url2 = 'http://www.longbaidu.com'

postdata ={
    'formhash':'148e9a5f',
    'referer':'http://www.longbaidu.com/',
    'username':'周哈哈',
    'password':'180710',
    'questionid':'0',
    'answer':''
}

def mkdir(path_name):
    path = os.getcwd()
    subpath = os.path.join(path, path_name)
    # subpath = path + os.sep + path_name
    isdirexist = os.path.exists(subpath)
    if not isdirexist:
        # 创建子文件夹
        # os.mkdir(subpath)   #只创建该目录 父目录不创建
        os.makedirs(subpath)
    else:
        # 提示
        print("链接存放于", subpath)

def savesrc(cnt,filepath):
    # os.remove(filepath) #删除文件
    stm = open(filepath,'w',encoding='utf-8') #创建文件
    stm.write(' *** Warning! Only for study! *** \n *** save as utf-8 ***\n')
    for i in cnt.find_all('a'):
        try:
            ref = i.attrs['href']
            stm.write(ref+'\n')
        except:
            continue
    stm.close()

def log_in(url,postdata,headers):
    session = requests.Session()
    session.post(url,data=postdata,headers=headers)

    # url2 = 'http://www.longbaidu.com/home.php?mod=space&uid=165925'
    # after = session.get(url2,headers=headers)
    # print(after.text)
    # print('Good, sucess post it !')
    # print('Oops, errors happened !')
    #以后加上检测登录成功

if __name__ == '__main__':

    path_name = '网页中的电影链接'
    filepath = os.getcwd() + os.sep + path_name + os.sep + 'link.txt'
    mkdir(path_name)
    # log_in(url1,postdata,headers)
    f = requests.get(url2)
    cnt = BeautifulSoup(f.content, "lxml")
    savesrc(cnt,filepath)