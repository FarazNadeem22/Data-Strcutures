# assume you have a df called data_train with a bunch of columns names

# Get col names 
col_names = []
col_names.append([cols for cols in data_train])  # This gives me a list of lists with its first item as a list of the col names
col_names = col_names[0] # Get the first item of this list which is the list of column names

# populate two dictionaries one with the frequency count called count dict and the other with mapped named called map dict
map_dict = {}
count_dict = {}
for i,col in enumerate(col_names):
    map_dict[i] = col
    count_dict[col] = 0


# ref used https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value & https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php

for i, element in enumerate(bagging_models_list):
    # extract name from map_dict
    name = map_dict[element.tree_.feature[0]]
    # add one to count in count_dict 
    count_dict[name] +=1

# sort dict by descending order 
count_dict = {key: value for key, value in sorted(count_dict.items(), key=lambda item: item[1], reverse = True)}
 
# convert to pandas DataFrame 
top_predictors_bagging = pd.DataFrame(count_dict, index=[1])
