import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Remote(
        command_executor='http://172.18.0.1:4444/wd/hub', options=webdriver.ChromeOptions())

    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()

def test_selenium_grid_chrome1(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Grid with Chrome")
    search_box.submit()

    assert "Selenium Grid with Chrome" in browser.title

def test_selenium_grid_chrome2(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Grid with Chrome")
    search_box.submit()

    assert "Selenium Grid with Chrome" in browser.title

def test_selenium_grid_chrome3(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Grid with Chrome")
    search_box.submit()

    assert "Selenium Grid with Chrome" in browser.title

def test_selenium_grid_chrome4(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Grid with Chrome")
    search_box.submit()

    assert "Selenium Grid with Chrome" in browser.title

def test_selenium_grid_chrome5(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Grid with Chrome")
    search_box.submit()

    assert "Selenium Grid with Chrome" in browser.title

def test_selenium_grid_chrome6(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Grid with Chrome")
    search_box.submit()

    assert "Selenium Grid with Chrome" in browser.title

def test_selenium_grid_chrome7(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Grid with Chrome")
    search_box.submit()

    assert "Selenium Grid with Chrome" in browser.title
