# -*- coding: utf-8 -*-

# 定义常量
APP_ID = '9839224'
API_KEY = '38aM2cGHnGXgfjwPgNv3hgHN'
SECRET_KEY = 'ze0DckCR2GTpFcz8LX17L61Ec8NV9Bc7'

# 引入AipImageCensor SDK
from aip import AipImageCensor


# 初始化AipImageCensor对象
aipImageCensor = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 调用色情识别接口
result = aipImageCensor.antiPorn(get_file_content('antiporn.jpg'))
print(result)
