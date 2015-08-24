form webapp2 import WSGIApplication, Route

app = webapp2.WSGIApplication([
    Route('/sources',
          handler='sources.SourcesList',
          name='sources'),
    Route('/source/new',
          handler='sources.Sources',
          name='sources-new'),
    Route('/source/<ident>',
          handler='sources.Sources',
          name='source-edit'),
    Route('/check/<ident>',
          handler='checker.Check',
          name='check'),
    Route('/checkall',
          handler='checker.CheckAll',
          name='check-all')
], debug=True)
