import allure
from assertpy import assert_that

def assert_with_screenshot(assert_type, driver, actual, expect=None):
    """
    通用断言并自动截图工具
    支持多种断言类型，断言失败时自动截图并附加到Allure报告中。
    :param assert_type: str，断言类型，可选值：
        - 'true'  : 断言actual为True
        - 'equal' : 断言actual等于expect
        # 可根据需要扩展更多类型
    :param driver: selenium webdriver对象，用于截图
    :param actual: 实际值
    :param expect: 期望值（仅在'equal'等需要比较时传入）
    :raises AssertionError: 断言失败时抛出，并自动截图
    :raises ValueError: 不支持的断言类型时抛出
    """
    try:
        if assert_type == 'true':
            assert_that(actual).is_true()
        elif assert_type == 'equal':
            assert_that(actual).is_equal_to(expect)
        else:
            raise ValueError(f"不支持的断言类型: {assert_type}")
    except AssertionError as e:
        # 断言失败时截图并附加到Allure报告
        allure.attach(
            driver.get_screenshot_as_png(),
            name="失败截图",
            attachment_type=allure.attachment_type.PNG
        )
        raise e