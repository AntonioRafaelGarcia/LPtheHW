from sys import argv

script, user_name, dick_game = argv
prompt = ':{)} '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"Hmmm, looks like your dick game is awfully {dick_game}. Guess that makes one of us.")


print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
You have a {computer} computer. Nice.
Lastly, dick game is {dick_game}. ::crickets::
""")
