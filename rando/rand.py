user_input = input("Enter your (yes/no) question: ")
import random 
random_response = ["Yes", "No", "Maybe", "I'ts doesnt matter", "You should be responsible for your choise"]

print("Answer on your question(",user_input  + ") is:" + " " + random.choice(random_response))
