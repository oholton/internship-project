# Created by leoh2 at 7/14/2024
Feature: Settings

  Scenario: User can go to settings and edit the personal information
    Given Open the main page
    When Log in to the page
    Then Click on "settings" option
    And Click on "Edit profile" option
    And Change "company" information
    And Verify the right information is present in the input fields
    And Verify “Close” and “Save Changes” buttons are available and clickable