import requests

class DadJokeAPI:
  def __init__(self):
    '''
    Initializes the DadJokeAPI handler with a url.
    args:
      None
    return:
      None
    '''
    self.api_url = "https://icanhazdadjoke.com"

  def get(self, id=None):
    '''
    Gets a dad joke json. Gets a specific dad joke json if an ID is specified.
    
    args:
      id: (str) an 11 character alphanumeric id corresponding to
      a specific dad joke
    return:
      jokejson: (dict) returns a dad joke as a dictionary
    '''
    headers = {"Accept": "application/json"}

    if id:
      url = self.api_url + f"/j/{id}"
    else:
      url = self.api_url
      
    request = requests.get(url, headers=headers)
    jokejson = request.json()
  
    return jokejson

  def get_joke(self, id=None):
    '''
    Gets a single dad joke in plaintext. Gets a specific dad joke if an ID
    is specified.
    '''
    jokejson = self.get(id)
    joke = jokejson['joke']
  
    return joke

  def __str__(self):
    '''
    Returns the url of the api used.
    args:
      None
    return:
      self.api_url: (str) url of api used
    '''
    return self.api_url
    
    
    