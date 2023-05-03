import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_google_search():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://www.google.com")
    search_box = driver.find_elements(By.CSS_SELECTOR, "[name=q]").pop()

    search_box.send_keys("stam")

    search_box.submit()
    assert "stam" in driver.title

    driver.quit()
