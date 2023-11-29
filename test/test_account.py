from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from data import Urls, LoginData
from locators import TestLocators


class TestAccountPage:
    def test_account_registered_profile(self, driver):
        driver.get(Urls.login_url)
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(LoginData.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(LoginData.password)
        driver.find_element(*TestLocators.LOGIN_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.ACCOUNT_BTN))
        driver.find_element(*TestLocators.ACCOUNT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(Urls.profile_url))
        assert driver.current_url == Urls.profile_url
