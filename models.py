from base_model import BaseModel
from google.appengine.ext import ndb

class Page(BaseModel):
  '''Models a page to check, including what to expect on the page.'''

  name = ndb.StringProperty(default='')
  url = ndb.StringProperty(default='')
  phrases = ndb.StringProperty(default='')
  prev_data = ndb.TextProperty(default='')
  update = ndb.IntegerProperty(default=0)
  major_update = ndb.IntegerProperty(default=0)
