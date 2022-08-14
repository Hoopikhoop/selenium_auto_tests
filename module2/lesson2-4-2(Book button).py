import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def main():
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    try:
        button = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '$100')
        )
        browser.find_element(By.CSS_SELECTOR, 'button#book').click()
        x = browser.find_element(By.CSS_SELECTOR, 'label .nowrap:nth-of-type(2)').text
        y = calc(x)
        browser.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys(y)

        submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit.click()

    finally:
        time.sleep(10)
        browser.quit()


main()
