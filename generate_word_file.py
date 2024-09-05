from random import randrange

fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Pineapple', 'Mango', 'Strawberry', 'Blueberry', 'Watermelon', 'Kiwi', 'Peach', 'Cherry']
size = int(1e9)

def main():
  with open("./fruits_1e9.txt", "w") as file:
    for i in range(size):
      file.write(fruits[randrange(0, len(fruits))])
      if i != size - 1:
        file.write(',')



if __name__ == "__main__":
  main()