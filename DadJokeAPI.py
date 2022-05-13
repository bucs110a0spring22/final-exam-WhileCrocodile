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

  def __str__(self):
    return self.api_url
    
    
    