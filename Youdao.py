import hashlib
import time,random
from pprint import pprint

import requests
class YoudaoFY():
    def __init__(self,strs):
        self.strs=strs
        self.hede={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '237',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-114072045@10.108.160.17; JSESSIONID=aaac12pgaA53IfpvTfBnx; OUTFOX_SEARCH_USER_ID_NCOO=145324238.0465335; ___rl__test__cookies=1594961104711',
            'DNT': '1',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
    def getdete(self):
        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        bv = "5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
        t = hashlib.md5(bv.encode()).hexdigest()
        r = '%d' % (time.time() * 1000)
        i = r + str(random.randint(0, 10))
        e = self.strs
        signs = "fanyideskweb" + e + i + "mmbP%A-r6U3Nw(n]BjuEU"
        sign = hashlib.md5(signs.encode()).hexdigest()
        dates = {
            'i': e,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'ts': r,
            'bv': t,
            'salt': i,
            'sign': sign,
            'doctype': 'json',
            'version': 2.1,
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        html = requests.post(url, data=dates, headers=self.hede)
        return html
    def __str__(self):
        texts=self.getdete().json()
        return str(texts['translateResult'][0][0])

# print(YoudaoFY('what the fuck'))
