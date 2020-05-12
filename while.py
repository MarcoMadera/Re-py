import random

def main():
  number_found = False
  random_number = random.randint(0, 50)

  while not number_found:
    number = int(input('Intenta un número: '))

    if number == random_number:
      print('Felicidades. Encontraste el número')
      number_found = True
    elif number > random_number:
      print('El número es más pequeño')
    else:
      print('El número es más grande')

if __name__ == '__main__':
  main()