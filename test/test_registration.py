from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from data import Urls, LoginData
from locators import TestLocators


class TestRegistration:
    def test_registration_correct(self, driver):
        driver.get(Urls.reg_url)
        driver.find_element(*TestLocators.NANE_INPUT).send_keys(LoginData.name)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(LoginData.random_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(LoginData.password)
        driver.find_element(*TestLocators.REGISTRATION_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_contains("/login"))
        assert driver.current_url == Urls.login_url

    def test_registration_short_pass(self, driver):
        driver.get(Urls.reg_url)
        driver.find_element(*TestLocators.NANE_INPUT).send_keys(LoginData.name)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(LoginData.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(LoginData.invalid_password)
        driver.find_element(*TestLocators.REGISTRATION_BTN).click()
        assert driver.find_element(*TestLocators.PASSWORD_ERROR).text == 'Некорректный пароль'
