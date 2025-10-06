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

Project1EdTechWebApp/test/features/ 
-------------
To have the test scenarios written in plain English (BDD)
- homepage.feature
- login.feature

Project1EdTechWebApp/test/step_definitions/
-------
Step definition files to implement the code for each step mentioned in feature file.
- homepage_steps.py → Code that connects feature steps to actions
- login_steps.py

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
------------------------------
Pre-requisites:
----
- Python 3.8 or higher
- Google Chrome (or Firefox / Edge)
- Internet connection (for driver downloads)
--------------------------
Download the Plugins
-----
Run 'pip install -r requirements.txt' in project terminal

Run the testcases:
------
- To run the test cases in Chrome by default:
    pytest -v --alluredir=reports
- To run in a different browser
    - pytest -v --browser=firefox --alluredir=reports
    - pytest -v --browser=edge --alluredir=reports
- To run specific feature file
    - pytest test/features/homepage.feature -v --alluredir=reports
- To run selected testcases using markers
    - pytest -m smoke --alluredir=allure-results
    - Here smoke is one of the marker defined in pytest.ini
    - --alluredir tells pytest where to save the results for Allure
--------------------------------   

 
Reporting
----------
- To view the Allure test report run: allure serve reports
- This will open a detailed dashboard in your browser,
- Shows test results, logs and screenshots.

---------------------------------

Author
-------
Indumathi

