import pytest
import allure
from pages.main_page import MainPage
from pages.order_form_page import OrderFormPage



# Тестовые данные для двух наборов
ORDER_DATA = [
    {
        "name": "Иван",
        "surname": "Иванов",
        "address": "Москва, ул. Пушкина, д. 1",
        "phone": "+79991112233",
        "metro": "Бульвар Рокоссовского",
        "date": "30.12.2026",
        "comment": "Спасибо за заказ!",
        "button_index": 0  # 0 = верхняя кнопка "Заказать"
    },
    {
        "name": "Сергей",
        "surname": "Сергеев",
        "address": "Москва, ул. Пушкина, д. 2",
        "phone": "+79994445566",
        "metro": "Бульвар Рокоссовского",
        "date": "31.12.2026",
        "comment": "Оставить у двери",
        "button_index": 1  # 1 = нижняя кнопка "Заказать"
    }
]

@allure.feature("Оформление заказа")
@allure.story("Успешное оформление заказа")
class TestOrderFlow:

    @pytest.mark.parametrize(
        "data",
        ORDER_DATA,
        ids=[
            "Иван_верхняя_кнопка_Заказать",
            "Сергей_нижняя_кнопка_Заказать"
        ]
    )
    # Оформление заказа
    def test_order_success_flow(self, main_page: MainPage, data):

        allure.dynamic.title(
            f"Оформление заказа: {data['name']} {data['surname']}"
        )

        order_form = OrderFormPage(main_page.driver)

        with allure.step(
            f"Кликнуть на кнопку 'Заказать' (индекс: {data['button_index']})"
        ):
            main_page.click_order_button(data["button_index"])

        with allure.step("Проверить, что открылся экран 'Для кого самокат'"):
            assert order_form.is_for_whom_window_visible(), (
                "Не открылся экран 'Для кого самокат'"
            )

        with allure.step("Заполнить экран 'Для кого самокат'"):
            order_form.fill_for_whom_window(
                name=data["name"],
                surname=data["surname"],
                address=data["address"],
                phone=data["phone"],
                metro_station=data["metro"]
            )

        with allure.step("Проверить, что открылся экран 'Про аренду'"):
            assert order_form.is_rental_window_visible(), (
                "Не открылся экран 'Про аренду'"
            )

        with allure.step("Заполнить экран 'Про аренду' и нажать 'Заказать'"):
            order_form.fill_rental_window_and_submit(
                date=data["date"],
                comment=data["comment"]
            )

        with allure.step("Проверить появление модального окна подтверждения"):
            assert order_form.is_confirm_modal_visible(), (
                "Модальное окно 'Хотите оформить заказ?' не появилось!"
            )
