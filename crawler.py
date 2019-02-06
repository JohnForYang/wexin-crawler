# -*- coding: utf-8 -*-
"""
运行方式:
mitmdump -s crawler.py
"""

import mitmproxy.http
from mitmproxy import ctx


class WixinCrawler:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        print('拦截到request')
        print('flow.request.content类型：%s' % type(flow.request.content))
        print(flow.request.content)
        print('flow.request.headers类型：%s' % type(flow.request.headers))
        print(flow.request.headers)
        print('flow.request.url类型：%s' % type(flow.request.url))
        print(flow.request.url)
        
    def response(self, flow: mitmproxy.http.HTTPFlow):
        print('拦截到response')
        print('flow.request.url类型：%s' % type(flow.request.url))
        print(flow.request.url)
        print('flow.response.text类型：%s' % type(flow.response.text))
        print(flow.response.text)

        

addons = [
    WixinCrawler()
]