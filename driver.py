from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FormFiller:
    def __init__(self, form_url):
        self.driver = webdriver.Chrome()
        self.driver.get(form_url)
        self.index = 0

    def fill_form(self, add_list, price_list, link_list):
        while True:
            try:

                time.sleep(1)

                address_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]'
                                                                   '/div/div/div[2]/div/div[1]/div[2]/textarea')
                address_field.send_keys(add_list[self.index])

                time.sleep(1)

                price_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div'
                                                                 '/div/div[2]/div/div[1]/div/div[1]/input')
                price_field.send_keys(price_list[self.index])

                time.sleep(1)

                link_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div'
                                                                '/div/div[2]/div/div[1]/div/div[1]/input')
                link_field.send_keys(link_list[self.index])

                time.sleep(1)

                submit = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]'
                                                            '/div/span/span')
                submit.click()

                time.sleep(2)

                submit_another = self.driver.find_element(By.CSS_SELECTOR, '.c2gzEf a')
                submit_another.click()

                self.index += 1

            except IndexError:
                print("Done!")
                break
