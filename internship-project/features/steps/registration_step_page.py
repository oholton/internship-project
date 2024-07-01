from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open registration page')
def open_registration(context):
    context.app.signup_page.open_registration_page()

@when('Input text for first and last name')
def input_fullname(context):
    context.app.signup_page.enter_full_name()

@when('Input phone number')
def input_phone(context):
    context.app.signup_page.enter_phone_number()

@when('Input text for email address')
def input_email(context):
    context.app.signup_page.enter_email()

@when('Input text for password')
def input_password(context):
    context.app.signup_page.enter_password()

@then('Verify info for first and last name')
def verify_fullname(context):
    context.app.signup_page.verify_full_name()

@then('Verify phone number')
def verify_phonenum(context):
    context.app.signup_page.verify_phone()

@then('Verify text for email address')
def verify_email_text(context):
    context.app.signup_page.verify_email()

@then('Verify text for password')
def verify_passwrd(context):
    context.app.signup_page.verify_password()




