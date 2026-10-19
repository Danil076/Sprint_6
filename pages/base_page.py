from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Принять куки")
    def accept_cookies(self):
        # Закрывает баннер с куками, если он появился
        cookie_buttons = self.driver.find_elements(By.ID, "rcc-confirm-button")
        for button in cookie_buttons:
            button.click()

    @allure.step("Найти элемент и дождаться его видимости: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти все элементы и дождаться их появления в DOM: {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
   
    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.wait.until(EC.element_to_be_clickable(element)).click()

    @allure.step("Кликнуть на элемент по индексу из списка: {locator}, индекс: {index}")
    def click_element_by_index(self, locator, index):
        elements = self.find_elements(locator)
        element = elements[index]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable(element)).click()

    @allure.step("Кликнуть по элементу через JavaScript: {locator}")
    def click_element_by_js(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text.strip()

    @allure.step("Переключиться на последнюю открытую вкладку браузера")
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Дождаться, что URL содержит текст: {text}")
    def wait_for_url_to_contain(self, text):
        self.wait.until(EC.url_contains(text))

    @allure.step("Дождаться, что URL равен: {url}")
    def wait_for_url_to_be(self, url):
        self.wait.until(EC.url_to_be(url))
