import page
import allure

from base.base import Base


class PagePublish(Base):
    # 点击攻略
    def click_strategy(self):
        self.base_click(page.publish_click_travel)

    # 点击发表游记
    def click_publish_travel_notes(self):
        self.base_click(page.publish_click_travel_notes)

    # 以前发表过游记时会出现新窗口问是否修改现有游记还是新建
    def click_new_travel_notes(self):
        if self.base_if_exist(page.publish_new_travel_notes):
            self.base_click(page.publish_new_travel_notes)

    #  切换主窗口到游记界面
    def publish_change_window(self):
        self.base_change_window()

    # 输入游记名称
    def input_travel_name(self, name):
        self.base_click(page.publish_click_travel_name_before)
        self.base_input(page.publish_click_travel_name, name)

    # 输入游记开头
    def input_traval_title(self, title):
        self.base_click(page.publish_click_travel_title)
        self.base_input(page.publish_click_travel_title, title)

    # 输入游记内容
    def input_content(self, content):
        self.base_click(page.publish_click_travel_place)
        self.base_input(page.publish_click_travel_place, content)

    # 点击发表游记
    def click_publish(self):
        self.base_click(page.publish_click_publish)

    # 点击发表之后 错误信息
    def publish_get_error_info(self):
        return self.base_get_text(page.publish_error_info)

    # 发表成功
    def publish_success(self):
        return self.base_if_exist(page.publish_success)

    def publish(self, name, title, content):
        with allure.step('进入攻略页面-点击发表游记并切换句柄'):
            self.click_strategy()
            self.click_publish_travel_notes()
            self.publish_change_window()
        with allure.step('点击新建游记'):
            self.click_new_travel_notes()
        self.driver.refresh()
        with allure.step('输入标题-简介-内容'):
            self.input_travel_name(name)
            self.input_traval_title(title)
            self.input_content(content)
            self.click_publish()
