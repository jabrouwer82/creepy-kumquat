# This file contains helpful "tools" that other files can import and use
import logging
import webapp2

from google.appengine.api.taskqueue import TaskAlreadyExistsError, TombstonedTaskError
from google.appengine.ext import ndb

from mail import send_mail
from configuration import jinja_env

class Handler(webapp2.RequestHandler):

  def render_template(self, template_name, write=True, **contents):
    template = jinja_env.get_template(template_name)
    # Next we strip the .html off
    template_name = template_name.split('.')[0]
    contents['template'] = template_name
    if write:
      self.response.out.write(template.render(contents))
    else:
      return template.render(contents)

  def render_json(self, json_txt):
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(json_txt)

  def handle_exception(self, exception, debug_mode):
    # Send me an email, then continue with the eception as usual.
    send_mail('Exception in nexus checker', repr(exception))
    webapp2.RequestHandler.handle_exception(self, exception, debug_mode)
