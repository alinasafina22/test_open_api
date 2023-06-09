import requests
import pytest
from utils.json_fixtures import JsonFixtures


@pytest.mark.api
class TestApi(object):

    # тест для get запроса single user/not found

    @pytest.mark.parametrize("api_request, expected_status, expected_body",
                             [('/api/users/2', 200, JsonFixtures.get_user_expected_body),
                              ('/api/users/23', 404, {})])
    def test_get_user(self, api_request, expected_status, expected_body):
        get_list_users = requests.get(f'https://reqres.in{api_request}')
        status = get_list_users.status_code
        body = get_list_users.json()
        assert status == expected_status, f"Фактический статус {status}, ожидаемый статус {expected_status}"
        assert body == expected_body

    # тест register - successful

    @pytest.mark.parametrize("person,status_expected, body_expected", [
        (
                JsonFixtures.register_data,
                200,
                JsonFixtures.expected_register

        ),
        (
                JsonFixtures.negative_data,
                400,
                JsonFixtures.expected_negative
        )
    ])
    def test_register_user(self, person, status_expected, body_expected):
        post_register = requests.post('https://reqres.in/api/register', person)
        status = post_register.status_code
        body = post_register.json()
        assert status == status_expected, f"Фактический статус {status}, ожидаемый статус {status_expected}"
        assert body == body_expected

    def test_update_user(self):
        user = JsonFixtures.user
        update_user = requests.put('https://reqres.in/api/users/2', user)
        status = update_user.status_code
        name_user = update_user.json()["name"]
        job_user = update_user.json()["job"]
        assert status == 200, f"Фактический статус {status}, ожидаемый статус 200"
        assert name_user == user["name"]
        assert job_user == user["job"]
