import requests
import allure
from faker import Faker
from random import randint


fake = Faker()

phone = (str(randint(0, 9)) + "(" + str(randint(100, 999)) + ")" + str(randint(100, 999)) + "-" + str(randint(10, 99)) + "-" + str(randint(10, 99)))


@allure.description("API Проверка возможности регистрации в систему под пользователем Mike")
@allure.testcase("https://shop.synctoskill.com", "STS2321")
@allure.title("API Проверка возможности регистрации в систему")
@allure.severity(severity_level="BLOCKER")
def test_api_reg():

    temp_email = fake.ascii_company_email()
    password = fake.password()
    name = fake.first_name()
    address = fake.address()
    date = fake.date()

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    body = {
        "password": password,
        "passwordConfirmation": password,
        "email": temp_email,
        "fullName": name,
        "imageUrl": "",
        "birthDate": date,
        "address": address,
        "phone": phone
    }

    response = requests.post("https://shop.synctoskill.com/api/AccountApi/register", headers=header, json=body)
    print(response.json())
    print(temp_email)
    print(password)
    print(name)
    print(address)
    print(date)
    print(phone)
    assert response.status_code == 200
