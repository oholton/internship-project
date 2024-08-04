from behave import given, when, then
from selenium.webdriver.common.by import By

@then("Verify the project page opens")
def verify_right_page(context):
    context.app.add_a_project_page.verify_add_project_page_open()

@then("Add some test information to the input fields")
def add_test_information_page(context):
    context.app.add_a_project_page.input_name()
    context.app.add_a_project_page.input_company()
    context.app.add_a_project_page.input_role()

@then("Verify the right information in the input fields selected")
def verify_right_information_page(context):
    context.app.add_a_project_page.verify_multiple_text_entries()

@then('Verify “Send an application” button is available and clickable')
def verify_button_clickable(context):
    context.app.add_a_project_page.send_bttn_clickable()
