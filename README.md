EdTech WebApplication Automation Framework
----
-------------------------
Introduction:
---
This web automation framework involves 
- ✅ Built using Selenium WebDriver + Pytest + BDD
- ✅ Page Object Model (POM) design
- ✅ Cross-browser support (Chrome, Firefox, Edge)
- ✅ Automatic screenshots on failure
- ✅ Allure reporting with clean results

Usage of this framework:
---------
To exeucute the automation testcases of web application and prepare proper test reports with screenshots and log info.

Project Structure:
-----------------
------------------------------
Project1EdTechWebApp/pages:
-----
- basepage.py: Common browser actions (click, type, waits)
- homepage.py: Homepage related actions
- loginpage.py: Login page related actions
- signuppage.py: Signup page related actions
- locators.py: All the element locators in one place
- mycoursespage.py: Actions involved in the page shown after successful login

Project1EdTechWebApp/test/features/ 
-------------
To have the test scenarios written in plain English (BDD)
- homepage.feature
- login.feature

Project1EdTechWebApp/test/step_definitions/
-------
Step definition files to implement the code for each step mentioned in feature file.
- __init__.py : To mark the step_definitions folder as Python package, so the files can be imported elsewhere in this project
- test_steps_common.py: Has all code part of step definitions common to all feature files
- test_steps_homepage.py: Includes the code part of step definitions involved in homepage
- test_steps_login.py: Includes the code part of step definitions involved in login page

Project1EdTechWebApp/utility/
---------------
- capture_screenshot.py: Takes screenshots including the test failures
- constants.py: Stores values like URLs, credentials, etc.
- logger.py: Prints logs during test execution

Project1EdTechWebApp/conftest.py: Browser setup (Chrome, Firefox, Edge, etc.)
Project1EdTechWebApp/pytest.ini: Pytest configuration file
Project1EdTechWebApp/requirements.txt: List of required Python libraries
Project1EdTechWebApp/pytest.ini: Define markers to execute selected testcases. The markers are used in .feature file
Project1EdTechWebApp/README.md: You’re reading this file 😊

---------------------------------
By using this project, you’ll understand:
----
- How to run web automation tests in Python
- How to write BDD test cases using .feature files
- How to use Page Object Model (POM) for clean code
- How to generate Allure Reports with screenshots


Pre-requisites:
----
- Python 3.8 or higher
- Google Chrome (or Firefox / Edge)
- Internet connection (for driver downloads)


Download the Plugins
-----
Run 'pip install -r requirements.txt' in project terminal
 
Reporting
----------
- To view the Allure test report run: allure serve reports
- This will open a detailed dashboard in your browser,
- Shows test results, logs and screenshots.

Commands to remember:
-------
1. To run all feature files
   pytest   (OR)  pytest tests/features/
2. To run feature file
   pytest tests/features/login.feature
3. To run multiple feature files
   pytest tests/features/login.feature tests/features/homepage.feature
4. To run test by marker for example 'smoke' defined in .ini file,and @smoke in.feature file
   pytest -m smoke 
5. Run with Allure reporting: To run tests and generate report
   pytest --alluredir=reports/allure-results
   To view the report
      allure serve reports/allure-results
      This will automatically build and open the report in browser
   To save HTML report inside the reports folder.
      allure generate reports/allure-results -o reports/allure-reports --clean
6. To run with specific browser
   pytest --browser=firefox tests/features/login.feature
7. To run tests by keyword/scenario name
   pytest -k "login"
   Here all the test scenarios containing "login" in it will get executed.
8. To run in verbose mode for debugging
   pytest -v  (OR)  pytest -v tests/features/login.feature
9. To stop at first failure, thi is useful for debugging one case at a time.
    pytest -x
10. To check the step definitions are discovered correctly
    pytest ---collect-only   (OR)   pytest --collect-only -q

Example combined run commands:
------
1. Run login feature with Firefox and Allure
   pytest --browser=firefox tests/features/login.feature --alluredir=reports/allure-results -v

2. Run only smoke tests with Allure in Chrome
    pytest -m smoke --alluredir=reports/allure-results

3. Run everything wth Allure
    pytest tests/features/ --alluredir=reports/allure-results -v
    then run: allure serve reports/allure-results
Author
-------
Indumathi

