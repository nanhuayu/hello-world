# 引入文字识别OCR SDK
from aip import AipOcr

# 定义常量
APP_ID = '9838807'
API_KEY = 'ZyNwfGnvQQnYPIuGt25iTWhw'
SECRET_KEY = 'r8RZWXQPMBnS4TyUorzdO6fpFO4h1Ggs'

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 初始化ApiOcr对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 定义参数变量
options = {
  'detect_direction': 'true',
  'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content('general.png'), options)
print(result)
