import webapp2

from pages.newpost import NewPost
from pages.login import LoginPage
from pages.main_page import MainPage
from pages.signup import SignupPage


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/login', LoginPage),
                               ('/newpost', NewPost),
                               ('/signup', SignupPage),
                               ], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()