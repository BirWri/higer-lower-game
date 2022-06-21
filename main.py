# Choose 2 random from list
import random
import art
from game_data import data
#from replit import clear



def random_option():
  """Returns a random entry from the list """
  return random.choice(data)

def selection_a(option_a):
  a_name = option_a["name"]
  a_desc = option_a["description"]
  a_country = option_a["country"]

  print(f"Compare A:{a_name}, {a_desc}, from {a_country}.")

def selection_b(option_b):
  b_name = option_b["name"]
  b_desc = option_b["description"]
  b_country = option_b["country"]

  print(f"Against B:{b_name}, {b_desc}, from {b_country}.")

def retrieve_follower_count(data):
  follower_count = data["follower_count"]
  return follower_count

# Creates the first random option
option_a = random_option()

# Print Higher logo
print(art.logo)

# Players score
score = 0

game_on = True
while game_on:

  #Generates the second random option
  option_b = random_option()
  
  # Print first option
  selection_a(option_a)
  
  # Print vs logo
  print(art.vs)
  
  # Print second option
  selection_b(option_b)
  
  # Retrieve the followers amount for each option
  a = retrieve_follower_count(data = option_a)
  b = retrieve_follower_count(data = option_b)
  
  # Ask for user input
  user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # Clear the Terminal
  #clear()

  #Print logo again
  print(art.logo)

  # Validate if user chose corretly
  if user_guess == 'a':
    if a > b:
      score += 1
      #figure how to copy the dict to new name
      option_a = option_b.copy()
      print(f"You're right! Current score: {score}.")
    else:
        print(f"You lose. Your score: {score}")
        game_on = False     
  else:
      if b > a:
        score += 1
        option_a =option_b.copy()
        print(f"You're right! Current score: {score}.")
      else:
        print(f"You lose. Your score: {score}")
        game_on = False
  