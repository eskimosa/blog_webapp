import models
import cookie_pw_handling
from handlers.handlers import BlogHandler
import os
import jinja2


template_dir = os.path.join(os.path.dirname('/Users/jenya/Desktop/becoming_full_stack/web_development/projects_udacity_course/my_project_blog/templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class LoginPage(BlogHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        user = models.User.get_by_username(username)
        if user and cookie_pw_handling.make_pw_hash(username, password) == user.password_hash:
            self.set_secure_cookie('user_id', str(models.User.user_id))
            self.redirect('/')
        else:
            error = 'Invalid login'
            self.render('login.html', username=username, error=error)

