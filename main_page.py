import datastore
import main
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class MainPage(main.BlogHandler):
    def get(self):
        if self.user:
            posts = datastore.BlogPost.all().order('-created')
            self.render('front.html', posts=posts)
        else:
            self.redirect('/login')

