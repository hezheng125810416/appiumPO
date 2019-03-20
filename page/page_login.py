import page
from base.base import Base


class PageLogin(Base):
    # 点击我
    def page_click_me(self):
        self.base_click(page.login_me)
    # 点击 已有账号，去登录
    def page_click_username_link(self):
        self.base_click(page.login_username_link)
    # 用户名输入
    def page_username(self,username):
        self.base_input(page.login_username,username)
    # 密码框输入
    def page_password(self,password):
        self.base_input(page.login_pwd, password)
    # 点击登录按钮
    def page_login_btn(self):
        self.base_click(page.login_btn)
    # 获取用户文本信息
    def page_get_username_text(self):
        return self.base_get_text(page.login_nickname)
    # 点击左设置按钮
    def page_click_left_btn(self):
        self.base_click(page.login_setting)
    # 拖拽框体
    def page_drag_and_drop(self):
        el1=self.base_element(page.login_send_msg)
        el2=self.base_element(page.login_update_pwd)
        self.base_drag_and_drop(el1,el2)
    # 点击退出按钮
    def page_logout_btn(self):
        self.base_click(page.login_logout_btn)
    # 点击确认按钮退出登录
    def page_logout_btn_ok(self):
        self.base_click(page.login_logout_btn_ok)
    # 登录界面点击左上角叉叉按钮退出到主界面
    def page_login_Window_out(self):
        self.base_click(page.login_loginWindow_out)
    # 组装登录流程
    def page_login(self,username,password):
        self.page_click_me()
        self.page_click_username_link()
        self.page_username(username)
        self.page_password(password)
        self.page_login_btn()

    # 组装退出流程
    def page_logout(self):
        self.page_click_left_btn()
        self.page_drag_and_drop()
        self.page_logout_btn()
        self.page_logout_btn_ok()

    # 判断是否成功退出
    def page_logout_is_ok(self):
        try:
            self.base_element(page.login_me,time=3)
            return True
        except:
            return False