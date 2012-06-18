
import pprint
import webapp2
import jinja2
import os

from mydb import PyperDB

class Main(webapp2.RequestHandler):
    def get(self):
        td = os.path.join(os.getcwd(), 'temps')
        jinjadir = jinja2.Environment(loader=jinja2.FileSystemLoader(td))
        tem = jinjadir.get_template('form.template')
        items = {'items': ['a', 'b', 'c']}
        html = """ <h3> Webapp2 !!</h3>"""
        self.response.out.write(tem.render(items))

class Form(webapp2.RequestHandler):
    def post(self):  
        name = self.request.get('myname')
        msg = 'Welcome  ' + name 
        if name:
            uid = PyperDB(name=name, status=True, user_id=None)
            uid.put()
        self.response.out.write(msg)
        

mywebapp = webapp2.WSGIApplication([('/',Main), ('/sign', Form),])


def myapp(environ, start_response):
    response_headers = [('Content-type', 'text/html',)]
    msg = 'hi ! this is wsgi app'
    msg += pprint.pformat(environ)
    start_response('200 OK', response_headers)
    return [msg]
    
