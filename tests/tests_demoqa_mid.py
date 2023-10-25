import os

from selene import browser, have, be

from page.registration_page import RegistrationPage


registration_page = RegistrationPage()
def test_fill_registration_form():

    registration_page.open_page()

    registration_page.fill_first_name('Vitalii')
    registration_page.fill_last_name('Sharov')
    registration_page.fill_email('vitalii@example.com')
    registration_page.gender_selection('Male')
    registration_page.fill_user_number('1234567890')

    registration_page.fill_date_of_birth(year='1988', month='June', day='26')

    registration_page.select_subject('m')

    browser.all('.subjects-auto-complete__multi-value__label').should(have.exact_texts('Maths'))

    browser.all('label[for^="hobbies-checkbox"]').element_by(have.exact_text('Sports')).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/23.jpg'))

    browser.element('#currentAddress').type('Long address for checking the address \n'
                                            ' entry form and entering it into the test \n'
                                            ' with line breaks')

    browser.element('#react-select-3-input').type('Har').press_enter()
    browser.element('#react-select-4-input').type('Ka').press_enter().press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element('tbody').all('tr')[0].should(have.text('Vitalii Sharov'))
    browser.element('tbody').all('tr')[1].should(have.text('vitalii@example.com'))
    browser.element('tbody').all('tr')[2].should(have.text('Male'))
    browser.element('tbody').all('tr')[3].should(have.text('1234567890'))
    browser.element('tbody').all('tr')[4].should(have.text('26 June,1988'))
    browser.element('tbody').all('tr')[5].should(have.text('Maths'))
    browser.element('tbody').all('tr')[6].should(have.text('Sports'))
    browser.element('tbody').all('tr')[7].should(have.text('23.jpg'))
    browser.element('tbody').all('tr')[8].should(have.text('Long address for checking the address entry form and entering it into the test with line breaks'))
    browser.element('tbody').all('tr')[9].should(have.text('Haryana Karnal'))