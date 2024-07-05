# Created by leoh2 at 5/28/2024
Feature: Main page
  # Enter feature description here

  Scenario: User can filter by sale status Last units
    Given Open the main page
    When Log in to the page
    Then Click on "off plan" at the left side menu
    And Verify the right page opens
    And Filter by sale status of “Last Units”
    And Verify each product contains the Last Units tag

  Scenario: User can filter by sale status Last units on mobile
    Given Open the main page
    When Log in to the page
    Then Click on "off plan" on mobile
    And Verify the right page opens
    And Filter by sale status of “Last Units” on mobile
    And Verify each product contains the Last Units tag

  Scenario: User can click on “Connect the company” on the left side of the main page
    Given Open the main page
    When Log in to the page
    And Click on “Connect the company”
    Then Switch the new tab
    And Verify the right tab opens