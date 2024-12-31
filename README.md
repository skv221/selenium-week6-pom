# Week 6: Page Object Model (POM) Implementation with Hybrid Framework

This repository contains my work for Week 6 of the Python Selenium Learning Journey. The focus was on implementing the **Page Object Model (POM)** for a new web automation project, integrating it with a **Hybrid Framework** for enhanced flexibility and scalability.

## Key Learnings:
- **Hybrid Framework Implementation**: Combined the strengths of Data-Driven and Keyword-Driven frameworks for test automation, providing greater flexibility in test execution.
- **Page Object Model (POM)**: Applied POM to structure the test automation code, making it more modular and maintainable.
- **Test Execution**: Wrote and executed tests using the hybrid framework with POM, ensuring the scalability and reusability of the test scripts.

## Tasks:
- **Task 1**: Implemented the **Page Object Model (POM)** in a new automation project, creating separate classes for each page of the web application.
- **Task 2**: Integrated the **Hybrid Framework** into the project, enabling data-driven and keyword-driven test execution.
- **Task 3**: Refactored the test scripts to follow the **POM** structure and hybrid framework principles, ensuring easy maintenance and scalability.
- **Task 4**: Ran the tests using the hybrid framework and POM, verifying that the code structure improved reusability and modularity.

## Technologies Used:
- **Python**: The primary programming language for the automation scripts.
- **Selenium WebDriver**: Used for web automation tasks.
- **Pytest**: For executing test cases and generating reports.
- **Page Object Model (POM)**: To structure the automation code into modular page objects.
- **Hybrid Framework**: Combines data-driven and keyword-driven testing approaches for better flexibility.

## How to Run:
1. Clone the repository:
    ```bash
    git clone <repository-link>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the tests and generate an HTML report:
    ```bash
    pytest --html=reports/report.html --self-contained-html
    ```

   This will generate an HTML report in the `reports` directory as `report.html` after running the tests.

## Future Enhancements:
- Integrate Continuous Integration (CI) for automated testing.
- Expand the hybrid framework to support additional test scenarios.
- Optimize the locator strategies and implement better synchronization methods.
