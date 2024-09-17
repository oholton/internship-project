from behave import given, when, then

@then('Verify the change password page opens')
def verify_change_password_page_open(context):
    context.app.change_password_page.verify_password_page()

@then('Add some test password to the input fields')
def enter_passwords(context):
    context.app.change_password_page.input_new_password()
    context.app.change_password_page.repeat_new_password()

@then('Verify the “Change password” button is available')
def verify_change_password_btn_clickable(context):
    context.app.change_password_page.verify_change_password_clickability()

