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

    Scenario: User can add a project through the settings
      Given Open the main page
      When Log in to the page
      Then Click on "settings" option
      And Click on "Add a project" option
      And Verify the project page opens
      And Add some test information to the input fields
      And Verify the right information in the input fields selected
      And Verify “Send an application” button is available and clickable

