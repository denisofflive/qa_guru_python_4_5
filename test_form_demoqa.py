from selene.support.shared import browser
from selene import be, have
import os

FIRSTNAME = 'Denis'
LASTNAME = 'Denisov'
EMAIL = 'denis@denisov.com'
MOBILE = '1234567890'
FILE = '001.jpg'
ADDRESS = 'Moscow'
STATE = 'Uttar Pradesh'
CITY = 'Agra'


def test_form_demoqa(browser_setup):
    browser.open(browser.config.base_url + "/automation-practice-form")
    browser.element('#firstName').should(be.blank).type(FIRSTNAME)
    browser.element('#lastName').should(be.blank).type(LASTNAME)
    browser.element('#userEmail').should(be.blank).type(EMAIL)
    browser.element('[for="gender-radio-1"]').should(have.text('Male')).click()
    # browser.element(f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']").click()
    browser.element('#userNumber').should(be.blank).type(MOBILE)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="2"]').should(have.text('March')).click()
    browser.element('.react-datepicker__year-select option[value="1985"]').should(have.text('1985')).click()
    browser.element('.react-datepicker__day--015').should(have.text('15')).click()
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').should(have.text('Music')).click()
    # browser.element(f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']").click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + f'/resources/{FILE}')
    browser.element('#currentAddress').should(be.blank).type(ADDRESS)
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').should(have.text(STATE)).click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').should(have.text(CITY)).click()
    browser.element('#submit').click()

    """Валидация отображаемых данных"""

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element('tr:nth-child(1) td:nth-child(2)').should(have.text(f'{FIRSTNAME} {LASTNAME}'))
    browser.element('tr:nth-child(2) td:nth-child(2)').should(have.text(EMAIL))
    browser.element('tr:nth-child(3) td:nth-child(2)').should(have.text('Male'))
    browser.element('tr:nth-child(4) td:nth-child(2)').should(have.text(MOBILE))
    browser.element('tr:nth-child(5) td:nth-child(2)').should(have.text('15 March,1985'))
    browser.element('tr:nth-child(6) td:nth-child(2)').should(have.text('Maths'))
    browser.element('tr:nth-child(7) td:nth-child(2)').should(have.text('Music'))
    browser.element('tr:nth-child(8) td:nth-child(2)').should(have.text(FILE))
    browser.element('tr:nth-child(9) td:nth-child(2)').should(have.text(ADDRESS))
    browser.element('tr:nth-child(10) td:nth-child(2)').should(have.text(f'{STATE} {CITY}'))
    # time.sleep(3)
    browser.element('#closeLargeModal').click()
