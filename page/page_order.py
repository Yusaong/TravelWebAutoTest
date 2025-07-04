import page
import allure
from base.base import Base


class OrderPage(Base):
    # 输入购票人姓名
    def input_buy_ticket_name(self, name):
        self.base_input(page.buy_input_name, name)

    # 输入购票人身份证信息
    def input_buy_ticket_idcard(self, id_card):
        self.base_input(page.buy_input_idcard, id_card)

    # 输入取票人姓名
    def input_contact_name(self, name):
        self.base_input(page.buy_input_contact_name, name)

    # 输入取票人电话
    def input_contact_phone(self, phone):
        self.base_input(page.buy_input_contact_phone, phone)

    # 点击提交订单
    def click_submit(self):
        self.base_click(page.buy_click_submit)

    # 提交订单成功
    def submit_access(self):
        return self.base_if_exist(page.buy_submit_success)

    # 获取异常提示信息
    def buy_get_error_info(self):
        return self.base_get_text(page.buy_submit_fail_info)

    # 滑动页面使得确认购买按钮露出
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_protocol(self):
        self.base_click(page.buy_click_protocol)

    # 订票业务
    def order_tickets(self, name, id_card, phone, protocol):
        with allure.step('输入个人信息-姓名{name}-身份证号{id_card}-电话{phone}'):
            self.input_buy_ticket_name(name)
            self.input_buy_ticket_idcard(id_card)
            self.input_contact_name(name)
            self.input_contact_phone(phone)
        with allure.step('下拉到页面底部-勾选协议{protocol}-点击购买'):
            self.scroll_to_bottom()
            if not protocol:
                self.click_protocol()
            self.click_submit()
