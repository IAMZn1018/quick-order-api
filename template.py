from src.meal import get_content

from falcon_cors import CORS
import falcon
import json
import os


class Template1(object):

    def on_get(self, req, resp):
        '''
        '''
        menu = get_content()
        result = {
            'code': 200,
            'content': {
                'r': menu
            },
            'message': 'success'
        }
        resp.body = json.dumps(result)
        resp.status = falcon.HTTP_200

class Template2(object):

    def on_post(self, req, resp):
        '''
        '''
        print(req.params)
        print(req.headers)
        content = req.get_param('content', '')
        num = req.get_param('num', '')
        strTime = req.get_param('strTime', '')
        remark = req.get_param('remark', '')
        totalpricve = req.get_param('totalprice', '')
        print(content, num, strTime, remark, totalpricve)
        result = {
            'code': 200,
            'content': {
                'r': '请求成功'
            },
            'message': 'success'
        }

        resp.body = json.dumps(result)
        resp.status = falcon.HTTP_200

class Template3(object):

    def on_post(self, req, resp):
        '''
        '''
        suggestion = req.get_param('suggestion', '')
        print(suggestion)
        result = {
            'code': 200,
            'content': {
                'r': '请求成功'
            },
            'message': 'success'
        }

        resp.body = json.dumps(result)
        resp.status = falcon.HTTP_200 

public_cors = CORS(allow_all_origins=True,
                   allow_all_headers=True, allow_all_methods=True)

application = falcon.API(middleware=[public_cors.middleware])
application.req_options.auto_parse_form_urlencoded=True
# router
application.add_route('/meal', Template1())
application.add_route('/order', Template2())
application.add_route('/suggestion', Template3())