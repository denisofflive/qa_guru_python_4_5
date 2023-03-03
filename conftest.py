import pytest
from selene.support.shared import browser

@pytest.fixture()
def window_size():
    browser.config.window_width = 1024
    browser.config.window_height = 768

@pytest.fixture()
def base_url():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.driver.maximize_window()