import requests
import allure


@allure.description("API Проверка возможности логина в систему под пользователем Mike")
@allure.testcase("https://shop.synctoskill.com", "STS2321")
@allure.title("API Проверка возможности входа в систему")
@allure.severity(severity_level="BLOCKER")
def test_api_login():
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    body = {
        "email": "kqli@mail.com",
        "password": "Qwerty12345"
    }

    response = requests.post("https://shop.synctoskill.com/api/AccountApi/login", headers=header, json=body)
    assert response.status_code == 200
