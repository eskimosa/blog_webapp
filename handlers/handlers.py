import webapp2
import jinja2
import os
import cookie_pw_handling
import models

template_dir = '/Users/jenya/Desktop/becoming_full_stack/web_development/projects_udacity_course/my_project_blog/templates'
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, value):
        cookie_val = cookie_pw_handling.make_secure_val(value)
        self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and cookie_pw_handling.check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.user_id))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        user_from_db = models.session.query(models.User).filter_by(user_id=str(uid)).first()
        self.user = uid and user_from_db


def render_post(response, post):
    response.out.write('<b>' + post.subject + '</b><br>')
    response.out.write(post.content)
