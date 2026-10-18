from selenium.webdriver.common.by import By


class MainPageLocators:
     # Логотипы в шапке
     LOGO_YANDEX = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
     LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")

     # Кнопки "Заказать"
     ORDER_BUTTON_TOP = (By.XPATH, "(//button[normalize-space()='Заказать'])[1]")
     ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[normalize-space()='Заказать'])[2]")

     # Вопросы о важном
     QUESTION_BUTTONS = (By.CSS_SELECTOR, ".accordion__button")

     # Все панели с ответами
     ANSWER_PANELS = (By.CSS_SELECTOR, ".accordion__panel")

     # Список кнопок для удобного выбора по индексу (0 или 1)
     ORDER_BUTTONS = [ORDER_BUTTON_TOP, ORDER_BUTTON_BOTTOM]
     