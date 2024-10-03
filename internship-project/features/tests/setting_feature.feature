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

  Scenario: User can go to community page and click contact support
    Given Open the main page
    When Log in to the page
    Then Click on "settings" option
    And Click on "community" button
    And Verify the community page is open
    And Verify 'contact support' is clickable

  Scenario: User can open the Contact us page
    Given Open the main page
    When Log in to the page
    Then Click on "settings" option
    And Click on the "Contact us" option
    And Verify the correct page opens
    And Verify there are at least 4 social media icons
    And Verify the “Connect the company” button is available and clickable

    Scenario: User can open User guide page
      Given Open the main page
      When Log in to the page
      Then Click on "settings" option
      And Click on "User Guide" option
      And Verify the "User Guide" page opens
      And Verify all lesson videos contain titles

      Scenario: User can change password
        Given Open the main page
        When Log in to the page
        Then Click on "settings" option
        And Click on Change password option
        And Verify the change password page opens
        And Add some test password to the input fields
        And Verify the “Change password” button is available

    Scenario: User can go to settings and see the right number of UI elements
      Given Open the main page
      When Log in to the page
      Then Click on "settings" option
      And Verify the right page opens up
      And Verify that there are 12 options for settings
      And Verify 'connect to company' button is available