import page
import allure
from base.base import Base


class PurchasePage(Base):
    # 点击购买火车票
    def click_buy_tickets(self):
        self.base_click(page.buy_click_tickets)

    # 选择出发站
    def input_start_station(self, start_station):
        self.base_input(page.buy_start_station, start_station)

    # 选择到达站
    def input_arrive_station(self, arrive_station):
        self.base_input(page.buy_arrive_station, arrive_station)

    # 选择日期
    def input_time(self, time):
        date_input = self.base_find_element(page.buy_start_time)  # "//input[@name='date']"
        self.driver.execute_script("arguments[0].value = arguments[1];", date_input, time)

    # 选择搜索
    def click_find(self):
        self.base_click(page.buy_click_find)

    # 点击购买
    def click_buy_ticket(self):
        self.base_click(page.but_click_buy_ticket)

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

    def click_order_info(self):
        self.base_click(page.buy_order_info)

    def click_order_cancel(self):
        self.base_click(page.buy_order_cancel)

    def click_order_cancel_confirm(self):
        self.base_click(page.buy_order_cancel_confirm)

    def cancel_existing_order(self):
        self.click_order_info()
        if self.base_if_exist(page.buy_order_cancel):
            self.click_order_cancel()
            self.click_order_cancel_confirm()
        self.driver.back()

    # 购票业务
    def buy_tickets(self, start_station, arrive_station, time, name, id_card, phone, protocol):
        with allure.step('切换到购买界面尝试取消已有订单-输入起点{start_station}-终点{arrive_station}-出发时间{time}'):
            self.click_buy_tickets()
            with allure.step('尝试取消已有订单'):
                self.cancel_existing_order()
            self.input_start_station(start_station)
            self.input_arrive_station(arrive_station)
            self.input_time(time)
        with allure.step('点击第一张车票'):
            self.click_find()
            self.click_buy_ticket()
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
