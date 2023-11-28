import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
import data
from locators import TestLocators


class TestConstructorSection:

    def test_buns_section(self, driver):
        driver.get(data.main_url)
        driver.find_element(*TestLocators.SAUCE_BTN).click()  # клик по другому разделу, т.к. "Булки" активны изначально
        driver.find_element(*TestLocators.BUNS_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUNS_SECTION))
        current_section = driver.find_element(*TestLocators.BUNS_CURRENT).get_attribute('class')
        assert 'current' in current_section

    def test_sauce_section(self, driver):
        driver.get(data.main_url)
        driver.find_element(*TestLocators.SAUCE_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SAUCE_SECTION))
        current_section = driver.find_element(*TestLocators.SAUCE_CURRENT).get_attribute('class')
        assert 'current' in current_section

    def test_topping_section(self, driver):
        driver.get(data.main_url)
        driver.find_element(*TestLocators.TOPPING_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TOPPING_SECTION))
        current_section = driver.find_element(*TestLocators.TOPPING_CURRENT).get_attribute('class')
        assert 'current' in current_section
