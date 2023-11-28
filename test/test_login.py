from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
import data
from locators import TestLocators


class TestLogin:
    def test_login_main(self, driver):
        driver.get(data.main_url)
        driver.find_element(*TestLocators.LOGIN_IN_ACC_BTN).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(data.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.main_url))
        assert driver.current_url == data.main_url

    def test_login_account(self, driver):
        driver.get(data.main_url)
        driver.find_element(*TestLocators.ACCOUNT_BTN).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(data.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.main_url))
        assert driver.current_url == data.main_url

    def test_login_registration(self, driver):
        driver.get(data.reg_url)
        driver.find_element(*TestLocators.LOGIN_LINK_BTN).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(data.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.main_url))
        assert driver.current_url == data.main_url

    def test_login_forgot_pass(self, driver):
        driver.get(data.forgot_pass_url)
        driver.find_element(*TestLocators.LOGIN_LINK_BTN).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(data.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.main_url))
        assert driver.current_url == data.main_url
