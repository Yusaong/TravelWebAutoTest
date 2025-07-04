import pytest
import page
from selenium import webdriver
from page.page_order import OrderPage
from page.page_tickets import TicketPage
from page.page_login import PageLogin
from page.page_publish_travel_notes import PagePublish


@pytest.fixture(scope='function')
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(page.url)
    yield driver
    # 2. 关闭浏览器
    driver.quit()


@pytest.fixture(scope='function')
def get_login_page(get_driver):
    return PageLogin(get_driver)

@pytest.fixture(scope='function')
def get_ticket_page(get_driver):
    return TicketPage(get_driver)

@pytest.fixture(scope='function')
def get_order_page(get_driver):
    return OrderPage(get_driver)

@pytest.fixture(scope='function')
def get_publish_page(get_driver):
    return PagePublish(get_driver)

