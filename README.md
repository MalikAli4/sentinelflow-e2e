SentinelFlow E2E

This system is a production styled end to end QA automation framework built to validate critical user workflows in a web based admin dashb$

The framework simulates real user behavior using Playwright and PyTest to ensure that core functionality such as authentication, navigatio$

This franework currently validates the following workflows:
 
* User authentication (Testing valid and invalid login scenarios)
* Naviagtion to core modules such as the Admin and Time pages. 
* Admin user seach functionality (Positive and Negative cases)

These tests are designed to verify both expected behavior and failure handling

Tech Stack:
 
* Python
* Playwright
* PyTest
* GitHub Actions
* pytest-html (for reporting)

Key Features:
* Page Object Model (LoginPage, AdminPage, TimePage)
* Positive & Negative test coverage
* Automated UI interaction
* Screenshot capture on test failure 
* HTML test reports
* CI pipeline with GitHub Actions
* Artifact upload (reports & screenshots)

How to Run Tests:

1. Clone the repository:
        git clone https://github.com/MalikAli4/sentinelflow-e2e.git
        cd sentinelflow-e2e
2. Create and activate a virtual environment:   
        python3 -m venv venv
        source venv/bin/activate
3. Install Dependencies:
        pip install pytest playwright pytest-playwright pytest-html
        playwright install
4. Run the test suite:
        pytest –html=artifacts/report.html –self-contained-html


For Test Reporting 

* HTML reports are generated after each test run 
* Failed tests automatically capture screenshots
* Artifacts are stored under "artifacts/"


Purpose 

This project demonstrates real world QA automation skills, including: 

* E2E testing 
* Positive and Negative test design 
* Page Object Model architecture 
* Failure Handling and Debugging 
* CI/CD Integration 

Author 
Jay (Malik) Wells 
GitHub: https://github.com/MalikAli4
