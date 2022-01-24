# Iterating over iterables
# Fun fact: the value 10**100 is actually what's called a Googol which is a 1 followed by a hundred 0s.
small_value = iter(range(3))

print(next(small_value))
print(next(small_value))
print(next(small_value))

for num in range(3):
    print(num)

googol = iter(range(10**100))

print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))



# --------------------------
# Using enumerate() function
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

mutant_list = list(enumerate(mutants))
print(mutant_list)

for index1, value1 in enumerate(mutants):
    print(index1, value1)


for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)



# ---------------------
# Using zip()
mutants = ['charles xavier', 'bobby drake', 'kurt wagner','max eisenhardt','kitty pryde' ]
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']

mutant_data = list(zip(mutants, aliases, powers))
print(mutant_data)

mutant_zip = zip(mutants, aliases, powers)
print(mutant_zip)

for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)



# --------------------------
# Using * and zip to 'unzip'
z1 = zip(mutants, powers)
print(*z1)

# 'Unzip' the tuples in z1 by unpacking with * and zip()
z1 = zip(mutants, powers)
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)



# ----------------------------------------
# Extracting information for large amounts of Twitter data
# The file 'tweets.csv' is in the current directory of DataCamp.
import pandas as pd

def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    counts_dict = {}

    for chunk in pd.read_csv(csv_file, chunksize=c_size):
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    return counts_dict

result_counts = count_entries('tweets.csv', 10, 'lang')
print(result_counts)
