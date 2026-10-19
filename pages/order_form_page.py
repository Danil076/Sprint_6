from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from locators.order_form_locators import OrderFormLocators
from selenium.webdriver.support import expected_conditions as EC
import time
import allure


class OrderFormPage(BasePage):

    @allure.step("Проверить, что открыт экран 'Для кого самокат'")
    def is_for_whom_window_visible(self):

        # Проверяет, что на странице есть заголовок: "Для кого самокат"
        header = self.find_element(OrderFormLocators.FOR_WHOM_HEADER)
        return header.is_displayed()

    @allure.step("Заполнить экран 'Для кого самокат'")
    def fill_for_whom_window(self, name, surname, address, phone, metro_station):

        # Заполняет первое окно формы заказа
        self.find_element(OrderFormLocators.NAME).send_keys(name)
        self.find_element(OrderFormLocators.SURNAME).send_keys(surname)
        self.find_element(OrderFormLocators.ADDRESS).send_keys(address)
        self.find_element(OrderFormLocators.PHONE).send_keys(phone)

        # Метро: вводим название станции и выбираем вариант из выпадающего списка
        metro_input = self.find_element(OrderFormLocators.METRO)
        metro_input.clear()
        metro_input.send_keys(metro_station)

        metro_option = self.wait.until(
            EC.element_to_be_clickable(OrderFormLocators.METRO_DROPDOWN_ITEM)
        )
        metro_option.click()

        # Нажимаем на кнопку "Далее"
        self.click_element(OrderFormLocators.NEXT_BUTTON)

    @allure.step("Проверить, что открыт экран 'Про аренду'")
    def is_rental_window_visible(self):

        # Проверяет, что после нажатия "Далее" открылся экран "Про аренду"
        header = self.find_element(OrderFormLocators.RENTAL_HEADER)
        return header.is_displayed()

    @allure.step("Выбрать срок аренды: сутки")
    def select_rental_duration_day(self):

        # Открывает выпадающий список срока аренды и выбирает вариант "сутки"
        self.click_element(OrderFormLocators.RENTAL_DURATION_PLACEHOLDER)
        self.click_element(OrderFormLocators.RENTAL_DURATION_OPTION)

    @allure.step("Выбрать цвет самоката: чёрный жемчуг")
    def select_black_color(self):

        # Выбирает чекбокс чёрного цвета
        self.click_element_by_js(OrderFormLocators.COLOR_BLACK_CHECKBOX)

    @allure.step("Заполнить комментарий курьеру: {comment}")
    def fill_comment(self, comment):

        # Заполняет поле комментария для курьера
        self.find_element(OrderFormLocators.COMMENT).send_keys(comment) 

    @allure.step("Заполнить экран 'Про аренду' и нажать 'Заказать'")
    def fill_rental_window_and_submit(self, date, comment):

        # Заполняет экран 'Про аренду': дата, срок аренды, цвет, комментарий  и нажимает "Заказать"
        date_input = self.find_element(OrderFormLocators.DATE)
        date_input.clear()
        date_input.send_keys(date)

        date_input.send_keys(Keys.ESCAPE)

        self.select_rental_duration_day()
        self.select_black_color()
        self.fill_comment(comment)

        self.click_element(OrderFormLocators.ORDER_BUTTON_FINAL)

    # Окно подтверждения заказа
    @allure.step("Проверить модальное окно 'Хотите оформить заказ?'")
    def is_confirm_modal_visible(self):

        modal_header = self.find_element(OrderFormLocators.CONFIRM_MODAL_HEADER)
        return modal_header.is_displayed()

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        
        self.click_element(MainPageLocators.LOGO_YANDEX)
