

# 封装基类
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver=driver
    #用显式等待选择元素
    def base_element(self,loc,time=30,poll=0.5):
       return WebDriverWait(self.driver,timeout=time,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    #点击事件
    def base_click(self,loc):
        self.base_element(loc).click()
    #清空选择元素并输入数据
    def base_input(self,loc,value):
        el=self.base_element(loc)
        el.clear()
        el.send_keys(value)
    #拖拽
    def base_drag_and_drop(self,el1,el2):
        self.driver.drag_and_drop(el1,el2)
    # 获取文本
    def base_get_text(self,loc):
        return self.base_element(loc).text