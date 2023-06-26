# PM[] (Project Management)
* Based on **[Flask-Berry-Dashboard](https://github.com/app-generator/flask-berry-dashboard)**, go to the github page to get details of:
  * Original Flask Dashboard project
  * How to set up the environment  
  * How to start the app  
* Database: MySQL
* DB Tools: SQLAlchemy ORM, Flask-Migrate
* ECharts (For visualization)
* Bootstrap 5 (For UI)
* Develop with Pycharm originally
## 1 Set up environment
* ###  Using Conda with environment.yml to set up environment
```
conda env create -f environment.yml -n new_env
```
## 2 Important Tools
* #### [ECharts](https://echarts.apache.org/zh/index.html) for data visualization
* #### [Flask-SQLAlchemy](http://www.pythondoc.com/flask-sqlalchemy/) for database ORM
* #### [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) for database migrate
## 3 Modules
* ### Code-base structure
```bash
< PROJECT ROOT >
   |
   |-- apps/__init__.py
   |-- apps/
   |    |-- autentication/
   |    |    |-- forms.py                  # logic for login & register
   |    |    |-- models.py                 # model definition for Flask-SQLAlchemy
   |    |    |-- routes.py                 # logic for login & register
   |    |    |-- util.py                   # hash for password
   |    |
   |    |-- database/
   |    |    |-- query.py                  # basic database query 
   |    |    |-- models.py                 # pack up data for table&chart rendering
   |    |
   |    |-- home/
   |    |    |-- routes.py                 # view functions for web pages
   |    |
   |    |-- user/
   |    |    |-- routes.py                 # personal info page
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |    |-- assets/
   |    |    |    |-- js/
   |    |    |    |    |-- self-js/
   |    |    |    |    |    |-- <js>       # .js files of Core Functional Pages
   |    |-- templates/
   |         |-- my_pages/                 
   |         |    |-- <html>               # .html files of Core Functional Pages
   |         | 
   |         |-- includes/                 # Page chunks, components
   |         |    |
   |         |    |-- navigation.html      # Top bar
   |         |    |-- scripts.html         # JS scripts common to all pages
   |         |    |-- footer.html          # The common footer
   |         |
   |         |-- layouts/                  # App Layouts (the master pages)
   |         |    |
   |         |    |-- base.html            # Used by common pages like index, UI
   |         |
   |         |-- home/                     # UI Kit Pages
   |              |-- index.html           # default page
   |              |-- page-404.html        # 404 error page
   |              |-- *.html               # Used by common pages like index, UI
   |
   |-- requirements.txt
   |
   |-- run.py
   |
   |-- ************************************************************************
```
* ### Core Code
   * **apps/authentication/models.py**:  
   Definition of models used for intialization of database with **Flask-SQLAlchemy**. Refer to the official documentation of **Flask-SQLAlchemy & Flask-Migrate** for details.
   * **apps/database/prepare_dataset.py**:  
   Fetch data with functions defined in **query.py**, pack them up in the form that chart rendering requires, and return the dataset and metadata to view functions. 
   * **apps/home/routes.py**:
   Define routing functions for several pages.