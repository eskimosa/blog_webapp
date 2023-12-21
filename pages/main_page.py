import models
from handlers.handlers import BlogHandler
import os
import jinja2


template_dir = '/Users/jenya/Desktop/becoming_full_stack/web_development/projects_udacity_course/my_project_blog/templates'
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class MainPage(BlogHandler):
    def get(self):
        if self.user:
            posts = models.BlogPost.get_all(self.user.user_id)
            self.render('front.html', user=self.user, posts=posts)
        else:
            self.redirect('/login')

