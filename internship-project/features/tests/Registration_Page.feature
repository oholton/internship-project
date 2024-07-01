# Created by leoh2 at 6/30/2024
Feature: Registration Page
  Verify if user can enter information in text field

  Scenario: User can enter information into text field
    Given Open registration page
    When Input text for first and last name
    And Input phone number
    And Input text for email address
    And Input text for password
    Then Verify info for first and last name
    And Verify phone number
    And Verify text for email address
    And Verify text for password
