import models
import cookie_pw_handling
from handlers.handlers import BlogHandler
import os
import jinja2

template_dir = '/Users/jenya/Desktop/becoming_full_stack/web_development/projects_udacity_course/my_project_blog/templates'
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class SignupPage(BlogHandler):
    def get(self):
        self.render('signup.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        existing_user = models.User.get_by_username(username)
        if existing_user:
            error = 'Username is already taken! Please choose another.'
            self.render('signup.html', username=username, error=error)
        else:
            password_hash = cookie_pw_handling.make_pw_hash(username, password)

            new_user = models.User.create_user(models.User.session, username, password_hash)

            self.login(new_user)
            self.redirect('/')



