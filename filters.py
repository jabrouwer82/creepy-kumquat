'''Every function in this module is auto-imported to the jinja environment as filters.
'''
import webapp2

def uri(*args, **kwargs):
  '''Uses webapp2 named routes to build a uri for the given data.
  
  Args:
    *args: Argument list passed directly to uri_for.
    **kwargs: Keyword arguments passed directly to uri_for.
  
  Returns:
    str: A webapp2-built uri.
  '''
  return webapp2.uri_for(*args, **kwargs)
