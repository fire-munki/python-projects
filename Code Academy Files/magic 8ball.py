import random

#variables
name = "Matt"
question = "Will I win a world cup race?"
answer = ""
random_number = random.randint(1,11)

#testing random number generation
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "My sources say no."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
 answer = "Never in a month of Sundays."
elif random_number == 11:
 answer = "Tomorrow - getting racing now!."
else:
  answer = "Error"

#dealing with empty name and question variables
if question == "":
  print("Magic 8-Ball's needs a question to help you", name)
elif name == "" and not question == "":
  print(question)
  print("Magic 8-Ball's answer:",answer)
elif not name == "" and not question == "":
  print(name, "asks:", question)
  print("Magic 8-Ball's answer:",answer)
