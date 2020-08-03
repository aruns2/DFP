# Data Focused Python
# 95-888-C3
# HW2 Team 3
# Smith_Colton, coltons@andrew.cmu.edu
# Sharma_Arun, aruns2@andrew.cmu.edu

# 2.a)
records = list()
input_file = open('expenses.txt')

for file_line in input_file:
    records.append(file_line[:-1])

for line in records:
    print(line)

# 2.b)
input_file.close()
input_file = open('expenses.txt')

# list comprehension notation
records2 = [line[:-1] for line in input_file]

print("\nrecords == records2:", records == records2, '\n')

# 2.c)
input_file.close()
input_file = open('expenses.txt')

# nested tuple comprehension notation
records3 = tuple(tuple(line[:-1].split(':')) for line in input_file)

for tup in records3:
    print(tup)

input_file.close()

# 2.d)
# set comprehension notation
cat_set = set(tup[1] for tup in records3 if tup[1] not in "Category")
date_set = {tup[2] for tup in records3 if tup[2] not in "Date"}

print('\n')
print('Categories: ', cat_set, '\n')
print('Dates: ', date_set, '\n')

# 2.e)
# dict comprehension notation
rec_num_to_record = {k: v for k, v in enumerate(records3)}

for rn in range(len(rec_num_to_record)):
    print('{:3d}: {}'.format(rn, rec_num_to_record[rn]))

for i in rec_num_to_record.items():
    print('{:3d}: {}'.format(i[0], i[1]))

for k, v in rec_num_to_record.items():
    print('{:3d}: {}'.format(k, v))