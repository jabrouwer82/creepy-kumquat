from urllib2 import urlopen, URLERROR, 

class Check(Handler):
  def check(self, source):
    try:
      data = urllib2.urlopen(source.url).read().decode('UTF-8')
    except 
    if data == source.prev_data:
      self.response.write('No change to file')
