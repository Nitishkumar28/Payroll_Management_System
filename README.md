# Payroll_Management_System 

Payroll Management System

The Payroll Management System is a Python-based application designed to efficiently manage employee information, department details, salaries, incentives, and generate reports for an organization. The system interacts with a MySQL database to store and retrieve data, providing a user-friendly interface for managing payroll-related tasks.
Features

    User Authentication: The system offers user authentication through a login and sign-up process, ensuring secure access to authorized users.

    Employee Management: The application allows users to add new employees to the database, including their personal details (name, gender, contact information) and employment details (date of joining, department, designation, projects).

    Department and Designation: Users can specify the department and designation of each employee, allowing for easy categorization and organization of the workforce.

    Salary Calculation: The system calculates employee salaries based on provided inputs, including basic salary, HRA (House Rent Allowance), DA (Dearness Allowance), and tax deductions.

    Incentive Calculation: The application supports the calculation of incentives for employees. Default incentives and department-based incentives can be set, and net incentive values are automatically updated.

    Data Manipulation and Reporting: Users can update employee details, department information, and salary components. The system provides options to view employee details based on various criteria (designation, department, salary, projects). Comprehensive reports for individual employees or all employees can be generated.

Getting Started

    Clone the repository: git clone https://github.com/yourusername/payroll-management.git
    Install required packages: pip install mysql-connector-python tabulate
    Set up a MySQL database and update the database credentials in the code.
    Run the main.py file to launch the application.

Usage

    Upon running the application, users are prompted to log in or sign up.
    Once logged in, users can choose from various menu options to perform different tasks.
    Menu options include adding or deleting employees, updating employee details, viewing employee information, generating reports, updating salaries, and managing incentives.


Acknowledgements

    Python
    MySQL
    tabulate
