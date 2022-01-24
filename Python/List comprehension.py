# Create a list comprehension that produces a list of the squares of the numbers ranging from 0 to 9.
squares = [i**2 for i in range(0, 10)]



# -----------------------------------------------------------
# Recreate this matrix by using nested listed comprehensions.
matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

matrix = [[col for col in range(5)] for row in range(5)]
for row in matrix:
    print(row)



# ------------------------------------------------------------------------------------------
# Using conditionals in comprehensions
# create a list that only includes the members of fellowship that have 7 characters or more.
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [member for member in fellowship if len(member) >= 7]
print(new_fellowship)



# ------------------------------------------------------------------------------------------------------------------
# Create a list that keeps members of fellowship with 7 or more characters and replaces others with an empty string. 
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

print(new_fellowship)



# -----------------------------------------------------------------------------------------------------------------------
# create a dictionary with the members of the list as the keys and the length of each string as the corresponding values.
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = {member : len(member) for member in fellowship}

print(new_fellowship)



# -------------------------------------------------------
# Generator expressions
# Create a generator object that produces numeric values.
result = (num for num in range(0,31))

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in range(4,31):
    print(value)



# -----------------------------------------------------------------------------------------
# Create a generator expression that will generate the lengths of each string in lannister.
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

lengths = (len(person) for person in lannister)

for value in lengths:
    print(value)



# ----------------------------
# Generator functions
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

def get_lengths (input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    for person in input_list:
        yield len(person)


for value in get_lengths(lannister):
    print(value)



# ------------------------------------------------
# List comprehensions for time-stamped data
# Extract the time from time-stamped Twitter data.

tweet_time = df['created_at']

tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

print(tweet_clock_time)
