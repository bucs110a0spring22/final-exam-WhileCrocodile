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
      number: (int) number of zoo animals to get (min 1 , max 10 animals)
    return:
      animals_json: (list) list of zoo animal information in json form
    '''
    if number >= 1 and number <= 10:
      url = self.api_url + f"/{number}"
    else:
      url = self.api_url + "/1"
    
    request = requests.get(url)
    animalsjson = request.json()

    return animalsjson

  def get_animal(self):
    '''
    Gets a single random animal's name.
    args:
      None
    return:
      animal: (str) name of animal retrieved
    '''
    animals_json = self.get()
    animal = animals_json[0]['name']
    return animal
    
  def get_animals(self, number=1):
    '''
    Gets a number of random animals, and adds them into a list.
    Can optionally specify how many zoo animals to get (min 1, max 10)
    args:
      number: (int) number of zoo animals to get (min 1 , max 10 animals)
    return:
      animalslist: (list) list of zoo animal names in plaintext
    '''
    animals_json = self.get(number)
    animals_list = []
    for animal_index in range(len(animals_json)):
      animals_list.append(animals_json[animal_index]['name'])

    return animals_list
    
  def __str__(self):
      return self.api_url