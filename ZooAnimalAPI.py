import requests

class ZooAnimalAPI:
  def __init__(self):
    '''
    Initializes the ZooAnimalAPI handler with a url.
    args:
      None
    return:
      None
    '''
    self.api_url = "https://zoo-animal-api.herokuapp.com/animals/rand"

  def get(self, number=1):
    '''
    Gets information about a zoo animal in the form of jsons in a list.
    Can optionally specify how many zoo animals to get (min 1, max 10)
    args:
      number: (int) number of zoo animals to get; min 1 animal, max 10 animals
    return:
      animalsjson: (list) list of zoo animal information in json form
    '''
    if number >= 1 and number <= 10:
      url = self.api_url + f"/{number}"
    else:
      url = self.api_url + "/1"
    
    request = requests.get(url)
    animalsjson = request.json()

    return animalsjson

  def __str__(self):
    return self.api_url

    
    
    
    