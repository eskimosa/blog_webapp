import models
import cookie_pw_handling
import main
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class LoginPage(main.BlogHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        user = models.User.all().filter('username =', username).get()
        if user and cookie_pw_handling.make_pw_hash(username, password) == user.password_hash:
            self.set_secure_cookie('user_id', str(user.key().id()))
            self.redirect('/')
        else:
            error = 'Invalid login'
            self.render('login.html', username=username, error=error)

