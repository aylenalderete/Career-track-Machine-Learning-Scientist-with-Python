# Functions with one default argument
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    echo_word = echo * word1 
    shout_word = echo_word + '!!!'

    return shout_word

no_echo = shout_echo('Hey')
with_echo = shout_echo('Hey', 5)

print(no_echo)
print(with_echo)



# -----------------------------------------
# Functions with multiple default arguments
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    echo_word = word1 * echo

    if intense is True:
        echo_word_new = echo_word.upper() + '!!!'
    else:
        echo_word_new = echo_word + '!!!'
    return echo_word_new

with_big_echo = shout_echo('Hey', echo=5, intense=True)
big_no_echo = shout_echo('Hey', intense=True)

print(with_big_echo)
print(big_no_echo)



# ------------------------------------------------
# Functions with variable-length arguments (*args)
def gibberish(*args):
    """Concatenate strings in *args together."""

    hodgepodge = ''

    for word in args:
        hodgepodge += word
    return hodgepodge

one_word = gibberish('luke')
many_words = gibberish("luke", "leia", "han", "obi", "darth")

print(one_word)
print(many_words)



# -----------------------------------------------------------
# Functions with variable-length keyword arguments (**kwargs)
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    for key, value in kwargs.items():
        print(key + ": " + value)
    print("\nEND REPORT")

report_status(name='luke', affiliation='jedi', status='missing')
report_status(name='anakin', affiliation='sith lord', status='deceased')



# ------------------------
# Bringing it all together
# For this exercise, pandas has been imported as pd and the 'tweets.csv' file has been imported into the DataFrame tweets_df.
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    cols_count = {}
    col = df[col_name]
    
    for entry in col:
        if entry in cols_count.keys():
            cols_count[entry] += 1
        else:
            cols_count[entry] = 1
    return cols_count

result1 = count_entries(tweets_df)
result2 = count_entries(tweets_df, 'source')

print(result1)
print(result2)



# ------------------------
# Bringing it all together 2
# For this exercise, pandas has been imported as pd and the 'tweets.csv' file has been imported into the DataFrame tweets_df.
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    cols_count = {}

    for col_name in args:
        col = df[col_name]
    
        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
    return cols_count

result1 = count_entries(tweets_df, 'lang')
result2 = count_entries(tweets_df, 'lang', 'source')

print(result1)
print(result2)