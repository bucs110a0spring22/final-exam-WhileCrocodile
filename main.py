import DadJokeAPI
import ZooAnimalAPI
import random

def animal_joke(jokecount=1):
  '''
  Generates a string of animals telling dad jokes.
  args:
    jokecount: (int) number of jokes to tell
  return:
    None
  '''
  jokeapi = DadJokeAPI.DadJokeAPI()
  animalapi = ZooAnimalAPI.ZooAnimalAPI()

  # gets animal information as one request rather than multiple,
  # for speed and less resource utilization
  # dad jokes still have to be requested multiple times
  animaljoke = ""
  animaljson = animalapi.get(jokecount)
  for count in range(jokecount):
    animal = animaljson[count]["name"]
    jokejson = jokeapi.get()
    joke = jokejson["joke"]
    animaljoke += f"\n{animal} says:\n{joke}\n"
  return animaljoke

def animal_battle(fights=1):
  '''
  Determines who would win a fight between two animals.
  args:
    None
  return:
    fight_log: (string) Record of animal wins/losses
  '''
  animalapi = ZooAnimalAPI.ZooAnimalAPI()

  fight_log = ""
  for i in range(fights):
    animaljson = animalapi.get(2)
    animal_one = animaljson[0]["name"]
    animal_two = animaljson[1]["name"]
    if random.randrange(2):
      fight_log += f"{animal_one} won against {animal_two}!\n"
    else:
      fight_log += f"{animal_one} lost to {animal_two}!\n"
  
  return fight_log

def main():
  ##### Joke Generator #####
  
  numjokes = input("How many jokes would you like (min 1, max 10)?\n")
  # checks if numjokes is a number; if it is, converts
  # it into an int, then checks if it's between 0 and 10
  while not numjokes.isnumeric() or (int(numjokes) not in range(0, 11)):
    numjokes = input("Invalid input. How many jokes would you like (min 1, max 10)?\n")
  numjokes = int(numjokes)
  joke = animal_joke(jokecount=numjokes)
  print(joke)
  
  ##### Joke Generator #####

  ##### Fight Generator #####
  numfights = input("How many fights would you like to simulate?\n")
  while not numfights.isnumeric():
    numfights = input("Invalid input. How many fights would you like to simulate?\n")
  numfights = int(numfights)
  print(animal_battle(fights=numfights))
  ##### Fight Generator #####
  

if __name__ == "__main__":
  main()