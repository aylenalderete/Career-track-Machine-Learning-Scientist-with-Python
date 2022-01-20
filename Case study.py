
# CASE STUDY
# These lists are actually extracted from a bigger dataset file of world development indicators from the World Bank.
# For pedagogical purposes, we have pre-processed this dataset into the lists that you'll be working with -Datacamp.

# feature_names contains the header names of the World Bank dataset 
# and row_lists is a list of lists, where each sublist is a list of actual values of a row from the dataset.

def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    zipped_lists = zip(list1, list2)
    rs_dict = dict(zipped_lists)

    return rs_dict

rs_fxn = lists2dict(feature_names, row_vals)
print(rs_fxn)


#-------------------------------------------


print(row_lists[0])
print(row_lists[1])

list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

print(list_of_dicts[0])
print(list_of_dicts[1])



# ---------------------------------------------------------
# Convert the list of dictionaries into a pandas DataFrame.
# The lists2dict() function, feature_names list, and row_lists list have been preloaded for this exercise.
import pandas as pd

list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

df = pd.DataFrame(list_of_dicts)

print(df.head())



# -------------------------
# Processing data in chunks
# process the first 1000 rows of a file line by line,
# to create a dictionary of the counts of how 
# many times each country appears in a column in the dataset.
# The csv file 'world_dev_ind.csv' is in the current directory(DataCamp).
with open('world_dev_ind.csv') as file:

    file.readline()

    counts_dict = {}

    for j in range(0, 1000):
        line = file.readline().split(',')
        first_col = line[0]
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

print(counts_dict)



# ------------------------------------------
# Writing a generator to load data in chunks
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

with open('world_dev_ind.csv') as file:
    gen_file = read_large_file(file)

    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

# Now let's use the generator function to process the World Bank dataset
counts_dict = {}

with open('world_dev_ind.csv') as file:

    for line in read_large_file(file):
        row = line.split(',')
        first_col = row[0]
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

print(counts_dict)



# ------------------------------------------------------------------------------------------------------
# Read a file in small DataFrame chunks with read_csv().
# 'ind_pop.csv' is available to look at the urban population indicator for numerous countries and years.
import pandas as pd

df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

print(next(df_reader))
print(next(df_reader))



# --------------------------------------------------------------------------------
# Create another DataFrame composed of only the rows from a specific country. 
# Zip together two of the columns from the new DataFrame, 'Total Population'
# and 'Urban population (% of total)'. Finally, create a list of tuples from the 
# zip object, where each tuple is composed of a value from each of the two columns mentioned.
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
print(df_urb_pop.head())

df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])

pops_list = list(pops)
print(pops_list)



