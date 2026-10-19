import pytest
import allure
from pages.main_page import MainPage


@allure.feature("Главная страница")
@allure.story("Навигация по логотипам")
class TestHeaderNavigation:

    @allure.title("Клик по логотипу Яндекса открывает новую вкладку с Дзеном")
    def test_yandex_logo_open__new_tab(self, main_page: MainPage):

        with allure.step("Кликнуть по логотипу Яндекса"):

            main_page.click_yandex_logo()

        with allure.step("Переключиться на новую вкладку"):
            main_page.switch_to_last_window()

        with allure.step("Дождаться загрузки страницы Дзена"):    
            main_page.wait_for_url_to_contain("dzen")

        with allure.step("Проверить, что открылась страница Дзена"):
            current_url = main_page.get_current_url()
            assert "dzen" in current_url or "yandex" in current_url, (
                f"Ожидался переход на Дзен или Яндекс, а открылся URL: {current_url}"
            )

    @allure.title("Клик по логотипу Самоката ведёт на главную страницу сервиса")
    def test_scooter_logo_redirect(self, main_page: MainPage):
        
        expected_url = "https://qa-scooter.praktikum-services.ru/"

        # Переходим на страницу заказа
        with allure.step("Перейти на страницу заказа"):
            main_page.click_order_button(0)

        # Кликаем по логотипу Самоката в шапке
        with allure.step("Кликнуть по логотипу Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Дождаться перехода на главную страницу"):
            main_page.wait_for_url_to_be(expected_url)

        # Проверяем, что мы находимся на странице заказа
        with allure.step("Проверить, что мы остались на странице заказа"):
            current_url = main_page.get_current_url()
            assert current_url == expected_url, (
                f"Ожидался URL: {expected_url}, но открылся: {current_url}"
            )
            