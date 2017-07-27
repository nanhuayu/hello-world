# -*- coding: utf-8 -*-
# 引入NLP SDK
from aip import AipNlp
import aip

# 定义常量
APP_ID = '9839224'
API_KEY = '38aM2cGHnGXgfjwPgNv3hgHN'
SECRET_KEY = 'ze0DckCR2GTpFcz8LX17L61Ec8NV9Bc7'

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 初始化AipNlp对象
aipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# 调用分词接口
result = aipNlp.wordseg('你好百度')
print result

# 定义参数变量
option = {'lang_id': 1}

# 调用分词接口
result = aipNlp.wordseg('你好百度', option)
print result

result = aipNlp.wordpos('百度')
print result

