import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

course_username = "21020071"
course_password = "hieulc123456zo"
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()


def test_title(browser):
    browser.get("https://courses.uet.vnu.edu.vn/")
    expected_title = "Website môn học"
    actual_title = browser.title
    assert expected_title in actual_title


def test_redirect(browser):
    browser.get("https://courses.uet.vnu.edu.vn/")

    courses_link = browser.find_element(By.XPATH, "//a[text()='Courses']")
    courses_link.click()
    expected_url = "https://courses.uet.vnu.edu.vn/?redirect=0"
    assert browser.current_url == expected_url


def test_login_form(browser):
    browser.get("https://courses.uet.vnu.edu.vn/loginform/index.php")  # Replace with the actual URL

    username_input = browser.find_element(By.ID, "first-name")
    password_input = browser.find_element(By.NAME, "password")

    login_button = browser.find_element(By.CLASS_NAME, "login100-form-btn")

    username_input.send_keys(course_username)
    password_input.send_keys(course_password)

    login_button.click()

    assert "https://courses.uet.vnu.edu.vn/login/index.php" not in browser.current_url


def test_health_check(browser):
    url = "https://courses.uet.vnu.edu.vn/"

    try:
        # Open the website
        browser.get(url)

        # If the website is accessible, the script will reach this point without errors
        assert "website môn học" in browser.title.lower()

    except Exception as e:
        # Fail the test if there are any exceptions (e.g., WebDriverException)
        pytest.fail(f"Failed to connect to {url}. Error: {e}")


def test_search_on_vnexpress(browser):
    url = "https://vnexpress.net/"

    try:
        # Open the VNExpress website
        browser.get(url)

        # Find the search form element by its ID
        search_form = browser.find_element(By.ID, "formSearchHeader")

        # Find the search input and submit button within the form
        search_input = search_form.find_element(By.ID, "keywordHeader")
        submit_button = search_form.find_element(By.ID, "buttonSearchHeader")

        # Click the search button to activate the search input
        submit_button.click()

        # Enter the search query
        search_input.send_keys("Trương Mỹ Lan")

        time.sleep(2)

        submit_button.click()

        time.sleep(5)

        browser.switch_to.window(browser.window_handles[1])

        # Example: Check if the search results page is displayed
        assert "Kết quả tin tức cho từ khóa Trương Mỹ Lan" in browser.title

    except Exception as e:
        # Fail the test if there are any exceptions
        pytest.fail(f"Failed to perform the search on {url}. Error: {e}")
