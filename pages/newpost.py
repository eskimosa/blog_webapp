import models
from handlers.handlers import BlogHandler
import os
import jinja2


template_dir = '/Users/jenya/Desktop/becoming_full_stack/web_development/projects_udacity_course/my_project_blog/templates'
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class NewPost(BlogHandler):
    def get(self):
        if self.user:
            self.render('newpost.html')
        else:
            self.redirect('/login')

    def post(self):
        if self.user:
            subject = self.request.get('subject')
            content = self.request.get('content')

            if subject and content:
                models.BlogPost.create_post(models.BlogPost.session, subject, content)
                self.redirect('/')
            else:
                error = "Please add subject and content!"
                self.render('newpost.html', subject=subject, content=content, error=error)
        else:
            self.redirect('/login')

