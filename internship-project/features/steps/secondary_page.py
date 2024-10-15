from behave import given, when, then


@then ('Verify the Secondary page opens')
def verify_secondary_open(context):
    context.app.secondary_page.verify_secondary_page()
@then ('Go to the final page using the pagination button')
def click_final_page(context):
    context.app.secondary_page.click_pagination_button_forward()

@then ('Go back to the first page using the pagination button')
def click_back_page(context):
    context.app.secondary_page.click_pagination_button_backward()
