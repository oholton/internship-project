from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open the main page')
def open_page(context):
    context.app.login_page.open_login()

@when('Log in to the page')
def login(context):
    context.app.login_page.login()

@when('Click on “Connect the company”')
def connect_the_company(context):
    context.app.main_page.click_connect_company()

@then('Switch the new tab')
def switch_to_company(context):
    context.app.main_page.switch_new_tab()

@then('Click on "off plan" at the left side menu')
def click_offleft(context):
    context.app.main_page.offleft()

@then('Click on "off plan" on mobile')
def click_mobileoffleft(context):
    context.app.main_page.mobile_offleft()

@then('Filter by sale status of “Last Units” on mobile')
def filter_mobile(context):
    context.app.main_page.mobile_filter()

@then('Verify the right page opens')
def verify_offleft(context):
    context.app.main_page.verify_offleft_page()

@then('Filter by sale status of “Last Units”')
def filter_last_units(context):
    context.app.main_page.filter_by_last_unit()

@then('Verify each product contains the Last Units tag')
def verify_last_units_tag(context):
    context.app.main_page.verify_tag_last_units()

@then('Verify the right tab opens')
def verify_offleft(context):
    context.app.connect_company.verify_connect_company_open()

@then('Click on "settings" option')
def click_settings(context):
    context.app.main_page.click_settings()