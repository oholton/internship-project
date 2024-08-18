from behave import given, when, then

@then ("Verify the community page is open")
def verify_community_page_opened(context):
    context.app.community_page.verify_community_page()

@then ("Verify 'contact support' is clickable")
def verify_contact_support_clickable(context):
    context.app.community_page.verify_contact_support_button_clickable()

