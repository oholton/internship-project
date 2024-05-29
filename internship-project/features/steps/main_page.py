from behave import given, when, then
from time import sleep

@given('Open the main page')
def open_page(context):
    context.app.login_page.open_login()

@when('Log in to the page')
def login(context):
    context.app.login_page.login()

@then('Click on "off plan" at the left side menu')
def click_offleft(context):
    context.app.main_page.offleft()

@then('Verify the right page opens')
def verify_offleft(context):
    context.app.main_page.verify_offleft_page()
    sleep(3)

@then('Filter by sale status of “Last Units”')
def filter_last_units(context):
    context.app.main_page.filter_by_last_unit()

@then('Verify each product contains the Last Units tag')
def verify_last_units_tag(context):
    context.app.main_page.verify_tag_last_units()

