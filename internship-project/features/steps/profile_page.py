from behave import given, when, then

@then('Change "company" information')
def change_company(context):
    context.app.profile_page.company_text_change()

@then('Verify the right information is present in the input fields')
def verify_input_fields(context):
    context.app.profile_page.verify_company_text_change()

@then('Verify “Close” and “Save Changes” buttons are available and clickable')
def verify_close_and_save_buttons_clickable(context):
    context.app.profile_page.verify_save_changes_clickable()
    context.app.profile_page.verify_close_button_clickable()