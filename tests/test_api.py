import requests
import pytest
from utils.json_fixtures import JsonFixtures


class TestApi(object):
    cls = JsonFixtures()

    # тест для get запроса single user/not found
    @pytest.mark.parametrize("api_request, expected_status, expected_body",
                             [('/api/users/2', 200, cls.get_user_expected_body),
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
                {"email": "eve.holt@reqres.in", "password": "pistol"},
                200,
                '{"id":4,"token":"QpwL5tke4Pnpja7X4"}'
        ),
        (
                {"email": "sydney@fife"},
                400,
                '{"error":"Missing password"}'
        )
    ])
    def test_register_user(self, person, status_expected, body_expected):
        post_register = requests.post('https://reqres.in/api/register', person)
        status = post_register.status_code
        body = post_register.text
        assert status == status_expected, f"Фактический статус {status}, ожидаемый статус {status_expected}"
        assert body == body_expected
        return status, body

    def test_update_user(self):
        user = self.cls.user
        update_user = requests.put('https://reqres.in/api/users/2', user)
        status = update_user.status_code
        name_user = update_user.json()["name"]
        job_user = update_user.json()["job"]
        assert status == 200, f"Фактический статус {status}, ожидаемый статус 200"
        assert name_user == user["name"]
        assert job_user == user["job"]
