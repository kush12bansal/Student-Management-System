# Student Management System

A web-based **Student Management System** built with Flask and MySQL that provides secure authentication, real-time database integration, and CRUD operations to manage student data, grades, and attendance. This system is designed for educational institutions to simplify administrative tasks related to student information.

## Features

### 1. **Secure Authentication**
   - Users can securely log into the system using their credentials (username and password).
   - Passwords are stored securely in the database using hashing algorithms to ensure data safety.
   - User sessions are managed, allowing users to stay logged in across different pages while maintaining session integrity.
   - The login system is protected against common vulnerabilities such as SQL injection and session hijacking.

### 2. **Dashboard Navigation**
   - After logging in, users are directed to a dashboard where they can easily navigate between different sections of the system (Students, Attendance, Grades).
   - The dashboard provides an overview of the essential tasks and allows quick access to the main features, making it easy for admins and staff to manage student data.

### 3. **CRUD Operations for Students**
   - **Create**: Admins can add new student records by providing details such as name, age, address, and more.
   - **Read**: View a list of all students, along with the ability to search and filter by various criteria (e.g., name, grade).
   - **Update**: Update any student information as needed, ensuring data remains current.
   - **Delete**: Admins can remove students from the system, with a confirmation prompt to prevent accidental deletions.

### 4. **Grade Management**
   - Teachers or administrators can manage student grades through the system.
   - **Add grades**: Teachers can add grades for students, specifying the subject and grade.
   - **Edit grades**: Teachers can modify grades if necessary, for example, if a grading mistake was made.
   - **Delete grades**: Admins can delete grades if needed, with proper authorization required for such actions.
   - Grades are stored in relation to each student, ensuring easy access and tracking of academic performance over time.

### 5. **Attendance Tracking**
   - Teachers or admins can track student attendance for each class or day.
   - Attendance data is saved, allowing teachers to mark a student's attendance (Present/Absent).
   - Attendance records can be viewed and updated for each student, providing a historical overview of attendance.
   - The system can automatically calculate attendance percentages for students based on their recorded presence or absence.
   - Teachers can print or export attendance data for reporting or analysis.

### 6. **Real-Time Database Operations**
   - The system uses a Flask API to interact with the MySQL database, ensuring that updates to student records, grades, or attendance are reflected in real-time.
   - Any changes made in the system (like adding a student or modifying grades) are instantly updated and displayed to all users viewing the relevant page.
   - This ensures that the system operates smoothly and that data is always up-to-date.

### 7. **Responsive User Interface**
   - Built with a mobile-first approach, ensuring a seamless experience across devices, whether it’s viewed on a desktop, tablet, or smartphone.
   - The design adapts to different screen sizes, ensuring that all elements of the system are accessible on all devices.
   - A clean, professional design provides users with a user-friendly experience, making it easy to navigate and interact with the system.
   - Interactive elements such as dropdowns, form validation, and search functionality are provided to ensure smooth operations.

### 8. **Search and Filter Functionality**
   - Users can search for students by name, grade, or attendance status using a powerful search function.
   - The system provides various filtering options, such as sorting students by grade, attendance percentage, or enrollment status.
   - This feature simplifies the process of finding specific students or records, saving time for admins and teachers.

## Tech Stack

### Frontend
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) **HTML5**: Structure of the web pages.
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) **CSS3**: Styling and layout.
- ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black) **JavaScript**: Client-side interactivity and form validations.

### Backend
- ![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white) **Flask**: A lightweight Python web framework for routing and server-side logic.

### Database
- ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white) **MySQL**: Relational database management system to store student, grades, and attendance data.

## How to Run Locally

1. **Clone the Repository**:
git clone https://github.com/kush12bansal/Student-Management-System.git cd Student-Management-System

2. **Install Dependencies**:
Create and activate a virtual environment (optional but recommended):
python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate

3. **Install the required Python packages**:
pip install -r requirements.txt

4. **Setup MySQL Database**:
- Create a MySQL database for the project. You can use the following SQL query to create a database:
  ```sql
  CREATE DATABASE student_management_system;
  ```
- Import the required schema by running the SQL script in `database/setup.sql`.

5. **Configure Environment Variables**:
- Set up a `.env` file to store sensitive environment variables like the database username, password, and Flask app settings:
  ```
  FLASK_APP=app.py
  FLASK_ENV=development
  MYSQL_USER=your_username
  MYSQL_PASSWORD=your_password
  MYSQL_HOST=localhost
  MYSQL_DATABASE=student_management_system
  ```

6. **Run the Flask Server**:
python app.py

7. **Open the Application**:
- Open your browser and navigate to:
  ```
  http://localhost:5000/
  ```

- You should now see the dashboard of the **Student Management System**.
