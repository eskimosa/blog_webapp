import models
import cookie_pw_handling
from handlers.handlers import BlogHandler
import jinja2


template_dir = '/Users/jenya/Desktop/becoming_full_stack/web_development/projects_udacity_course/my_project_blog/templates'
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class LoginPage(BlogHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        db_user = models.User.get_by_username(username)
        valid_password = self._is_valid_password(db_user, username, password)
        if valid_password:
            self.set_secure_cookie('user_id', str(db_user.user_id))
            self.redirect('/')
        else:
            error = 'Invalid login'
            self.render('login.html', username=username, error=error)

    @staticmethod
    def _is_valid_password(db_user, username, password):
        if not db_user:
            return False
        salt = db_user.password_hash.split(',')[1]
        db_user_pwd_hash = cookie_pw_handling.make_pw_hash(username, password, salt)
        return db_user_pwd_hash == db_user.password_hash
