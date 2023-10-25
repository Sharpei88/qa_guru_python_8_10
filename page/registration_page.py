from selene import browser, be, have


class RegistrationPage:
    def open_page(self):
        browser.open('/automation-practice-form')
        return self
    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type('vitalii@example.com')
        return self

    def gender_selection(self, value):
        browser.all('label[for^="gender-radio"]').element_by(have.exact_text(value)).click()
        return self

    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').click().send_keys(year).press_enter()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self
    def select_subject(self, value):
        browser.element('#subjectsInput').type(value)
        browser.all('.subjects-auto-complete__option').element_by(have.exact_text('Maths')).click()
        return self