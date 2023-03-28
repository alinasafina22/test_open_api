from page import TestUI
import pytest
import requests


def test_get_single_user(browser):
    cls = TestUI(browser)
    cls.go_to_site()
    status_ui, body_ui = cls.get_single_user()
    body_ui = "".join(body_ui.split())
    response = requests.get('https://reqres.in/api/users/2')
    status_api = str(response.status_code)
    body_api = "".join(response.text.split())
    assert status_ui == status_api
    assert body_ui == body_api


def test_get_user_negative(browser):
    cls = TestUI(browser)
    cls.go_to_site()
    status_ui, body_ui = cls.get_user_not_found()
    body_ui = "".join(body_ui.split())
    response = requests.get('https://reqres.in/api/users/23')
    status_api = str(response.status_code)
    body_api = "".join(response.text.split())
    assert status_ui == status_api
    assert body_ui == body_api
