from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
        # Находим ВСЕ кнопки аккордеона сразу (получаем список)
        questions = self.wait.until(EC.presence_of_all_elements_located(MainPageLocators.QUESTION_BUTTONS))
        # Берем конкретную кнопку из списка по индексу
        question = questions[index]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        # Ждём, пока она станет кликабельной, и кликаем
        self.wait.until(EC.element_to_be_clickable(question)).click()

    @allure.step("Проверить, что ответ на вопрос с индексом {index} открыт")
    def is_answer_open(self, index):
        # Находим все панели с ответами (список из 8 элементов)
        answers = self.wait.until(EC.presence_of_all_elements_located(MainPageLocators.ANSWER_PANELS))
        # Берём конкретную панель по индексу
        answer = answers[index]
        hidden_attribute = answer.get_attribute("hidden")
        return hidden_attribute is None or hidden_attribute == "false"

    @allure.step("Получить текст ответа на вопрос с индексом {index}")
    def get_answer_text(self, index):
        answers = self.wait.until(EC.presence_of_all_elements_located(MainPageLocators.ANSWER_PANELS))
        answer = answers[index]
        return answer.find_element(By.TAG_NAME, "p").text

    @allure.step("Кликнуть по кнопке 'Заказать' (0 - верхняя, 1 - нижняя)")
    def click_order_button(self, button_index=0):
        # Создаем локаторы: (0 = верхняя, индекс 1 = нижняя)
        order_buttons = (
            MainPageLocators.ORDER_BUTTON_TOP,
            MainPageLocators.ORDER_BUTTON_BOTTOM
        )
        # Берём нужный локатор по индексу и кликаем
        self.click_element(order_buttons[button_index])

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Кликнуть по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)
        