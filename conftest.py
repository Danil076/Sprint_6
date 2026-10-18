import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage

@pytest.fixture(scope="function")
def driver():
    with allure.step("Инициализация браузера Firefox"):
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options = options)

    yield driver

    with allure.step("Закрытие браузера"):
        driver.quit()

@pytest.fixture
def main_page(driver):
    # Фикстура для создания объекта главной страницы и открытия её
    with allure.step("Открытие главной страницы Самоката"):
        page = MainPage(driver)
        page.open_main()
        # Закрываем куки
        page.accept_cookies()
    return page
