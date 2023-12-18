import models
import main
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class NewPost(main.BlogHandler):
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
                p = models.BlogPost(subject=subject, content=content)
                p.put()
                self.redirect('/')
            else:
                error = "Please add subject and content!"
                self.render('newpost.html', subject=subject, content=content, error=error)
        else:
            self.redirect('/login')

