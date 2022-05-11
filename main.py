import pandas as pd
import matplotlib.pyplot as plt
import html5lib

data = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states', flavor='html5lib')
states = data[0]
print(states)

# A
max_num_of_reps = states[('Numberof Reps.', 'Numberof Reps.')].max()
min_num_of_reps = states[('Numberof Reps.', 'Numberof Reps.')].min()
max_num_of_reps_states = states[states[('Numberof Reps.', 'Numberof Reps.')] == max_num_of_reps][
    ('Name &postal abbs. [1]', 'Name &postal abbs. [1]')]
min_num_of_reps_states = states[states[('Numberof Reps.', 'Numberof Reps.')] == min_num_of_reps][
    ('Name &postal abbs. [1]', 'Name &postal abbs. [1]')]

print('\n')
print("Max number of Reps:", max_num_of_reps)
print(max_num_of_reps_states)
print('\n')
print("Min number of Reps:", min_num_of_reps)
print(min_num_of_reps_states)

# B
population = states[('Population[B][3]', 'Population[B][3]')]
land_area = states[('Total area[4]', 'km2')]

states[('stat', 'density')] = population / land_area
states.plot(x=('Name &postal abbs. [1]', 'Name &postal abbs. [1]'), y=('stat', 'density'), kind='bar')
plt.tight_layout()
plt.show()

# C
states[('stat', 'date')] = pd.to_datetime(states[('Established[A]', 'Established[A]')])
states.sort_values(('stat', 'date'), ascending=True, ignore_index=True, inplace=True)
print(states[[('Name &postal abbs. [1]', 'Name &postal abbs. [1]'), ('Established[A]', 'Established[A]')]])


# D
def show_max_or_min(data, column, minimum=False):
    description = data[column].describe()
    if minimum:
        return int(description['min'])
    return int(description['max'])


max_state_population = show_max_or_min(states, ('Population[B][3]', 'Population[B][3]'))
print('\n')
print("Max state population:", max_state_population)

min_state_population = show_max_or_min(states, ('Population[B][3]', 'Population[B][3]'), True)
print('\n')
print("Min state population:", min_state_population)

max_num_of_reps_func = show_max_or_min(states, ('Numberof Reps.', 'Numberof Reps.'))
print('\n')
print("Max number of Reps:", max_num_of_reps_func)


