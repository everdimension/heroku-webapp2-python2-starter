import webapp2

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, webapp2, heroku and python 2!')

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)
