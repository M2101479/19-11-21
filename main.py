import random
import string
from random import randint

Team={
  'See':'Rock',
  'Dock': 'Red',
  'Not':'Fort',
  'Hat':'Pat',
}


print(Team.get('See'))


thing=random.choice(list(Team.values()))
print(thing)

def random_string(length):
  result = ''.join((random.choice(string.ascii_lowercase)for x in range (length)))
  return result

print(random_string(29))

def generate_dict():
  for i in range (10):
     print("'" + random_string(random.randint(1,10)) + "': '" + random_string(random.randint(1,10)) + "'")

generate_dict()




 
