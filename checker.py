from urllib2 import urlopen
from utils import Handler
from models import Page
import urllib2
class Check(Handler):
  def check(self, source):
    data = urllib2.urlopen(source.url).read().decode('UTF-8')
    if data == source.prev_data:
      self.response.write('No change to file')
    else:
      self.response.write('Recent Changes to file.')

      for keyphrase in source.phrases.split(','):
        if keyphrase in data:
          self.response.write('{keyphrase} found in page.'.format(keyphrase=keyphrase))
        else:
          self.response.write('{keyphrase} not found in page.'.format(keyphrase=keyphrase))

  def get(self, ident):
    source = Page.fetch_by_name_or_key(ident)
    self.check(source)

