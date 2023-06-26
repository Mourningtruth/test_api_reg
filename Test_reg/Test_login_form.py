import allure
from selenium import webdriver
from selenium.webdriver import Keys
from page_object.login_page import LoginPage


def test_setup():
    global driver
    driver = webdriver.Chrome()


@allure.description("Проверка возможности логина в систему под пользователем Mike")
@allure.testcase("https://shop.synctoskill.com", "STS2321")
@allure.title("Проверка возможности входа в систему")
@allure.severity(severity_level="BLOCKER")
def test_login():
    # driver.get("https://shop.synctoskill.com")
    LoginPage.start_page(driver)
    driver.maximize_window()
    driver.find_elements("xpath", LoginPage.login)[0].click()
    driver.find_element("xpath", LoginPage.email).send_keys("kqli@mail.com")
    driver.find_element("xpath", LoginPage.password).send_keys("Qwerty12345")
    driver.find_element("xpath", LoginPage.login_btn).click()
    user_name = driver.find_elements("xpath", LoginPage.profile_name)[0].get_attribute("text").find("Mike")
    assert(user_name != -1)


@allure.title("Проверка товаров в поисковой строке")
@allure.description("Поиск продукта Eggplant")
@allure.testcase("https://shop.synctoskill.com", "STS2321")
@allure.severity(severity_level="MAJOR")
def test_search():
    driver.get("https://shop.synctoskill.com")
    driver.find_element("xpath", "//input[@name='SearchQuery']").send_keys("Eggplant")
    driver.find_element("xpath", "//input[@name='SearchQuery']").send_keys(Keys.ENTER)
    search_result = driver.find_element("xpath", "//a[@class='btn btn-info']").get_attribute("text").find("Eggplant")
    assert (search_result != -1)
