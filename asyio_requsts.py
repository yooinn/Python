# import logging,time,trio,asks
# from lxml import etree
# import warnings
# from functools import partial
#
# url = 'https://blog.csdn.net/fyfugoyfa'
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
# start_time = time.time()
# async def get_urls():
#     headers = {
#         "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#     resp = await asks.get(url, headers=headers,)
#     html = etree.HTML(resp.text)
#     url_list = html.xpath('//div[@class="article-list"]/div/h4/a/@href')
#     return url_list
# async def main():
#     url_list=await get_urls()
#     async with trio.open_nursery() as n:
#         [n.start_soon(request_page,path,)
#              for path in url_list]         #任务入列
#
# async def request_page(url):
#     logging.info('scraping %s', url)
#     s=await asks.get(url)
# trio.run(main)
# end_time = time.time()
# logging.info('total time %s seconds', end_time - start_time)

from lxml import etree
import requests
import logging
import time
import aiohttp
import asyncio

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
url = 'https://blog.csdn.net/fyfugoyfa'
start_time = time.time()

# 先获取博客里的文章链接
def get_urls():
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    resp = requests.get(url, headers=headers)
    html = etree.HTML(resp.text)
    url_list = html.xpath('//div[@class="article-list"]/div/h4/a/@href')
    return url_list

async def request_page(url):
    logging.info('scraping %s', url)
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        return  await response.text()

def main():
    url_list = get_urls()
    loop = asyncio.get_event_loop()
    task = [loop.create_task(request_page(url)) for url in url_list]
    loop.run_until_complete(asyncio.gather(*task))


if __name__ == '__main__':
    main()
    end_time = time.time()
    logging.info('total time %s seconds', end_time - start_time)