Feature: Login
  Validates the Login functionality

  Scenario Outline: Validate email input field
  Validating that email field accepts only valid email
    Given The user opens the GUVI homepage
    When Clicking on Login button
    Then Enter the <email>
    And validate the email <expected_error> is displayed
    Examples:
      | email          | expected_error                                                  |
      | qwerty         | Hmm...that doesnt look like an email address. Try again.        |
      | qwerty@test.in | Oh! No profile exists with this Email ID. Click here to Sign Up |


  Scenario Outline: Validate login fails for invalid credentials
  Validating login fails for invalid credentials
    Given The user opens the GUVI homepage
    When Clicking on Login button
    Then Enter "<email>" and "<password>"
    And validate the login <expected_error> is displayed
    Examples:
      | email                | password | expected_error                                |
      | EMPTY                | EMPTY    | Hey, Did you forgot your password? Try again. |
      | indulax.88@gmail.com | EMPTY    | Hey, Did you forgot your password? Try again. |
      | indulax.88@gmail.com | qwerty   | Incorrect Email or Password                   |

  @smoke
  Scenario: Verify login functionality with valid credentials
  Validating login success for valid credentials
    Given The user opens the GUVI homepage
    When Clicking on Login button
    Then Enter "indulax.88@gmail.com" and "password"
    And Login should be successful

  Scenario: Verify sign out is success
    Given The user opens the GUVI homepage
    When Clicking on Login button
    Then Enter "indulax.88@gmail.com" and "password"
    And Login should be successful
    And The user should be able to logout successfully
