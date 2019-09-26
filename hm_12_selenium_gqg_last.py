from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import re


class Gqg:
    def __init__(self):
        chrome_options = Options()
        # 沒有這一行會自動開啟瀏覽器
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options,
                                       executable_path=r'D:\Study\Python2\chromedriver\chromedriver.exe')
        self.driver2 = webdriver.Chrome(chrome_options=chrome_options,
                                        executable_path=r'D:\Study\Python2\chromedriver\chromedriver.exe')

        self.url = "http://govmail.qingdao.gov.cn/government/mainfrm.aspx"

    def get_content_list(self):
        wait = WebDriverWait(self.driver, 2)
        time.sleep(3)
        while True:
            li_list = self.driver.find_elements_by_xpath("//div[@id='TabTab01Con1']/div[@class='box1_list_text']/ul/li")

            # print(len(li_list))
            for index, li in enumerate(li_list):
                li_list2 = self.driver2.find_elements_by_xpath(
                    "//div[@id='TabTab01Con1']/div[@class='box1_list_text']/ul/li")
                a_tag = li.find_element_by_xpath("./span[@class='typic01']/a").get_attribute("onclick")
                b = re.findall(r",\'(\d)\'\)", a_tag)[0]
                # print("index=%d" % index)
                if b == "1":
                    guid = re.findall(r"ViewReplyCheck\(\'\{(.*?)\}", a_tag)[0]
                    # print(guid)
                    for index2, li2 in enumerate(li_list2):
                        if index2 == index:
                            item = {}
                            item["guid"] = guid
                            li2.find_element_by_xpath("./span[@class='typic01']/a/div[1]").click()
                            handles2 = self.driver2.window_handles
                            # print(handles2)
                            size = len(handles2)
                            # print("index2=%d" % index)
                            # print("size=%d" % size)
                            # 主頁
                            handles_main = self.driver2.current_window_handle
                            # 跳到新開頁面
                            self.driver2.switch_to.window(handles2[-1])
                            stree = self.driver2.find_element_by_xpath(
                                "//div[@class='dafu_information']/div[@class='dafu_kuang']")
                            item["title"] = stree.find_element_by_xpath("./table//tr[1]/td[2]").text
                            item["public_time"] = stree.find_element_by_xpath("./table//tr[2]/td[4]").text
                            item["content"] = stree.find_element_by_xpath("./table//tr[3]/td[2]").text
                            item["seq"] = stree.find_element_by_xpath("./table//tr[5]/td[2]").text
                            item["ans_dep"] = stree.find_element_by_xpath("./table//tr[6]/td[2]").text
                            item["ans_time"] = stree.find_element_by_xpath("./table//tr[6]/td[4]").text
                            item["ans_content"] = stree.find_element_by_xpath("./table//tr[7]/td[2]").text
                            print(item)
                            # 跳回主畫面
                            self.driver2.switch_to.window(handles_main)
                            break
                # break

            next_page = self.driver.find_elements_by_link_text("下一页")
            if len(next_page) > 0:
                self.driver.find_element_by_link_text("下一页").click()
                time.sleep(3)
                print(self.driver.current_url)
                self.driver2.get(self.driver.current_url)
                print("=" * 90)
            else:
                break

        self.driver.close()
        self.driver.quit()
        self.driver2.close()
        self.driver2.quit()
        print("<gqg>爬蟲結束....")

    def run(self):
        print("<gqg>爬蟲開始....")
        # 1.取得url
        self.driver.get(self.url)
        self.driver2.get(self.url)
        self.get_content_list()


if __name__ == '__main__':
    gqg =Gqg()
    gqg.run()