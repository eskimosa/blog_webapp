import models
from handlers.handlers import BlogHandler


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
                models.BlogPost.create_post(subject, content, self.user.user_id)
                self.redirect('/')
            else:
                error = "Please add subject and content!"
                self.render('newpost.html', subject=subject, content=content, error=error)
        else:
            self.redirect('/login')

