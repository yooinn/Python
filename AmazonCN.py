import time
import requests
from lxml import  etree
class AmazonCN():
    def __init__(self,k:str):
        self.k=k
        self.qid=int(time.time())
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
    def Request(self):
        for i in range(1,11):
            print(i)
            url = f'https://www.amazon.cn/s?k={self.k}&page={i}&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&qid={self.qid}&ref=sr_pg_{i}'
            html=requests.get(url,headers=self.headers)
            HT=etree.HTML(html.text)
            yield  HT
    def CleanDate(self,HT):
        items={}
        shot = HT.xpath('//*[@class="s-main-slot s-result-list s-search-results sg-row"]/div/div/span/div/div')
        for shots in shot:
            ShotItem = shots.xpath('./span/a/div/img/@src|'
                                   './span/a/div/img/@alt|'
                                   './span/a/@href|'
                                   './div/div/span/@aria-label|'
                                   './div/div/div/a/span/span/text()')
            try:
                items['地址'] = ShotItem[0]
                items['图片'] = ShotItem[1]
                items['名字'] = ShotItem[2]
                items['评分'] = ShotItem[3]
                items['评论'] = ShotItem[4]
                items['价格'] = ShotItem[5]
            except Exception as f:
                print('Erre: ',f)

    def main(self):
            for i in self.Request():
                self.CleanDate(i)
am=AmazonCN('硬盘')
am.main()
