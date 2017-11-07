"""
# 01
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for names in names:
    print names

# 02
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print webster[key]

# 03
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
    if number % 2 == 0:
        print number

# 04
# Write your function below!
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1
    return count

# 05
for letter in "Codecademy":
  print letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
  # Only print out the letter i
  if letter == "i":
    print letter


# 06
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# 07
stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

# 08
for food in prices:
    print food
    print "price: %s" % prices[food]
    print "stock: %s" % stock[food]

total = 0

# 09

for food in prices:
    print prices[food] * stock[food]
    total = total + prices[food] * stock[food]

print total

# 10
groceries = [
    "banana",
    "orange",
    "apple"
]
"""

# 11 + 12
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def compute_bill(food):
    total = 0
    for food in shopping_list:
        if stock[food] > 0:
            total = total + prices[food]
            stock[food] = stock[food] - 1
    return total

print compute_bill("banana")
