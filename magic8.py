import random

name = "Tyler"
question = "Will I learn to fly?"
answer = ""

random_number = random.randint(1, 13)
# print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Why, it's happening as we speak!"
elif random_number == 11:
  answer = "Ask again, in a friendly tone of voice please"
elif random_number == 12:
  answer = "It seems so, yes"
elif random_number == 13:
  answer = "Absolutely not"
else:
  answer = "Error"

# print question
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

if question == "":
  print("You did not ask a question. Please try again.")
else:
  print("Magic 8-Ball's answer: " + answer)
