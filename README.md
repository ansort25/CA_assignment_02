# CA_assignment_02
Using any programming language of your choice (Java, JavaScript, Python, etc.) please create a small API testing project with a framework of your choice (Rest Assured, KarateDSL, Jasmine, Behave etc.) for the following scenario:

Using the documentation of the attached API: https://rickandmortyapi.com/

Test both the Rest API/character and the GraphQL calls, asserting:
- Status code;
- Body response;
- Latency below 1 second;
- Test correct negative cases

Make sure test report is generated at the end of the test run.

Please share a link to the project (Google Drive with packages or even better GitHub project) to the recruitment team.

---

Run on Python3.12. Pytest and pytest-reporter-html1. As a reporting tool pytest-reporter could be used to create custom templates with Jinja2

Steps to setup project:
- install requirements.txt running in terminal `pip install -r requirements.txt`

To run tests:
- run `pytest .\tests\ --template=html1/index.html --report=report.html`
Reports will be generated in root directory in a file called report.html.

---
Notes:
- test cases for Graphql are limited, these are just some example of what can be achieved
- reporting can be upgraded using pytest-reporter by creating custom reports
- tried a testing tool for Graphql https://github.com/schemathesis/schemathesis which installed a bunch od dependencies
that are not in use now as I needed more time to learn how to use that tool