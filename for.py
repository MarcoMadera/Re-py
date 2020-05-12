print(range(5))       #range(0,5)
print(range(30))      #range(0,30)

for i in range(5):
  print(i)

for i in range(30):
  if i % 3 != 0:
    continue
  else:
    print(i**2)

for i in range(30):
  if i % 3 == 0:
    print(i**2)
  elif i ==22:
    break

string = 'Marco'

for i in string:
  print(i)