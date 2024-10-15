# Created by leoh2 at 10/15/2024
Feature: Test features for Secondary Page

  Scenario: User can open the Secondary deals page and go through the pagination
    # Enter steps here
    Given Open the main page
    When Log in to the page
    And Click on Secondary option at the left side menu
    Then Verify the Secondary page opens
    And Go to the final page using the pagination button
    And Go back to the first page using the pagination button