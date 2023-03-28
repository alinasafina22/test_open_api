
class JsonFixtures:
    get_user_expected_body = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    user = {
        "name": "morpheus",
        "job": "zion resident"
    }
    register_data = {"email": "eve.holt@reqres.in", "password": "pistol"}
    negative_data = {"email": "sydney@fife"}
    expected_register = {'id': 4, 'token': 'QpwL5tke4Pnpja7X4'}
    expected_negative = {'error': 'Missing password'}
