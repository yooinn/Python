import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Fucktaobao():
    def __init__(self,names,pwd,sid):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.names=names
        self.pwd=pwd
        self.sid=sid
    def is_element(self, locator, time_out=3) -> bool:
        """判断页面是否存在该元素

        元素存在返回True，否则返回False

        :param locator: 定位器 (By.ID, value=None)
        :param time_out: 超时，默认 3
        :return:
        """
        try:
            WebDriverWait(self.driver, time_out,0.5).until(
                EC.presence_of_element_located(locator)
            )
        except  (TimeoutException, NoSuchElementException) as er:
            return False
        else:
            return True

    def go_tb(self):
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })
        self.driver.implicitly_wait(30)#隐式等待  一次设置全局有效
        self.driver.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.5af911d9QaofNQ&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F")
        self.driver.set_window_size(1178, 1020)#窗口大小
        self.driver.find_element(By.ID, "fm-login-id").send_keys(self.names)#输入
        self.driver.find_element(By.ID, "fm-login-password").send_keys(self.pwd)
        self.driver.find_element(By.CSS_SELECTOR, ".fm-button").click()
        '''验证码滑块'''
        # actions = ActionChains(self.driver)
        # source = self.driver.find_element_by_xpath("//*[@id='nc_1_n1t']/span")  # 需要滑动的元素
        # actions.click_and_hold(source).perform()  # 鼠标左键按下不放
        # actions.move_by_offset(298, 0)  # 需要滑动的坐标
        # actions.release().perform()  # 释放鼠标
        # time.sleep(1)

        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0,63)")
        self.search_product()


    def search_product(self):
        """模拟搜索商品，获取最大页数"""
        self.driver.find_element_by_id('q').send_keys(self.sid)  # 根据id值找到搜索框输入关键字
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-search")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-search").click()
        self.driver.maximize_window()  # 最大化窗口
        while self.driver.find_element_by_xpath('//*[@class="J_Ajax num icon-tag"]') :
            self.driver.execute_script("window.scrollTo(0,2048)")
            self.get_product()
            if  not self.is_element((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.next > a")):
                break
            else:
                self.driver.find_element(By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.next > a").click()#下一页
            time.sleep(2)

        self.driver.close()
    def get_product(self):

        divs = self.driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')

        for div in divs:

            info = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text  # 商品名称

            price = div.find_element_by_xpath('.//strong').text + '元'  # 商品价格

            deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text  # 付款人数
            if deal is None  :deal=0

            name = div.find_element_by_xpath('.//div[@class="shop"]/a').text  # 店铺名称

            print(info, price, deal, name, sep=' | ')

            with open('data1.csv', 'a', newline='') as csvfile:  # newline=''  指定一行一行写入

                csvwriter = csv.writer(csvfile, delimiter=',')  # delimiter=','  csv数据的分隔符

                csvwriter.writerow([info, price, deal, name])  # 序列化数据，写入csv


if __name__ == '__main__':
    names = ''
    pwd = ''
    sid = ''
    tb = Fucktaobao(names, pwd, sid)
    tb.go_tb()

