import time

from selene.support.shared import browser
from selene import be, have
import random


def test_form_demoqa(base_url):
    browser.element('#firstName').should(be.blank).type('Denis')
    browser.element('#lastName').should(be.blank).type('Denisov')
    browser.element('#userEmail').should(be.blank).type('denis@denisov.com')
    browser.element(f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']").click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="2"]').should(have.text('March')).click()
    browser.element('.react-datepicker__year-select option[value="1985"]').should(have.text('1985')).click()
    browser.element('.react-datepicker__day--015').should(have.text('15')).click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element(f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']").click()
    browser.element('#uploadPicture').send_keys("E:/qa_guru_python_4_5/001.jpg")
    browser.element('#currentAddress').should(be.blank).type('Moscow')
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').should(have.text('Uttar Pradesh')).click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').should(have.text('Agra')).click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    time.sleep(5)
