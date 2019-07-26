# coding = utf-8

import urllib
from urllib  import parse

# code = '%B8%B4%B3%F0%D5%DF%C1%AA%C3%CB'   #url编码格式

name = '复仇者联盟'
code = name.encode('gb2312')
# url = 'http://www.longbaidu.com/search.php?'
#
post_dic = {
    'mod':'forum',
    'searchid':'707',
    'orderby':'lastpost',
    'ascdesc':'desc',
    'searchsubmit':'yes',
    'kw': code
}

url_srch = parse.urlencode(post_dic)
print(url_srch)

name_deco = name.encode('gb2312')
print(name_deco)
name_deco = parse.quote(name_deco)
print(name_deco)
name_deco = parse.unquote(name_deco,'utf-8')
print(name_deco)
name_deco = parse.quote(name,'gb2312')
print(name_deco)
name_deco = parse.unquote(name_deco,'utf-8')
print(name_deco)


# deco = '学习一波来了'
deco = '%D1%A7%CF%B0%D2%BB%B2%A8%C0%B4%C1%CB'
# deco = deco.encode('gb2312')
# print(deco)
# deco = parse.quote(deco)
# print(deco)
deco = parse.unquote(deco,'gb2312')
print(deco)
