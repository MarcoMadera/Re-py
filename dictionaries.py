my_dict = {}
my_dict['First Element'] = 'Hey'
my_dict['Second Element'] = 'Bye'

print(my_dict)
print(my_dict['First Element'])

#-----------------#
grades = {}
grades['Communication'] = 7
grades['Mathematics'] = 9
grades['History'] = 6
grades['Databases'] = 9
grades['Social studies'] = 7
grades['Statistics'] = 10
grades['Audio Production'] = 8
grades['Computer programming'] = 10

for key in grades:
  print(key)

for value in grades.values():
  print(value)

for key, value in grades.items():
  print('key: {}, value: {}'.format(key, value))

sum = 0
for grade in grades.values():
  sum += grade

average = sum / len(grades.values())
print(average)