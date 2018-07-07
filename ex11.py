# prints question string, followed by prompt assignments for answers
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

# f prints string with prompt-assigned variable answers
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("Let's continue. What self-incriminating at the felony level are you willing to disclose?")
outstanding_felonies = input()
print(f"{outstanding_felonies}... sounds serious. Backing away now...")
