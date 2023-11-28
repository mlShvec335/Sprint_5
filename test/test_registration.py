from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
import data
from locators import TestLocators


class TestRegistration:
    def test_registration_correct(self, driver):
        driver.get(data.reg_url)
        driver.find_element(*TestLocators.NANE_INPUT).send_keys(data.name)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(data.random_email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(data.password)
        driver.find_element(*TestLocators.REGISTRATION_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_contains("/login"))
        assert driver.current_url == data.login_url

    def test_registration_short_pass(self, driver):
        driver.get(data.reg_url)
        driver.find_element(*TestLocators.NANE_INPUT).send_keys(data.name)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(data.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(data.invalid_password)
        driver.find_element(*TestLocators.REGISTRATION_BTN).click()
        assert driver.find_element(*TestLocators.PASSWORD_ERROR).text == 'Некорректный пароль'
