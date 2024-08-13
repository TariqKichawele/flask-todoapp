# ToDo App

![Screenshot 2024-08-13 at 6 35 16 PM](https://github.com/user-attachments/assets/35c84d55-ce09-4fa8-a388-1de9874a56a8)

**Overview**

This To-Do App is a simple yet powerful task management application built using Flask, PostgreSQL, SCSS, and HTML. It allows users to efficiently manage their daily tasks by adding, editing, and deleting to-dos in a user-friendly interface.

**Features**

- Add New Tasks: Easily add tasks to your to-do list.
- Edit Tasks: Modify existing tasks to update details or deadlines.
- Delete Tasks: Remove tasks that are completed or no longer needed.
- Responsive Design: The app is styled with SCSS for a modern, responsive UI, ensuring a smooth experience on all devices.
- Persistent Storage: Task data is stored securely in a PostgreSQL database, allowing tasks to be retained even after the application is closed or refreshed.

**Tech Stack**

- Flask: A lightweight web framework used to create the backend of the application.
- PostgreSQL: A robust, scalable database used to store the tasks and related data.
- SCSS: Used for styling the app, allowing for more organized and maintainable CSS.
- HTML: The structure of the app is built with standard HTML, ensuring compatibility across all browsers.

**Installation**

Clone the repository:
bash

Copy code
git clone https://github.com/TariqKichawele/flask-todoapp.git
cd flask-todoapp

Install dependencies:
bash
Copy code
pip install -r requirements.txt

Set up the database:
Create a PostgreSQL database and update the connection details in the app's configuration.
Run the database migrations to set up the tables.
Run the application:
bash
Copy code
flask run
Open the app in your browser:
Navigate to http://localhost:5000 to start managing your tasks.
Usage

Open the app in your browser.
Add new tasks using the input form.
Edit tasks by clicking on them in the list.
Delete tasks when they are completed.

Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. All contributions are welcome!

License

This project is licensed under the MIT License - see the LICENSE file for details.

  
