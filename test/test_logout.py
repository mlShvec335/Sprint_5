from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
import data
from locators import TestLocators


class TestLogout:
    def test_logout(self, driver):
        driver.get(data.login_url)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(data.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.ACCOUNT_BTN))
        driver.find_element(*TestLocators.ACCOUNT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.LOGOUT_BTN))
        driver.find_element(*TestLocators.LOGOUT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.login_url))
        assert driver.current_url == data.login_url
