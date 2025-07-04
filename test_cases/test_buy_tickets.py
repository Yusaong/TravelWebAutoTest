import pytest
import allure

from utils.data_reader import get_data_from_json
from utils.assert_with_screenshot import assert_with_screenshot

@allure.story('purchase')
@allure.title('购票功能测试')
@allure.description('购票功能测试，包括成功，信息填写不完整，未勾选协议类型')
@pytest.mark.parametrize("data", get_data_from_json("data/buy_tickets.json"))
@pytest.mark.purchase
def test_buy_tickets(get_login_page, get_purchase_page, data):
    with allure.step('初始化驱动器、页面对象'):
        login = get_login_page
        purchase = get_purchase_page
        driver = login.driver
    with allure.step('接收数据'):
        username = data.get('username')
        password = data.get('password')
        start_station = data.get('start_station')
        arrive_station = data.get('arrive_station')
        time = data.get('time')
        name = data.get('name')
        id = data.get('id')
        phone = data.get('phone')
        protocol = data.get('protocol')
        success = data.get('success')
        expect_result = data.get('expect_result')
    with allure.step('进入登录流程'):
        login.login(username, password, agree_protocol=True)
    with allure.step('进入购票流程'):
        purchase.buy_tickets(start_station, arrive_station, time, name, id, phone, protocol)
    # 如果购票成功，判断购票成功
    if success:
        assert_with_screenshot('true', driver, purchase.submit_access, None)
    else:
        msg = purchase.buy_get_error_info()
        assert_with_screenshot('equal', driver, msg, expect_result)
