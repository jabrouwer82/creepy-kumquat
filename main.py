from webapp2 import WSGIApplication, Route

app = WSGIApplication([
    Route('/',
          handler='sources.SourceList',
          name='home'),
    Route('/sources',
          handler='sources.SourceList',
          name='sources'),
    Route('/source/new',
          handler='sources.Source',
          name='source-new'),
    Route('/source/<ident>',
          handler='sources.Source',
          name='source-edit'),
    Route('source/delete/<ident>',
          handler='sources.SourceDelete',
          name='source-delete'),
    Route('/check/<ident>',
          handler='checker.Check',
          name='check'),
    Route('/checkall',
          handler='checker.CheckAll',
          name='check-all')
], debug=True)
