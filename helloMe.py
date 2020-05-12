def main(): 
  name = str(input('¿Cuál es tu nombre? '))
  age = int(input('¿Cuál es tu edad? '))
  if age > 18:
    print('Hola, señor ' + name + '!')
  else:
    print('Hola, joven ' + name + '!')

if __name__ == '__main__':
  main()