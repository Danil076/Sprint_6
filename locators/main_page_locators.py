from selenium.webdriver.common.by import By


class MainPageLocators:
     # Логотипы в шапке
     LOGO_YANDEX = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
     LOGO_SCOOTER = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")

     # Кнопки "Заказать"
     ORDER_BUTTONS = (By.XPATH, "//button[normalize-space()='Заказать']")

     # Вопросы о важном
     QUESTION_BUTTONS = (By.CSS_SELECTOR, ".accordion__button")

     # Все панели с ответами
     ANSWER_PANELS = (By.CSS_SELECTOR, ".accordion__panel")
     