# Mom Schedule
## A Time Planning Tool for Busy Mothers

Mom Schedule is a time-planning tool for busy Mothers. The application has a calendar and offers event editing and creating task cards.

As a site user, you can: Log in, Create Tasks, Categorize and Filter by following criteria: All Tasks, Calendar - to Overview your Month, See Completed Tasks Only, Hide Completed Tasks, Filter by Due Date, Filter by selected Category - Work, Childcare, Household, Health, Free time and Other tasks.

Main Technologies applied are: HTML, CSS, Python, Django Framework and Postgres Relational database.

This is the fourth Portfolio Project in frames of the Code Institute Full Stack Web Developer Course Assessment.

:point_down: Click the link below for the live view: 

# [Live View](https://mom-schedule.herokuapp.com/)


<img width="73%" alt="responsiveness" src="documentation_for_github_readme/tablet.png"> <img width="26%" alt="responsiveness" src="documentation_for_github_readme/phone.png">


## Contents:
- [UX](#ux)
    - [User Stories](#user-stories)
    - [Responsivity](#responsivity)
    - [User Friendly Messages](#user-friendly-messages)
- [Features](#features)
    - [Homepage](#homepage)
    - [Site Header and Log in](#site-header-and-log-in)
    - [Authentication and Authorization](#authentication-and-authorization)
    - [Site Navigation](#site-navigation)
        - [Sidebar](#sidebar)
        - [My Tasks](#my-tasks-and-filter-by-dropdown)
    - [Contact Us](#contact-us)
    - [New Task](#new-task)
    - [Future Features](#future-features)
- [Development Stages](#development-stages)
    - [Planning](#planning)
    - [Structure](#structure)
    - [Using Frameworks and Libraries](#using-frameworks-and-libraries)
    - [Using Source code](#using-source-code)
- [Testing](#testing)
    - [Validators](#validators)
    - [Manual Testing](#manual-testing)
    - [Automatic Testing - Writing Functions](#automatic-testing---writing-functions)
    - [Debugging](#debugging)
    - [Remaining Issues](#remaining-issues)
- [Deployment](#deployment)
    - [Heroku](#creating-the-heroku-app)
- [Sources & Credits](#sources--credits)
    - [Sources](#sources)
    - [Tools](#tools)
    - [Acknowledgments](#acknowledgments)


## UX

It is crucial to identify and get to know the website user in order to enhance the user experience. A Persona method helps 'bringing to life' a real-life individual with personality traits, favourite choices and preferences. Jane Smith (the Persona) is a working mother that loves bio products and enjoys walks in the nature. She will like the Mom Schedule colour pallette in natural tones. The persona summary is created with a tool called Xtensio that helps to conduct a virtual UX analysis. Additionally, a customer journey tracking was conducted to follow Jane's navigation and make it to her most convenience.

More about this user Persona is described in my previous project, called Mom Lifehacks: https://github.com/annagabain/Mom-Lifehacks#User-Experience-and-User-Interface-Design-UX-and-UI

### User Stories

- As a site user, I can register so that I can have a unique and private schedule.

- As a site user, I can **log in** so that I can view my own schedule.

- As a user, I can see a navigation option (sidebar) so that I can create, sort my tasks, manage them, as well as find the contact option.

- As a site user I can **Create** a task so that I can note down an event or an activity.

- As a site user, I can **View** an individual task so that I can read the details of it.

- As a site user, I can **Edit** an individual task so that I can adapt it to my needs.

- As a site user I can **Delete** an individual task so that I can remove the no longer needed information.

- As a user I can see my tasks as cards so that I have a better visual overview.

- As a user, I can view my tasks marked on a calendar so that I can remember the dates.

- As user I can contact the site owners so that can ask questions or provide feedback.

- As **a Site Admin**, I can log in so that I can **view and manage the users, task categories and tasks**.

- As a Site Admin, I can see the messages sent from the 'contact us' form so that I can **communicate with the user**.

- As a Site Admin, I can access the user registration information so that I can help them changing the passwords, editing or deleting the accounts.


All user stories as part of a project: https://github.com/users/annagabain/projects/7/views/1


### Responsivity

There have been two main device views considered for the responsivity of Mom Schedule: Mobile and Laptop. Some efforts have been made to make sure the application is visually appealing and functional on tablets and larger monitors as well.

*Initial test result: Am I responsive?*

<img width="70%" alt="responsiveness" src="documentation_for_github_readme/responsiveness.jpg">

The Methods to achieve desired device responsivity level include Bootstrap5 features and custom CSS.

<img width="70%" alt="responsivity" src="documentation_for_github_readme/responsivity.jpg">

### User Friendly Messages

In order to reassure the user for the actions they have taken, as well as to guide them, user-friendly messages have been created.

*Log in confirmation message & new user guidance to create the first Task*

<img width="70%" alt="user friendliness" src="documentation_for_github_readme/user_messages_4.png">

The logged in user is redirected to the All Tasks page. In case the user has just registered or did not create any Tasks, a link is provided to do so.

*Log out confirmation message*

<img width="70%" alt="user friendliness" src="documentation_for_github_readme/user_messages_2.png">

The user is being informed about the log in / log out status to make sure their information is kept safe and private.

*No tasks and what to do about it message*

<img width="70%" alt="user friendliness" src="documentation_for_github_readme/user_messages.png">

In case the user has no Tasks within selected filter, a message is provided accordingly, to hint them what to do. This ensures a smoother website navigation and user experience.


:point_up_2: [Back to Contents](#contents)

## Features

### Homepage

The welcoming intorduction is visible to everyone, regardless of their log in status. This overview provides information about the application features and functionality. Sample screenshots show what to expect once registered and logged in.

<img width="70%" alt="welcome page" src="documentation_for_github_readme/welcoming_intro.jpg">

### Site Header and Log in

The site header contains Mom Schedule clickable logo that leads to the homepage.

<img width="70%" alt="welcome page" src="documentation_for_github_readme/header_and_login.jpg">

As well as the login status and greeting the user by their username. There is a dropdon button to log out of the application directly.

<img width="70%" alt="welcome page" src="documentation_for_github_readme/header_and_login_dropdown.jpg">

### Authentication and Authorization

The application provides an Authentication and Authorization mechanism by enabling the user to register a personal account. There are several pages that request authorized view, as well as authentication of the user account to be able to store individual data.

*Register and Log in*

<img width="45%" alt="login" src="documentation_for_github_readme/login_print_screen.jpg"> <img width="30%" alt="register" src="documentation_for_github_readme/register_print_screen.jpg">

:point_up_2: [Back to Contents](#contents)

### Site Navigation

In order to comfortably navigate through the tasks, homepage and contact the website administrators, a sidebar is available to the user. On the mobile view the navigation is floated to the top of the page, to maximize the application usability in frames of the limmited space on the phone screen.

#### Sidebar

The Sidebar includes: Homepage, Contact form, My Tasks and Filtering dropdown, including the Calendar view, New Task button.

#### My Tasks and Filter by Dropdown

Upon clicking the My Tasks dropdown, the user navigates through the Task filtering, the first of which is viewing all of the tasks.

*Sidebar dropdown with nested categories dropdown*

<img width="40%" alt="welcome page" src="documentation_for_github_readme/sidebar_dropdown.png"> <img width="40%" alt="welcome page" src="documentation_for_github_readme/sidebar_dropdown_categories.png">

*Filtering Tasks - Show all:*

<img width="70%" alt="filter tasks show all tasks" src="documentation_for_github_readme/all_tasks_print_screen.jpg">

*Filtering Tasks - Show Headlines on Calendar:*

<img width="70%" alt="filter tasks show calendar" src="documentation_for_github_readme/calendar_print_screen.jpg">

*Filtering Tasks - By due date (for urgency):*

<img width="70%" alt="filter tasks by dues date" src="documentation_for_github_readme/filter_by_due_date_print_screen.jpg">


### Contact Us

The user, regardless of their authentication status, is able to contact the website owner for questions and comments about the application.

<img width="50%" alt="contact form" src="documentation_for_github_readme/contact_form.png">


### New Task

This is the most important feature. The New Task form enables the user creating new tasks.

<img width="50%" alt="new task" src="documentation_for_github_readme/new_task_print_screen.jpg">


### Future Features

Some possible features will be considered for Mom Schedule upon request from the users:

- Week view
- Day view
- Mark start and end dates and show them as a span between the calendar dates
- Highlight today in the Calendar
- Show urgent deadlines (send notifications)

:point_up_2: [Back to Contents](#contents)

## Development Stages

### Planning

Initial planning has been conducted manually with pen and paper. Most of the features have been implemented in Mom Schedule project afterwards.

<img width="70%" alt="planning" src="documentation_for_github_readme/Planning_1.jpg">

The main database consisted of 3 Tables, necessary to create the data manipulation flow. These are Tasks, Categories and Users.

<img width="70%" alt="planning" src="documentation_for_github_readme/Planning_2.jpg">

### Structure

*PgSQL Relational Database Diagram*

<img width="100%" alt="wireframe" src="documentation_for_github_readme/wireframes/drawSQL-mom-schedule-database-diagram-export-2023-02-02.png">

#### Desktop Wireframes

*Today View, now All Tasks*

*Login / Register View, now in separate windows*

<img width="40%" alt="wireframe" src="documentation_for_github_readme/wireframes/mom-schedule-wireframe-desktop-today-view.png"> <img width="40%" alt="wireframe" src="documentation_for_github_readme/wireframes/mom-schedule-wireframe-desktop-register-login-view.png"> 

*Edit Task View*

*Initially 'This Week View', now Month's Calendar*

<img width="40%" alt="wireframe" src="documentation_for_github_readme/wireframes/mom-schedule-wireframe-desktop-task-edit.png"> <img width="40%" alt="wireframe" src="documentation_for_github_readme/wireframes/mom-schedule-wireframe-desktop-week-view.png">


### Using Frameworks and Libraries

The following frameworks have been acting as main tools for the application programming: 

- Django 
- PostgreSQL
- Bootstrap 5
- Cloudinary


### Using Source code

Some parts of the project have been created using sections of code from other sources. An example of this is the HTML calendar feature, that was partially taken from a repository: https://github.com/sajib1066/event-calendar , forked and adapted to the Mom Schedule project.

:point_up_2: [Back to Contents](#contents)

## Testing

### Validators

A short validation has been performed with Html and Css validators. Minor issues have been detected with Html. Css validation passed with no issues.

*HTML Validator*

<img width="70%" alt="html validator" src="documentation_for_github_readme/Html_validator_minor_errors.png"> 


*CSS Validator*

<img width="70%" alt="css validator" src="documentation_for_github_readme/CSS_validator_No errors.png"> 


### Manual Testing

In the browser by running the local server: **python3 manage.py runserver**

Two devices for responsivoty: a laptop and an iPhone 8.

A user experience walkthrough.

### Automatic Testing - Writing Functions

#### Test functions
Django’s unit tests use a Python standard library module: unittest. This module defines tests using a class-based approach.

In terminal: **python3 manage.py test**

Several test functions have been written and placed in files similar to the original, with the prefix 'test' to them (eg. test_forms.py, test_views.py).

*test_forms.py*

<img width="100%" alt="debugging" src="documentation_for_github_readme/test_forms.jpg"> 


#### Coverage

A coverage Html report has been generated to test the percentage of the code tested within the application.

*Coverage report*

<img width="70%" alt="debugging" src="documentation_for_github_readme/coverage_htmlcov.jpg"> 

The coverage report showed there are improvements to make in the following tests :

- test_models.py - tested 86%, so 14% was yet to be improved
- test_utils.py - tested 32%, so 68% was yet to be improved
- test_views.py - tested 32%, so 68% was yet to be improved


:point_up_2: [Back to Contents](#contents)

### Debugging

-------------------

:lady_beetle: - *Static files weren't included by Heroku after deployment.*

:bulb: - Using the WhiteNoise package fixed the issue.

*Before*

<img width="50%" alt="debugging" src="documentation_for_github_readme/static_css_heroku.jpg"> 

*After*

<img width="50%" alt="debugging" src="documentation_for_github_readme/static_css_local.jpg">

-----------------------------------------------------------------------------------


:lady_beetle: - *Title prepopulated with the first word only*


<img width="50%" alt="debugging" src="documentation_for_github_readme/title_bug_1.png"> 


*Before: The Task heading is prepopulated only partially. Instead of "Cleaning Chores" we see "Cleaning" only*



<img width="50%" alt="debugging" src="documentation_for_github_readme/title_bug_2.png"> 


:mag: {{ title }}

The title was going into the database as a 'the variable seen, the **first** value preserved' and being posted to the database as the first value that is true, ignoring the rest of the text.

<img width="50%" alt="debugging" src="documentation_for_github_readme/title_bug_reason.png"> 


:bulb: Changing to {{ 'title' }} as a string solved the problem and the database started storing the whole inner contents of that string, no matter how many words.

<img width="50%" alt="debugging" src="documentation_for_github_readme/title_bug_solution.png"> 


*After: The Task heading is now prepopulated completely as "Cleaning Chores".*


<img width="50%" alt="debugging" src="documentation_for_github_readme/title_bug_3.png">

-----------------------------------------------------------------------------------

:lady_beetle: - *Date Format*

having trouble with the date formats in Django. The HTML form has dd-mm-yyyy and Django has yyyy-mm-dd.
They somehow communicate to save the date correctly in the database but the problem occurs when I try editing one of my Tasks, by clicking the yellow edit button for a specific task on my all_tasks.html. 

It **did not prepopulate the date dropdown** and threw an error when trying to submit without choosing the date over again. However, editing inside the admin site worked well (it displayed yyyy-mm-dd).

<img width="50%" alt="debugging" src="documentation_for_github_readme/bug-date-admin.jpg"> <img width="50%" alt="debugging" src="documentation_for_github_readme/bug-date-admin-2.jpg">

<img width="50%" alt="debugging" src="documentation_for_github_readme/bug-date-admin-3.jpg"> <img width="50%" alt="debugging" src="documentation_for_github_readme/bug-date-admin-4.jpg">

:mag: - Tried solving by adding this code to settings.py: 

LANGUAGE_CODE = 'en-us'

USE_L10N = False

DATE_INPUT_FORMATS = ['%d-%m-%Y']

It did not work


:bulb: - found a solution:

Changed the date format in my edit function in views.py as follows:

...

date.strftime("%Y-%m-%d"),

Now it prepopulates my field with the date as dd-mm-yyyy. The mom_task is then saved without errors.

-----------------------------------------------------------------------------------

:lady_beetle: TestCase Bug


*Before: Got an error creating the test database: permission denied to create database*


<img width="70%" alt="debugging" src="documentation_for_github_readme/testing_database_bug.jpg"> 

:mag:  - Checking the current database settings in settings.py

<img width="70%" alt="debugging" src="documentation_for_github_readme/testing_database_bug_solution_1.jpg"> 

:bulb: - Temporarily activating the sqlite3 Django backends database fixed the issue.

<img width="70%" alt="debugging" src="documentation_for_github_readme/testing_database_bug_solution_2.jpg"> 

*After*

<img width="70%" alt="debugging" src="documentation_for_github_readme/testing_database_bug_solution_3.jpg"> 

### Remaining Issues

- Broken first two cards in Firefox Browser only
- Dropdown sidebar categories on Calendar page



:point_up_2: [Back to Contents](#contents)

## Deployment

The project is deployed to GitHub via Gitpod Terminal with an integrated VScode editor. Then it is connected to the Heroku app to be reached via a web browser for user convenience. To enable this, a special Code Institute template was cloned and used https://github.com/Code-Institute-Org/python-essentials-template .

The app is run in the backend terminal using **python3 manage.py runserver** and dependencies are placed in the requirements.txt file. The instruction on Heroku deployment was taken from the Code Institute Love Sandwiches walkthrough project, step by step as required.

### Creating the Heroku app

The project was deployed to Heroku as follows:

- Create an account and log in to https://www.heroku.com/
- Click 'New' from the dashboard, and from the drop-down menu select "Create new app"
- Make a unique app name: mom-data
- Choose a relevant geographical region, Europe
- Click "Create app"
- In the settings menu, go to "Config Vars" section
- Click "Reveal Config Vars", where dependencies are installed
- In "Deploy" tab, select Github as the deployment method
- Connect to GitHub
- Find the project repository and click "connect" next to it
- "Enable Automatic Deploys" for automatic deployment with every new change

## Tools

Wireframes: https://www.figma.com/

Bootstrap grid: https://getbootstrap.com/docs/4.1/layout/grid/

:point_up_2: [Back to Contents](#contents)

## Sources & Credits

### Sources
Writing and running tests in Django: https://docs.djangoproject.com/en/4.1/topics/testing/overview/

CSS tricks: https://css-tricks.com/snippets/css/a-guide-to-flexbox/#top-of-site

How to Create a Dropdown List in Django python: https://labpys.com/how-to-create-cascading-dependent-dropdown-list-in-django-python/?utm_content=cmp-true

Grid system: https://getbootstrap.com/docs/5.0/layout/grid/

Python Datetime: https://www.w3schools.com/python/python_datetime.asp

User Specific Pages: https://www.techwithtim.net/tutorials/django/user-specific-pages-data/

Setup Bootstrap messages for Django: https://ordinarycoders.com/blog/article/django-messages-framework

Django project base template: https://stackoverflow.com/questions/14720464/django-project-base-template#:~:text=Yes%2C%20you%20can%20use%20%7B%25,where%20to%20place%20the%20base.

A guide to user registration: https://ordinarycoders.com/blog/article/django-user-register-login-logout

Using WhiteNoise with Django: https://whitenoise.evans.io/en/stable/django.html

Django and Static Assets: https://devcenter.heroku.com/articles/django-assets?fbclid=IwAR16j_4bi-WEMxrA-VwWmFUfPOFP9ef2Kqzb6lM1pVCiKti_dhwoku1ceEg

Django models: https://docs.djangoproject.com/en/4.1/topics/db/models/

How to create a calendar with Django:  https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html

Event Calendar sample project and some source code: https://github.com/sajib1066/event-calendar

Develop a Simple Python Django ToDo App in 1 minute: https://dev.to/nditah/develop-a-simple-python-django-todo-app-in-1-minute-4908

### Acknowledgments

Richard Wells - the course mentor for friendly guidance, help with refactoring some code and numerous project feedback sessions

Jakob Lövhall - help with Python datetime formatting


:point_up_2: [Back to Contents](#contents)