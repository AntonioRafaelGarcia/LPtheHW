# imports the argv module from the sys library... I think that's the right phrasing
from sys import argv
# read the WYSS section for how to run this
script, first, second, third, last = argv # provides argument assignment framework for each

user_choice = input("""Something witty. Come on,
remember when you were clever?
Think way back to before you started that soul-sucking corporate job...
to before you willingly chose to trade 8 hours/day in a sterile office,
and 2 hours/day in commute for a salary that'll never pay your retirement...
back to the good ol' days, before commitments, before fugly spouses,
back to when you were COOL because you smoked cigarettes and fingered girls...
I know you still got it in you, just dig deep down into that pit you keep hiding from yourself
you useless, spineless faggot.""")

# prints string statements with appropriate argument inputs
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Last up:", last)
print("From the fag-child, this'll be good:", user_choice)
