from behave import given, when, then

@then ('Click on "Edit profile" option')
def click_edit_profile(context):
    context.app.settings_page.click_edit_profile_button()

@then ('Click on "Add a project" option')
def click_add_project(context):
    context.app.settings_page.click_add_project_button()

@then ('Click on "community" button')
def click_community_button(context):
    context.app.settings_page.click_community_button()

@then ('Click on the "Contact us" option')
def click_contact_us_button(context):
    context.app.settings_page.click_contact_us_button()

@then ('Click on Change password option')
def click_change_password(context):
    context.app.settings_page.click_change_password_option()