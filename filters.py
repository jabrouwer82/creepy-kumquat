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

def divided_by_rate(count):
  '''Divides the number of updates by the rpm to determine minute count.

  Args:
    count: Number of updates since the source changed.

  Returns:
    int: The number of minutes since the source changed.
  '''
  rpm = 2
  return count / rpm
