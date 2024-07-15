from behave import given, when, then

@then ('Click on "Edit profile" option')
def click_edit_profile(context):
    context.app.settings_page.click_edit_profile_button()