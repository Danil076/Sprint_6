from selenium.webdriver.common.by import By


class OrderFormLocators:

   # Экран 1: Для кого самокат
   FOR_WHOM_HEADER = (By.XPATH, "//div[contains(text(), 'Для кого самокат')]")

   # Поля ввода
   NAME = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
   SURNAME = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
   ADDRESS = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
   PHONE = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')

   # Станция метро
   METRO = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
   METRO_DROPDOWN_ITEM = (By.CSS_SELECTOR, '.Order_SelectOption__82bhS')

   # Кнопка "Далее"
   NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Далее']")

   # Экран 2: Про аренду
   RENTAL_HEADER = (By.XPATH, "//div[contains(text(), 'Про аренду')]")

   # Дата доставки
   DATE = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')

   # Срок аренды самоката
   RENTAL_DURATION_PLACEHOLDER = (By.CSS_SELECTOR, '.Dropdown-placeholder')
   RENTAL_DURATION_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and contains(text(), 'сутки')]")

   # Цвет самоката
   COLOR_BLACK_CHECKBOX = (By.ID, "black")

   # Комментарий для курьера
   COMMENT = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')

   ORDER_BUTTON_FINAL = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and normalize-space()='Заказать']")

   # Модальное окно подтверждения
   CONFIRM_MODAL_HEADER = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]")
   CONFIRM_BUTTON_YES = (By.XPATH, "//button[normalize-space()='Да']")
