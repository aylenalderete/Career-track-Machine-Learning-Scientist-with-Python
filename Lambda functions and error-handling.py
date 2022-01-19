# Convert a function that does a simple task into a lambda function.
def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words

#lambda function
echo_word = (lambda word1, echo: word1 * echo)

result = echo_word('hey', 5)
print(result)



# -------------------------------------------------------------------
# Use lambda functions to anonymously embed an operation within map()
spells = ["protego", "accio", "expecto patronum", "legilimens"]

shout_spells = map(lambda item: item + '!!!', spells)
shout_spells_list = list(shout_spells)

print(shout_spells_list)



# -----------------------------
# Filter() and lambda functions
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

result = filter(lambda member: len(member) > 6, fellowship)
result_list = list(result)

print(result_list)



# -----------------------------
# Reduce() and lambda functions
# Import reduce from functools
from functools import reduce

stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

result = reduce(lambda item1, item2: item1 + item2, stark)

print(result)



# -----------------------------
# Error handling with try-except
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')

    echo_word = ''
    shout_words = ''

    try:
        echo_word = word1 * echo
        shout_words = echo_word + '!!!'
    except:
        print("word1 must be a string and echo must be an integer.")
    return shout_words

shout_echo("particle", echo="accelerator")



# -----------------------------
# Working with a Twitter dataset
result = filter(lambda x: x[0:2] == 'RT' , tweets_df['text'])

res_list = list(result)

for tweet in res_list:
    print(tweet)