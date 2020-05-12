import turtle

def main():
  window = turtle.Screen()
  madera = turtle.Turtle()
  make_square(madera)

  window.mainloop()

def make_square(madera):
  length = int(input('Tamaño de cuadrado: '))

  for _ in range(4):
    make_line_and_turn(madera, length)
    
def make_line_and_turn(madera, length):
  madera.forward(length)
  madera.left(90)

if __name__ == '__main__':
  main()