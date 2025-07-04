import page
import allure
from base.base import Base


class TicketPage(Base):
    # 点击购买火车票
    def click_buy_tickets(self):
        self.base_click(page.buy_click_tickets)

    # 取消现有订单（如果有）
    def cancel_existing_order(self):
        self.click_order_info()
        if self.base_if_exist(page.buy_order_cancel):
            self.click_order_cancel()
            self.click_order_cancel_confirm()
        self.driver.back()

    # 点击查看订单
    def click_order_info(self):
        self.base_click(page.buy_order_info)

    # 点击取消订单
    def click_order_cancel(self):
        self.base_click(page.buy_order_cancel)

    # 点击确定
    def click_order_cancel_confirm(self):
        self.base_click(page.buy_order_cancel_confirm)

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

    # 搜索火车票业务
    def search_tickets(self, start_station, arrive_station, time):
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
