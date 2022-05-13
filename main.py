import src.DadJokeAPI as DadJokeAPI
import src.ZooAnimalAPI as ZooAnimalAPI
import src.FruitAPI as FruitAPI
import random
import json

def animal_joke(jokecount=1):
  '''
  Generates a string of animals telling dad jokes.
  args:
    jokecount: (int) number of jokes to tell
  return:
    animaljoke: (str) jokes made by animals
  '''
  jokeapi = DadJokeAPI.DadJokeAPI()
  animalapi = ZooAnimalAPI.ZooAnimalAPI()

  # gets animal information as one request rather than multiple,
  # for speed and less resource utilization
  # dad jokes still have to be requested multiple times
  animaljoke = ""
  animallist = animalapi.get_animals(jokecount)
  for count in range(jokecount):
    animal = animallist[count]
    joke = jokeapi.get_joke()
    animaljoke += f"\n{animal} says:\n{joke}\n"
  return animaljoke

def animal_battle(fights=1):
  '''
  Simulates many fights between many different animals.
  args:
    fights: (int) number of fights to simulate
  return:
    fight_log: (string) record of simulated battles
  '''
  animalapi = ZooAnimalAPI.ZooAnimalAPI()
  battle_descriptors = open("etc/battle_descriptors.txt", "r")
  descriptors_list = json.load(battle_descriptors)
  
  fight_log = ""
  for i in range(fights):
    descriptor = random.choice(descriptors_list)
    animaljson = animalapi.get_animals(2)
    animal_one = animaljson[0]
    animal_two = animaljson[1]
    if random.randrange(2):
      fight_log += f"{animal_one} {descriptor} {animal_two}!\n"
    else:
      fight_log += f"{animal_one} was {descriptor} by {animal_two}!\n"
    
  return fight_log

def animal_duel(rounds=5):
  '''
  Simulates many rounds of fighting between 2 animals.
  args:
    rounds: (int) number of rounds to simulate
  return:
    fight_log = (string) record of simulated rounds
    winner = (string) animal that won the most rounds
    fight_log, winner = (tuple) a tuple of the previous 2 strings
  '''
  animalapi = ZooAnimalAPI.ZooAnimalAPI()
  battle_descriptors = open("etc/battle_descriptors.txt", "r")
  descriptors_list = json.load(battle_descriptors)
  battle_descriptors.close()

  animaljson = animalapi.get_animals(2)
  animal_one = animaljson[0]
  animal_two = animaljson[1]

  one_score = 0
  two_score = 0

  fight_log = ""
  for i in range(rounds):
    descriptor = random.choice(descriptors_list)
    if random.randrange(2):
      fight_log += f"{animal_one} {descriptor} {animal_two}!\n"
      one_score += 1
    else:
      fight_log += f"{animal_two} {descriptor} {animal_one}!\n"
      two_score += 1

  if one_score == two_score:
    winner = "Tie"
  elif one_score > two_score:
    winner = animal_one
  else:
    winner = animal_two
  
  return fight_log, winner

def animal_fruit(fruits=1):
    '''
    Determines if an animal would like a number of fruits.
    args:
      fruits: (int) number of fruits to consider
    return:
      animal_response: (str) animal responses to fruit
    '''
    animalapi = ZooAnimalAPI.ZooAnimalAPI()
    fruitapi = FruitAPI.FruitAPI()
    animal = animalapi.get_animal()
    fruits_list = fruitapi.fruits_list(fruits)
    animal_responses = open("etc/animal_responses.txt", "r")
    responses_list = json.load(animal_responses)
    animal_responses.close()
    animal_response = ""
    
    for fruit in fruits_list:
      response = random.choice(responses_list)
      animal_response += f"{animal} {response} {fruit}!\n"

    return animal_response

def main():
    ##### Joke Generator #####
    print("/ / / / / Joke Generator / / / / /")
    numjokes = input("How many jokes would you like (min 1, max 10)?\n")
    # checks if numjokes is a number; if it is, converts
    # it into an int, then checks if it's between 0 and 10
    while not numjokes.isnumeric() or (int(numjokes) not in range(0, 11)):
      numjokes = input("Invalid input. How many jokes would you like (min 1, max 10)?\n")
    numjokes = int(numjokes)
    joke = animal_joke(jokecount=numjokes)
    print(joke)
  
    ##### Battle Generator #####
    print("/ / / / / Battle Generator / / / / /")
    numfights = input("How many fights would you like to simulate?\n")
    while not numfights.isnumeric():
      numfights = input("Invalid input. How many fights would you like to simulate?\n")
    numfights = int(numfights)
    print(animal_battle(fights=numfights))

    ##### Duel Generator #####
    print("/ / / / / Duel Generator / / / / /")
    numduels = input("How many duels would you like to simulate?\n")
    while not numduels.isnumeric():
      numduels = input("Invalid input. How many fights would you like to simulate?\n")
    numduels = int(numduels)
    duel, winner = animal_duel(rounds=numduels)
    print(duel)
    print(f"Winner: {winner}\n")
  
    ##### Fruit Response Generator #####
    print("/ / / / / Fruit Response Generator / / / / /")
    numfruit = input("How many fruits would you like the animal to consider?\n")
    while not numfruit.isnumeric():
      numfruit = input("Invalid input. How many fruit would you like the animal to consider?\n")
    numfruit = int(numfruit)
    print(animal_fruit(numfruit))
  

if __name__ == "__main__":
    main()