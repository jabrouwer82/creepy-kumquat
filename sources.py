from mail import send_mail
from models import Page
from utils import Handler

class Source(Handler):
  def get(self, ident=None):
    if ident:
      source = Page.fetch_by_name_or_key(ident)

    if not ident or not source:
      source = Page()

    self.render_template('source.html', source=source)

  def post(self, ident=None):
    if ident:
      source = Page.fetch_by_key(ident)
    else:
      source = Page()

    source.name = self.request.get('name', '')
    source.url = self.request.get('url', '')
    source.phrases = self.request.get('phrases', '')
    key = source.put()
    self.response.write(key.urlsafe())

class SourceList(handler):
  def get(self):
    sources = Page.query().fetch()
    self.render_template('sources.html', sources=sources)

class SourceDelete(handler):
  def get(self, ident):
    source = Page.fetch_by_key(ident)
    source.key.delete()
    subject = 'Deleted {page} from datastore'.format(page=source.name)
    html_message = self.render_template('delete_email.html', write=False, item=source)
    send_mail(subject, html=html_message)
    self.response.write(html_message)
