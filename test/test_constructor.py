from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from data import Urls, LoginData
from locators import TestLocators


class TestConstructorPage:
    def test_constructor_btn(self, driver):
        driver.get(Urls.login_url)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(LoginData.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(LoginData.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.ACCOUNT_BTN))
        driver.find_element(*TestLocators.ACCOUNT_BTN).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Urls.main_url))
        assert driver.current_url == Urls.main_url
        assert driver.find_element(*TestLocators.CONSTRUCTOR_TITLE).text == 'Соберите бургер'

    def test_logo_btn(self, driver):
        driver.get(Urls.login_url)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(LoginData.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(LoginData.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.ACCOUNT_BTN))
        driver.find_element(*TestLocators.ACCOUNT_BTN).click()
        driver.find_element(*TestLocators.LOGO_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Urls.main_url))
        assert driver.current_url == Urls.main_url
        assert driver.find_element(*TestLocators.CONSTRUCTOR_TITLE).text == 'Соберите бургер'
