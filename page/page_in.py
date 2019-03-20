from base.get_driver import get_driver

from page.page_login import PageLogin

"""
    目标：统一入口类
    操作：
        1. 新建侧类 PageIn
            # 获取页面对象方法

"""
driver=get_driver()

class PageIn():
    def page_get_login(self):
        return PageLogin(driver)
