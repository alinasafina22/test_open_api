from pages.main_page import MainPage
import pytest
import requests
from utils.json_fixtures import JsonFixtures


@pytest.mark.ui
def test_get_single_user(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    status_ui, body_ui = main_page.get_single_user()
    body_ui = "".join(body_ui.split())
    response = requests.get('https://reqres.in/api/users/2')
    status_api = str(response.status_code)
    body_api = "".join(response.text.split())
    assert status_ui == status_api
    assert body_ui == body_api


@pytest.mark.ui
def test_get_user_negative(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    status_ui, body_ui = main_page.get_user_not_found()
    body_ui = "".join(body_ui.split())
    response = requests.get('https://reqres.in/api/users/23')
    status_api = str(response.status_code)
    body_api = "".join(response.text.split())
    assert status_ui == status_api
    assert body_ui == body_api


@pytest.mark.ui
@pytest.mark.parametrize("function, input_data", [('main_page.register_successful()', 'json_fixture.register_data'),
                                                  ('main_page.register_unsuccessful()', 'json_fixture.negative_data')])
def test_register_positive(browser, function, input_data):
    main_page = MainPage(browser)
    main_page.go_to_site()
    json_fixture = JsonFixtures()
    status_ui, body_ui = eval(function)
    body_ui = "".join(body_ui.split())
    response = requests.post('https://reqres.in/api/register', eval(input_data))
    status_api = str(response.status_code)
    body_api = "".join(response.text.split())
    assert status_ui == status_api
    assert body_ui == body_api


@pytest.mark.ui
def test_update_information(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    json_fixture = JsonFixtures()
    status_ui, body_ui = main_page.update_client()
    body_ui = "".join(body_ui.split())[:29]
    response = requests.put('https://reqres.in/api/users/2', json_fixture.user)
    status_api = str(response.status_code)
    body_api = "".join(response.text.split())[:29]
    assert status_ui == status_api
    assert body_ui == body_api
