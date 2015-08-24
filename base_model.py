from google.appengine.ext import ndb

class BaseModel(ndb.Model):
  @classmethod
  def fetch_by_name(cls, name):
    '''Attempts to fetch the given model by its name property.

    Args:
      cls (class): The name of the model class to query.
      name (str): The name of the model.

    Returns:
      Model: If a model with the property 'name'==<name> is found.
      None: If no model is found.
    '''
    item = cls.query(cls.name == name).get()
    return item

  @classmethod
  def fetch_by_key(cls, url_key):
    '''Attempts to fetch the given model by its url-safe key.

    Args:
      cls (class): The name of the model class to query.
      url_key (str): The url encoded key.

    Returns:
      Model: If a model with the matching key is found.
      None: If no model is found.
    '''
    key = ndb.Key(urlsafe=url_key)
    item = key.get()
    return item

  @classmethod
  def fetch_by_name_or_key(cls, ident):
    '''Attempts to fetch the given model by its name property or by url-safe key.

    Attempts to fetch by name first, then key.

    Args:
      cls (class): The name of the model class to query.
      ident (str): The name or key of the model.

    Returns:
      Model: If a model with the property 'name'==<name> or matching key is found.
      None: If no model is found.
    '''
    item = cls.fetch_by_name(ident)
    if not item:
      item = cls.fetch_by_key(ident)
    return item

  @classmethod
  def fetch_by_key_or_name(cls, ident):
    '''Attempts to fetch the given model by its url-safe key or by its name property.

    Attempts to fetch by key first, then name.

    Args:
      cls (class): The name of the model class to query.
      ident (str): The name or key of the model.

    Returns:
      Model: If a model with the matching key or property 'name'==<name> is found.
      None: If no model is found.
    '''
    item = cls.fetch_by_key(ident)
    if not item:
      item = cls.fetch_by_name(ident)
    return item

