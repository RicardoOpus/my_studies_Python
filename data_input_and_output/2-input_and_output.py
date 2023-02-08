# INPUT:
from random import randint

n = randint(1,2)
guess = 0
while guess != n:
  guess = int(input("Choose a number from 1 to 10" + "\n"))
  if guess == n:
    print("You hit the correct number!")


import sys

# With sys:
if __name__ == "__main__":
    for argument in sys.argv:
        
        print("Received -> ", argument)


# Print:
# Defining a separator
print("Venom's albums are", "Welcome to Hell", "Black Metal", "At War with Satan", sep=", ")


err = "File not found"
print(f"Erro happens: {err}", file=sys.stderr)


# Unpacking:
a, b = "cd"
print(a)
print(b)

c, *d = (1, 2, 3)
print(c)
print(d)