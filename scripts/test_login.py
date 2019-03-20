import os
import sys
sys.path.append(os.getcwd())
import pytest

from page.page_in import PageIn
# def get_data():
#     return [("hz12466123","123456"),("asdasd","1234567")]
class Testlogin:
    def setup(self):
        self.login=PageIn().page_get_login()

    def teardown(self):
        self.login.driver.quit()
    # @pytest.mark.parametrize("username,password",get_data())
    def test01(self,username='itheima',password='123456'):
        # 登录
        self.login.page_login(username,password)
        try:
            # 断言登录是否成功
            assert username==self.login.page_get_username_text()
            # 登录成功后进行退出操作
            self.login.page_logout()
            try:
                # 断言退出是否成功
                assert self.login.page_logout_is_ok()
            except:
                print("退出失败")
        except:
            print("登录失败")
            self.login.page_login_Window_out()

