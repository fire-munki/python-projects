#Lesson 8

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

guess = int(raw_input("Your guess: "))

while guesses_left < 4:
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "You lose."


#Lesson 10

for i in range(3):
  hobby = raw_input("Your hobby is: ")
  hobbies.append(hobby)
    
print hobbies


