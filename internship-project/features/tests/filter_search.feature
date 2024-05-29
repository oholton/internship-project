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