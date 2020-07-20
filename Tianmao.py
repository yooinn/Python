from pprint import pprint

import requests
from lxml import etree

sid='U盘'
url = f"https://list.tmall.com/search_product.htm?q={sid}&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton"

headers = {
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'Referer': 'https://www.tmall.com/',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 't=21aaf0eeaafa3cb518ae1518a6e7a099; _tb_token_=f8e635e15316b; cookie2=18dbeb11c34efce77f1b43c568a46491; _med=dw:1536&dh:864&pw:1920&ph:1080&ist:0; cq=ccp%3D1; res=scroll%3A1142*7056-client%3A1142*662-offset%3A1142*7056-screen%3A1536*864; pnm_cku822=098%23E1hvLQvUvbpvUvCkvvvvvjiPnL5U6j3PPsFhtjnEPmPO1jYjR2zwljYbn2s90jtnRphvCvvvvvmtvpvIvvvvHhCvvWQvvvb2phvU79vvvQCvpvACvvv2vhCv2R9vvvbUphvUSgyCvvOUvvVva6JivpvUvvmvKoShyKUEvpCWmmE%2Fvvw%2Bkb5BSfOBfvDrQjc6KqpKodzafX7reBlv%2BExrs8TJnDeDyO2vHdUfbjc6D76OdeQHYExrz8TNwZ29snsIeEDzBWkQ0f06W9hCvvOvCvvvphvPvpvhvv2MMTwCvvpvvUmm; t=21aaf0eeaafa3cb518ae1518a6e7a099; _tb_token_=f8e635e15316b; cookie2=18dbeb11c34efce77f1b43c568a46491'
}

response = requests.get( url, headers=headers,)

html=etree.HTML(response.text)

names_title=html.xpath('//*[@id="J_ItemList"]/div/div/p/a/@title')#名称
price=html.xpath('//*[@id="J_ItemList"]/div/div/p/em/@title')#价格
deal=html.xpath('//*[@id="J_ItemList"]/div/div/p/span/em/text()')#月成交
comment=html.xpath('//*[@id="J_ItemList"]/div/div/p/span/a/text()')#评论
#展示图片 只能匹配55个 缺失5个图片地址
imga=html.xpath('//a[@class="productImg"]/img/@data-ks-lazyload')
#全部图片
img=[i.replace('_30x30.jpg', '') for i in html.xpath('//*/div[@class="proThumb-wrap"]/p/b/img/@data-ks-lazyload')]
import pandas as pd
sr = pd.DataFrame({'名称':names_title,
                   '价格':price,
                   '月成交':deal,
                   '评论':comment,
                   })
sr.to_csv('Tianmao.csv')