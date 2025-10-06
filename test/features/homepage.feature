Feature: Homepage
  Scenario: Verify that GUVI homepage is loaded successfully
    Given The user opens the GUVI homepage
    When The page is fully loaded
    Then The user should see the signup button

  Scenario: Verify whether the title of the webpage is correct
    Validate the GUVI webpage title is  “GUVI | Learn to code in your native language”
    Given The user opens the GUVI homepage
    When The page is fully loaded
    Then Verify the "home" page title

  @smoke
  Scenario: Validate the Login button
    Verify visibility and clickability of the Login button
    Given The user opens the GUVI homepage
    When The page is fully loaded
    Then The Login button should be visible and clickable
    And Verify the "login" page title
    And Verify the "login" page url

  Scenario: Validate the Sign up button
    Verify visibility and clickability of the Sign-Up button.
    Given The user opens the GUVI homepage
    When The page is fully loaded
    Then The Sign up button should be visible and clickable
    And Verify the "signup" page title
    And Verify the "signup" page url


