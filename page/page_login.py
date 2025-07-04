import page
import allure
from base.base import Base


class PageLogin(Base):

    # 切换到登录界面
    def click_please_login(self):
        self.base_click(page.login_please_login)

    #  切换主窗口到登录界面
    def change_window(self):
        self.base_change_window()

    # 点击 登录按钮
    def click_login(self):
        self.base_click(page.login_login)

    # 点击 密码登录
    def click_pwd_login(self):
        self.base_click(page.login_click_pwd_login)

    # 输入账号
    def input_account(self, username):
        self.base_input(page.login_input_account, username)

    # 输入密码
    def input_password(self, password):
        self.base_input(page.login_input_password, password)

    # 点击协议
    def click_protocol(self):
        self.base_click(page.login_click_protocol)

    # 登录
    def click_login_button(self):
        self.base_click(page.login_click_login_button)

    # 判断是否登录成功
    def is_login_success(self):
        return self.base_if_exist(page.login_logout)

    # 移动滑块
    def moving_vertify_code(self):
        self.base_move(page.login_moving_btn, page.login_moving_area)

    # 登录业务
    def login(self, username, password, agree_protocol):
        # -同意协议-点击登录-移动滑块-点击空白区域
        with allure.step('切换到登录界面-切换窗口'):
            self.click_please_login()
            self.change_window()
        with allure.step('点击登录-点击账号密码登录'):
            self.click_login()
            self.click_pwd_login()
        with allure.step(f'输入账号{username}-密码{password}'):
            self.input_account(username)
            self.input_password(password)
        with allure.step(f'是否同意协议？{agree_protocol}'):
            if agree_protocol:
                self.click_protocol()
        with allure.step('点击登录按钮'):
            self.click_login_button()

        if username and password and agree_protocol:
            self.moving_vertify_code()
            self.base_move_to_empty_space()

    def get_error_info(self, error_type):
        loc = page.code_mapping[error_type]
        return self.base_get_text(loc)
