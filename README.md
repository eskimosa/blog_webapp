Intro
--

This repository contains a simple blog web application built using Python and the webapp2 framework. The application includes features such as user authentication, posting and viewing blog entries.

This project marks the culmination of the Udacity Web Development course guided by the creator of Reddit where I delved into Google App Engine, explored webapp2 and got hands-on with Jinja templating

Project Structure
--

1. main.py: The main entry point of the web application. It configures the webapp2 framework to handle different routes and starts the server.

2. cookie_pw_handling.py: Contains functions for hashing and handling user passwords securely.

3. models.py: Defines the data models using SQLAlchemy for users and blog posts.

4. handlers.py: Contains a base handler class that other handlers inherit from.

5. pages/: This directory includes additional pages and components used in the web application.

6. templates/: This directory includes HTML templates used for rendering pages.  

Requirements
--

```shell
$ cat requirements.txt
webapp2==2.5.2
WebOb==1.8.7
Paste==3.6.1
Jinja2==2.11.3
SQLAlchemy==1.4.50
```

Setup
--

1. Create '.env' file in the same directory as your scripts.
2. Add a path to your 'templates' directory and configure jinja environment, add a SECRET key for hashing:
```shell
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

SECRET = 'your_secret_key'
```
3. Install the required packages:
```shell
$ virtualenv venv
$ venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Running the Scripts
--
```shell
$ python2 main.py # webapp2 doesn't support Python version above 2.7
```

Please adjust any paths or formatting to match your actual file structure and preferences.

Author
--

[eskimosa](https://github.com/eskimosa/)
