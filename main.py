import os
import random
#Beginning of the chat
print("Welcome to my chatbot")

def chatbox_response(user_input):
  responses = [
    "Really, that's unique", 
    "That's interesting", 
    "I wouldn't have guessed.",
    "Me too! I like it as well.", 
  ]
  return random.choice(responses) 

def chatbox_question(user_input):
  responses = [
    "What are your hobbies?"
    "What's your favorite science subject?",
    "Do you think that free time is something that happens   or you make happen?",
    "What's your favorite book genre?", 
    "What's your favorite movie?",
    "Do you think processes that are thought as stressful can be joyful?", 
    "What is your favorite teacher like?", 
    "Do you think that a strict teacher or a more at ease teacher is better?",
    "How do you think people can be successful?",
    "What are your favorite organizations systems?",
    "What are the most random things that are weird that you have either a habit of or have done once or a few times?"
    
  ]
  return random.choice(responses)
  
def init_chat():
  exit_chat = "Bye"

  user_input = input("What motivates you to work hard?\n")

  while user_input != exit_chat:
    user_input = input(chatbox_question(user_input) + "\n")
    if user_input != exit_chat:
      print(chatbox_response(user_input) + "\n")
    else: 
      print("See you later then")

if __name__ == "__main__":
  init_chat()