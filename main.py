import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_title(browser):
    browser.get("https://courses.uet.vnu.edu.vn/")
    expected_title = "Website môn học"
    actual_title = browser.title
    assert expected_title in actual_title


def test_redirect(browser):
    browser.get("https://courses.uet.vnu.edu.vn/")

    # Replace find_element_by_xpath with find_element and use XPath to find element by text
    courses_link = browser.find_element(By.XPATH, "//a[text()='Courses']")
    courses_link.click()
    expected_url = "https://courses.uet.vnu.edu.vn/?redirect=0"
    assert browser.current_url == expected_url


def test_login_form(browser):
    browser.get("https://courses.uet.vnu.edu.vn/loginform/index.php")  # Replace with the actual URL

    username_input = browser.find_element(By.ID, "first-name")
    password_input = browser.find_element(By.NAME, "password")

    login_button = browser.find_element(By.CLASS_NAME, "login100-form-btn")

    username_input.send_keys("21020071")
    password_input.send_keys("hieulc123456zo")

    # Submit the form
    login_button.click()

    # Validate the result (you may need to adjust this based on the actual behavior after login)
    assert "https://courses.uet.vnu.edu.vn/login/index.php" not in browser.current_url

    span_name = browser.find_element(By.CLASS_NAME, "usertext mr-1")
    span_name_text = span_name.text

    assert "Huy Hiệu Nguyễn" in span_name_text


