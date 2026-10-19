from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    # Ссылка на главную страницу
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("Открыть главную страницу Самоката")
    def open_main(self):

        self.open(self.BASE_URL)
        # Ждём появления логотипа как признака того, что страница загрузилась
        self.find_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть по вопросу с индексом {index}")
    def click_question(self,index):

        self.click_element_by_index(MainPageLocators.QUESTION_BUTTONS, index)

    @allure.step("Проверить, что ответ на вопрос с индексом {index} открыт")
    def is_answer_open(self, index):

        # Находим все панели с ответами (список из 8 элементов)
        answers = self.find_elements(MainPageLocators.ANSWER_PANELS)
        # Берём конкретную панель по индексу
        answer = answers[index]
        hidden_attribute = answer.get_attribute("hidden")
        return hidden_attribute is None or hidden_attribute == "false"

    @allure.step("Получить текст ответа на вопрос с индексом {index}")
    def get_answer_text(self, index):

        answers = self.find_elements(MainPageLocators.ANSWER_PANELS)
        answer = answers[index]
        return answer.find_element(By.TAG_NAME, "p").text

    @allure.step("Кликнуть по кнопке 'Заказать' (0 - верхняя, 1 - нижняя)")
    def click_order_button(self, button_index=0):

        # Создаем локаторы: (0 = верхняя, индекс 1 = нижняя)
        self.click_element_by_index(MainPageLocators.ORDER_BUTTONS, button_index)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Кликнуть по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)
        