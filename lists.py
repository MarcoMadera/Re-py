friends1 = list()
friends1.append('Pedro')
friends1.append('Enrique')
friends1.append('Alberto')
friends1[1] = 'Joaquin'
friends1.pop()

friends2 = ['María','Consuelo', 'Alejandra']

friends = friends1 + friends2
print(friends)
friends.sort()
print(friends)
del friends[2]
print(friends*2)
print(friends[0])
group = ['f','r','i','e','n','d','s']
str_group = ''.join(group)
print(str_group)

def average_temps(temps):
  sum_of_temps = 0

  for temp in temps:
    sum_of_temps += temp

  return sum_of_temps / len(temps)


if __name__ == '__main__':
  temps = [21, 24, 24, 22, 20, 23, 24]

  average = average_temps(temps)

  print('La temperatura promedio es: {:.1f}'.format(average))