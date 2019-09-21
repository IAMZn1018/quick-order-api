# -*-coding:utf-8 -*-

import json, csv, datetime

# 返回请求结果
def response_data(content, code=200, message='success'):
    ret = {
        'code': code,
        'message': message,
        'content': content
    }
    return json.dumps(ret, ensure_ascii=False)

def get_content():
    f =  open('./src/config/xiangcun.json', encoding='utf-8')
    json_data = json.load(f)
    return json_data
