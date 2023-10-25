from selene import browser, be


class RegistrationPage:
    def open_page(self):
        browser.open('/automation-practice-form')
        return self
    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self