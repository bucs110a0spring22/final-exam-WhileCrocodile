import requests
import random

class FruitAPI:
  def __init__(self):
      self.api_url = "https://www.fruityvice.com/api/fruit/all"

  def get(self):
    '''
    Gets the full list of fruit information in json.
    args:
      None
    return:
      fruitsjson: (dict) dictionary of fruits and associated information
    '''
    request = requests.get(self.api_url)
    fruitsjson = request.json()
    return fruitsjson

  def random_fruit(self):
    '''
    Picks a single random fruit.
    args:
      None
    return:
      randomfruit: (str) the name of a random fruit
    '''
    fruitsjson = self.get()
    fruit_index = random.randrange(len(fruitsjson))
    randomfruit = fruitsjson[fruit_index]['name']
    return randomfruit

  def fruits_list(self, number):
    '''
    Creates a list of random fruit names.
    args:
      number: (int) how many fruits to include in the list
    return:
      fruits_list: (list) list of random fruits
    '''
    fruitsjson = self.get()
    fruits_list = []
    for iterations in range(number):
      fruit_index = random.randrange(len(fruitsjson))
      fruit = fruitsjson[fruit_index]['name']
      fruits_list.append(fruit)
    return fruits_list
    