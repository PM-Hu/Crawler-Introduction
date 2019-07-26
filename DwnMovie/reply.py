# coding = utf-8

import requests
import os
from bs4 import BeautifulSoup

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

url = 'http://www.longbaidu.com/forum.php?mod=viewthread&tid=76889&page=8#lastpost'

messg = '我是一个post程序！'
messg = messg.encode('gb2312')

postdata ={
    'mod':'post',
    'action': 'reply',
    'fid': '39',
    'tid': '76889',
    'replysubmit': 'yes',
    'infloat': 'yes',
    'handlekey':'fastpost',
    'inajax': '1',
    'message': messg ,
    'posttime':'1562286615',
    'formhash':'0639f7f6',
    'usesig': '1',
    'subject': '  '
}


def log_in(url,postdata,headers):
    session = requests.Session()
    session.post(url,data=postdata,headers=headers)


if __name__ == '__main__':

    log_in(url,postdata,headers)

