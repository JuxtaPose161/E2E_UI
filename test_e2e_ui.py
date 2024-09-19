import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

login = 'standard_user'
password = 'secret_sauce'

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)
    def check_login(self, browser):
        browser.find_element(By.ID, 'user-name').send_keys(login)
        browser.find_element(By.ID, 'password').send_keys(password)
        browser.find_element(By.ID, 'login-button').click()
    def select_product(self, browser):
        first_product = browser.find_element(By.CSS_SELECTOR, '.inventory_item')
        product_name = first_product.find_element(By.CLASS_NAME, 'inventory_item_name').text
        first_product.find_element(By.CSS_SELECTOR, 'button').click()
        browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        product_in_cart = browser.find_element(By.CLASS_NAME, 'inventory_item_name').text
        self.assertEqual(product_name, product_in_cart, 'products not equal')
        browser.find_element(By.ID, 'checkout').click()
    def finish_buying(self, browser):
        form = browser.find_elements(By.CSS_SELECTOR, 'input.form_input')
        form[0].send_keys('John')
        form[1].send_keys('John')
        form[2].send_keys('111111')
        browser.find_element(By.ID, 'continue').click()
        browser.find_element(By.ID, 'finish').click()

    def test_main_function(self):
        self.browser.get('https://www.saucedemo.com/')
        self.assertIn('Swag Labs', self.browser.title)
        browser = self.browser
        try:
            self.check_login(browser)
            sleep(1)
            print('User login')
        except Exception as e:
            self.fail(f'Auth Error with this logs: {e}')

        try:
            self.select_product(browser)
            sleep(1)
            print('User select product')
        except Exception as e:
            self.fail(f'Select Error with this logs: {e}')

        try:
            self.finish_buying(browser)
            sleep(1)
            print('User finish buying')
        except Exception as e:
            self.fail(f'Buying Error with this logs: {e}')

        print(browser.find_element(By.CLASS_NAME, 'complete-text').text)
        browser.find_element(By.ID, 'back-to-products').click()
        self.assertIn('Swag Labs', self.browser.title)

if __name__ == '__main__':
    unittest.main()