import pytest
import allure
from utils.data_reader import get_data_from_json
from utils.assert_with_screenshot import assert_with_screenshot


@allure.story('publish')
@allure.title('发布游记功能测试')
@allure.description('发布游记功能测试，包括成功，信息填写不完整，未勾选协议类型')
@pytest.mark.publish
@pytest.mark.parametrize("data", get_data_from_json('data/publish_travel_notes.json'))
def test_publish(get_login_page, get_publish_page, data):
    with allure.step('初始化驱动器、页面对象'):
        login = get_login_page
        publish = get_publish_page
        driver = login.driver
    with allure.step('接收数据'):
        username = data.get('username')
        password = data.get('password')
        name = data.get('name')
        title = data.get('title')
        content = data.get('content')
        success = data.get('success')
        expect_result = data.get('expect_result')
    with allure.step('进入登录流程'):
        login.login(username, password, agree_protocol=True)
    with allure.step('进入发布游记流程'):
        publish.publish(name, title, content)
    # 如果购票成功，判断购票成功
    if success:
        assert_with_screenshot('true', driver, publish.publish_success, None)
    else:
        msg = publish.publish_get_error_info()
        assert_with_screenshot('equal', driver, msg, expect_result)