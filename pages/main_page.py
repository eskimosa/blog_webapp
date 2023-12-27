import models
from handlers.handlers import BlogHandler


class MainPage(BlogHandler):
    def get(self):
        if self.user:
            posts = models.BlogPost.get_all(self.user.user_id).order_by(models.BlogPost.created.desc())
            self.render('front.html', user=self.user, posts=posts)
        else:
            self.redirect('/login')

