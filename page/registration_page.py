from selene import browser


class RegistrationPage:
    def open_page(self):
        browser.open('/automation-practice-form')
        return self