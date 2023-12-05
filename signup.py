import datastore
import cookie_pw_handling
import main
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class SignupPage(main.BlogHandler):
    def get(self):
        self.render('signup.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        existing_user = datastore.User.all().filter('username =', username).get()
        if existing_user:
            error = 'Username is already taken! Please choose another.'
            self.render('signup.html', username=username, error=error)
        else:
            password_hash = cookie_pw_handling.make_pw_hash(username, password)

            new_user = datastore.User(username=username, password_hash=password_hash)
            new_user.put()

            self.login(new_user)
            self.redirect('/')



