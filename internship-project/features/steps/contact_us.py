from behave import given, when, then

@then('Verify the correct page opens')
def contact_us_page_verification(context):
    context.app.contact_us_page.verify_contact_us_page()

@then('Verify there are at least 4 social media icons')
def verify_social_media_icons(context):
    context.app.contact_us_page.verify_social_media_icons()

@then('Verify the “Connect the company” button is available and clickable')
def verify_connect_company_btn_clickable(context):
    context.app.contact_us_page.verify_connect_the_company_btn()

