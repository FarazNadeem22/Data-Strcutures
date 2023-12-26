# Import the required module from the Turtle graphics library
from turtle import st

# Dictionary containing state-capital pairs
sc = {
    'New York': 'Albany',
    'California': 'Sacramento',
    'Texas': 'Austin'
}

# Iterate through the dictionary and print each state-capital pair
for state, cap in sc.items():
    print(state, cap)

# Lists containing strings
d = ['f', 'gn', 'stell', 'tess', 'Ric']
f = ['k', 't', 'h', 'b', 'm']

# Combine the lists 'd' and 'f' into a nested list 'cm'
cm = [d, f]

# Print an element from the nested list 'cm'
# Here, it accesses the second list 'f' within 'cm' and prints the third element 'h'
print(cm[1][2])
