from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest


class TestRegistration(unittest.TestCase):
    def test_first_registration(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
        first_name.send_keys('Some')
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        last_name.send_keys('Person')
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")
        email.send_keys('some_email@mail.ru')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(5)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')
        browser.quit()

    def test_second_registration(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
        first_name.send_keys('Some')
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
        last_name.send_keys('Person')
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")
        email.send_keys('some_email@mail.ru')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(5)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')
        browser.quit()


if __name__ == '__main__':
    unittest.main()
