from pages.base_page import BasePage
import allure
from data import Urls
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    @allure.step('Открытие страницы "Вход"')
    def open_login_page(self):
        self.open_url(f'{Urls.MAIN_PAGE}{Urls.LOGIN}')

    @allure.step('Нажатие кнопки"Восстановить пароль"')
    def click_recovery_password(self):
        recovery_password_button = self.find_element_visibility(LoginLocators.BUTTON_RECOVERY_PASSWORD)
        self.driver.execute_script('arguments[0].click();', recovery_password_button)
