import allure
import pytest

from utils.data_reader import get_data_from_json
from utils.assert_with_screenshot import assert_with_screenshot

@allure.story('login')
@allure.title('登录功能测试')
@allure.description('登录功能测试，包括成功，账号密码错误，未勾选协议，未填写账号密码类型')
@pytest.mark.parametrize("data", get_data_from_json("data/login.json"))
@pytest.mark.login
def test_login(get_login_page, data):
    with allure.step('初始化驱动器、页面对象'):
        login = get_login_page
        driver = login.driver
    with allure.step('接收数据'):
        username = data.get('username')
        password = data.get('password')
        protocol = data.get('protocol')
        success = data.get('success')
        error_type = data.get('error_type')
        expect_result = data.get('expect_result')
    #  账号、密码不为空并且点击了协议
    with allure.step('进入登录流程'):
        login.login(username, password, protocol)

    if success:
        assert_with_screenshot('true', driver, login.is_login_success(), None)
    else:
        msg = login.get_error_info(error_type)
        assert_with_screenshot('equal', driver, msg, expect_result)