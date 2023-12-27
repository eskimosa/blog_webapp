import webapp2
from paste import httpserver
from paste.cascade import Cascade
from paste.urlparser import StaticURLParser

from pages.newpost import NewPost
from pages.login import LoginPage
from pages.main_page import MainPage
from pages.signup import SignupPage
from pages.logout import Logout


web_app = webapp2.WSGIApplication([('/', MainPage),
                               ('/login', LoginPage),
                               ('/newpost', NewPost),
                               ('/signup', SignupPage),
                               ('/logout', Logout)
                               ], debug=True)

static_app = StaticURLParser("static")
app = Cascade([static_app, web_app])


def main():
    httpserver.serve(app, host='127.0.0.1', port='8081')


if __name__ == '__main__':
    main()
