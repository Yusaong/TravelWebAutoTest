import allure
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

class Base:
    # 初始化函数
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    # 一段时间内持续查找元素
    def base_find_element(self, loc, timeout=10, poll=0.5):
        '''
        :param loc: 元组，元素定位方式和定位值
        :param timeout: 隐式等待的时间,默認參數為30
        :param poll: 轮询的时间间隔
        :return: 找到的元素对象
        '''
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))


    def base_click(self, loc):
        with allure.step(f'点击元素 {loc}'):
            try:
                self.base_find_element(loc).click()
            except Exception as e:
                allure.attach(self.driver.get_screenshot_as_png(), name="点击失败截图",
                              attachment_type=allure.attachment_type.PNG)
                raise e

    # 切换窗口
    def base_change_window(self):
        """
        关闭所有非最新窗口，只保留并切换到最新打开的窗口
        """
        handles = self.driver.window_handles
        latest_handle = handles[-1]
        for handle in handles[:-1]:
            self.driver.switch_to.window(handle)
            self.driver.close()
        self.driver.switch_to.window(latest_handle)

    def base_input(self, loc, value, clear_first=True):
        el = self.base_find_element(loc)
        if clear_first:
            el.clear()
        el.send_keys(value)

    def base_get_text(self, loc):
        with allure.step('寻找元素{loc}'):
            element = self.base_find_element(loc).text
        return element


    # 拖动滑块方法
    def base_move(self, loca, locb):
        loc1 = self.base_find_element(loca)
        loc2 = self.base_find_element(locb)
        with allure.step(f'滑动滑块-{loc1}到滑动框-{loc2}右边'):
            try:
                self.action.drag_and_drop_by_offset(loc1, loc2.size['width'], -loc2.size['height'])
                self.action.move_by_offset(10, 10)
                self.action.perform()
            except Exception as e:
                allure.attach(self.driver.get_screenshot_as_png(), name="点击失败截图",
                              attachment_type=allure.attachment_type.PNG)
                raise e

    # 移动滑块后进行点击，触发页面事件，避免验证失败
    def base_move_to_empty_space(self):
        self.action.move_by_offset(0, 0)
        self.action.click()
        self.action.perform()
        time.sleep(1)

    # 封装判断元素是否存在
    def base_if_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=3)
            return True
        except:
            return False
