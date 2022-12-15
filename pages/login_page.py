from .base_page import BasePage
from .locators import LoginPageLocoators
from selenium.webdriver.common.by import By
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "it's not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocoators.Login_Form), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocoators.Registration_Form), "Registration form is not presented"

    def register_new_user(self, email, password):
        register = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        register.click()
        registration_email = self.browser.find_element(By.CSS_SELECTOR,"[name= 'registration-email']")
        registration_email.send_keys(email)
        registration_password = self.browser.find_element(By.CSS_SELECTOR,"[name= 'registration-password1']")
        registration_password.send_keys(password)
        registration_password_repeat = self.browser.find_element(By.CSS_SELECTOR, "[name= 'registration-password2']")
        registration_password_repeat.send_keys(password)
        registration_button = self.browser.find_element(By.CSS_SELECTOR, "[name= 'registration_submit']")
        registration_button.click()