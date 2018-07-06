# instantiates and assigns to variable
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# prints f-string assigned variable, x and y, and then strings seeded with x and y
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# instantiates and assigns to variable, boolean and a .format()-prompted string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# prints prompted .format()
print(joke_evaluation.format(hilarious))

# instantiates and assigns strings to variables
w = "This is the left side of..."
e = "a string with a right side."

# prints concatenated strings
print(w + e)


string = "This string right {}."
prompt = "here"
other_prompt = "there"

print(string.format(other_prompt))
