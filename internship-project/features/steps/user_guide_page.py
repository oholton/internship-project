from behave import given, when, then

@then ('Click on "User Guide" option')
def click_on_user_guide_page(context):
    context.app.settings_page.click_user_guide()

@then ('Verify the "User Guide" page opens')
def verify_user_guide_page(context):
    context.app.user_guide_page.verify_user_guide_open()

@then ('Verify all lesson videos contain titles')
def verify_video_titles(context):
    context.app.user_guide_page.verify_video_title_links()
