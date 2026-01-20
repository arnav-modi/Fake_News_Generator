import random

def load_data(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()

subjects = load_data("subject.txt")
actions = load_data("action.txt")
Places_or_things = load_data("place_or_thing.txt")

while True:  
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(Places_or_things)


    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\n Do you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

print("\n Thankyou for using the Fake News Headline Generator. Have a fun day")    