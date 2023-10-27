from users.users import User
from page.registration_page import RegistrationPage
from users_data.user1_data import Vitalii_Sharov

registration_page = RegistrationPage()
def test_submit_student_registration_form_by_high_steps():
    student = Vitalii_Sharov


    registration_page.open_form()
    registration_page.submit_form(student)
    registration_page.should_have_registrated_user(student)
