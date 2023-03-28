from pages.main_page import MainPage
import pytest
import requests
from utils.json_fixtures import JsonFixtures


@pytest.mark.ui
def test_get_single_user(browser):
    cls = MainPage(browser)
    cls.go_to_site()
    status_ui, body_ui = cls.get_single_user()
    body_ui = "".join(body_ui.split())
    response = requests.get('https://reqres.in/api/users/2')
    status_api = str(response.status_code)
    body_api = "".join(response.text.split())
    assert status_ui == status_api
    assert body_ui == body_api


@pytest.mark.ui
def test_get_user_negative(browser):
    cls = MainPage(browser)
    cls.go_to_site()
    status_ui, body_ui = cls.get_user_not_found()
    body_ui = "".join(body_ui.split())
    response = requests.get('https://reqres.in/api/users/23')
    status_api = str(response.status_code)
    body_api = "".join(response.text.split())
    assert status_ui == status_api
    assert body_ui == body_api


@pytest.mark.ui
@pytest.mark.parametrize("function, input_data", [('cls.register_successful()', 'cls2.register_data'),
                                                  ('cls.register_unsuccessful()', 'cls2.negative_data')])
def test_register_positive(browser, function, input_data):
    cls = MainPage(browser)
    cls.go_to_site()
    cls2 = JsonFixtures()
    status_ui, body_ui = eval(function)
    body_ui = "".join(body_ui.split())
    response = requests.post('https://reqres.in/api/register', eval(input_data))
    status_api = str(response.status_code)
    body_api = "".join(response.text.split())
    assert status_ui == status_api
    assert body_ui == body_api



