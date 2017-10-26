# File has been tested and updated to python 3.6 (eg. print to print())
#print "Pig Latin"
print('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word: ") # updated raw_inout() to input()
pyg = "ay"

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print(new_word)
else:
    print("empty")