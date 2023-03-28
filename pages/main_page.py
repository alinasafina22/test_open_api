import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class UiLocators:

    # selectors
    get_single_user_btn = (By.CSS_SELECTOR, '[data-id="users-single"]')
    get_single_not_found_btn = (By.CSS_SELECTOR, '[data-id="users-single-not-found"]')
    post_register_successful_btn = (By.CSS_SELECTOR, '[data-id="register-successful"]')
    post_register_unsuccessful_btn = (By.CSS_SELECTOR, '[data-id="register-unsuccessful"]')
    put_update_btn = (By.CSS_SELECTOR, '[data-id="put"]')

    # результаты
    response_code_txt = (By.CSS_SELECTOR, 'span.response-code')
    response_body_txt = (By.CSS_SELECTOR, '[data-key="output-response"]')


class MainPage(BasePage):

    def get_single_user(self):
        get_click_btn = self.find_element(UiLocators.get_single_user_btn)
        get_click_btn.click()
        sleep(1)
        status_code = self.find_element(UiLocators.response_code_txt)
        status = status_code.text
        body_txt = self.find_element(UiLocators.response_body_txt)
        body = body_txt.text
        ' '.join(body.split())
        return status, body

    def get_user_not_found(self):
        get_btn = self.find_element(UiLocators.get_single_not_found_btn)
        get_btn.click()
        sleep(2)
        status_code = self.find_element(UiLocators.response_code_txt)
        status = status_code.text
        body_txt = self.find_element(UiLocators.response_body_txt)
        body = body_txt.text
        ' '.join(body.split())
        return status, body

    def register_successful(self):
        post_btn = self.find_element(UiLocators.post_register_successful_btn)
        post_btn.click()
        sleep(1)
        status_code = self.find_element(UiLocators.response_code_txt)
        status = status_code.text
        body_txt = self.find_element(UiLocators.response_body_txt)
        body = body_txt.text
        ' '.join(body.split())
        return status, body

    def register_unsuccessful(self):
        post_btn = self.find_element(UiLocators.post_register_unsuccessful_btn)
        post_btn.click()
        sleep(1)
        status_code = self.find_element(UiLocators.response_code_txt)
        status = status_code.text
        body_txt = self.find_element(UiLocators.response_body_txt)
        body = body_txt.text
        ' '.join(body.split())
        return status, body
