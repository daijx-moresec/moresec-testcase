#coding: utf-8
from selenium.webdriver.common.action_chains import ActionChains
from Lib import *
monitors_xpath=["//div[contains(@class,\"monitors el-row\")]/div[1]/div/div","//div[contains(@class,\"monitors el-row\")]/div[2]/div/div"]
class AdvMonitor(WebBasic):
    #添加监控
    def add_sec_monitor(self):
        # 添加资产
        self.navigate_page("_网站资产")
        self.search_item("//input[contains(@placeholder,'标题')]", "//button[span/text()='搜索']", url_asset[0])
        self.wait_and_click("//tbody/tr[td[2]/div/span/text()='%s']/td[5]/div/button[2]" % url_asset[0])
        time.sleep(1)   #等待监控

    def isElementExist(self,xpath):
        flag = True
        try:
            self.browser.find_element_by_xpath(xpath)
            return flag
        except:
            flag = False
            return flag

    #查看监控情况
    def check_sec_monitor_leaks(self):
        for i in range(2):
            time.sleep(4)
            ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath(monitors_xpath[i])).perform()  # 鼠标悬停...
            time.sleep(4)
            self.browser.find_element_by_xpath("/html/body/ul/li[1]").click()  # 详情

            if i%2==0:
                xpath='//span[text()=\"共 0 条\"]'
                flag=self.isElementExist(xpath)
                assert flag is True
            else:
                xpath='//ul[contains(@class,\"el-pager\")]/li[4]'
                flag=self.isElementExist(xpath)
                assert flag is True
            self.browser.find_element_by_xpath("//div[contains(@class,\"__back\")]").click()#返回


    #查看sitemap
    def check_sec_monitor_sitemap(self):
        self.navigate_page("监控")
        for i in range(2):
            time.sleep(4)
            ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath(monitors_xpath[i])).perform()#鼠标悬停...
            time.sleep(3)
            self.browser.find_element_by_xpath("/html/body/ul/li[1]").click()#详情
            self.browser.find_element_by_xpath("//h1[text()=\"sitemap\"]").click()#sitemap
            time.sleep(2)
            self.browser.find_element_by_xpath("//div[contains(@class,\"__back\")]").click()#返回

    #添加网站可用性监控
    def add_alive_monitor(self):
        self.navigate_page("监控")
        self.wait_and_click("//h1[text()='网站可用性监控']")
        for item in alive_monitor_data:
            time.sleep(1)   #此处需要显示等待，代码执行速度比页面渲染速度快，弹出框还没有显示出来
            self.wait_and_click("//button[span/text()=' 添加监控']")     #点击添加监控
            self.wait_and_input("//input[contains(@placeholder,'监控名称')]", "test_auto")
            self.browser.find_element_by_xpath("//input[contains(@placeholder,'监控目标')]").send_keys(item["target"])
            if item["period"] != 5:
                self.select_from_dropdownlist("//input[@placeholder='请选择']", "//ul[contains(@class,'el-select-dropdown__list')]", "%s分钟" % item["period"])
            if item["resp_time"] != 110:
                self.clear_and_input("//span[contains(text(),'响应时间')]/div/input", item["resp_time"])
            self.click_ok()
            time.sleep(1)

    def workflow(self):
         self.add_sec_monitor()
         self.add_alive_monitor()