number = int(input('Pick a Number (Q to Quit)'))
while True:
    if number == 'q' or 'Q':
      print('see yah!')
    if (number % 2) == 0:
     print(f"{number} is even")
    else:
     print(f"{number} is odd")

