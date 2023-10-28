from page.registration_page import RegistrationPage


def test_fill_registration_form():
    registration_page = RegistrationPage()

    registration_page.open_page()
    registration_page.fill_first_name('Vitalii')
    registration_page.fill_last_name('Sharov')
    registration_page.fill_email('vitalii@example.com')
    registration_page.gender_selection('Male')
    registration_page.fill_user_number('1234567890')
    registration_page.fill_date_of_birth(year='1988', month='June', day='26')
    registration_page.select_subject('m')
    registration_page.select_hobbies('Sports')
    registration_page.add_file('23.jpg')
    registration_page.fill_current_adress('Lenin Street')
    registration_page.select_state('Har')
    registration_page.select_city('Ka')
    registration_page.submit_form()

    registration_page.registered_user_with(
        'Vitalii Sharov',
        'vitalii@example.com',
        'Male',
        '1234567890',
        '26 June,1988',
        'Maths',
        'Sports',
        '23.jpg',
        'Lenin Street',
        'Haryana Karnal')
