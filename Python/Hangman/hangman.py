"""
This a a simple hangman game built and run in python using ASCII art as the different stages of the hangman.

Words in the dictionary are taken from random sources.
"""

from random import *

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic=[
    """
            +--------+
            |
            |
            |
            |
            |
            |
            |
    ======================
    """,
    """
            +--------+
            |        |
            |        O
            |
            |
            |
            |
            |
    ======================
    """,
    """
            +--------+
            |        |
            |        O
            |        |
            |
            |
            |
            |
    ======================
    """,
    """
            +--------+
            |        |
            |        O
            |       /|
            |
            |
            |
            |
    ======================
    """,
    """
            +--------+
            |        |
            |        O
            |       /|\
            |
            |
            |
            |
    ======================
    """,
    """
            +--------+
            |        |
            |        O
            |       /|\
            |       /
            |
            |
            |
    ======================
    """,
    """
            +--------+
            |        |
            |        O
            |       /|\
            |       / \
            |
            |     DEADMAN!
            |
    ======================
    """,]
    print(graphic[hangman])
    return

def start():
    print("Let's play a game of hangman.")
    while game():
        pass
    scores()

def game():
    dictionary = ["Afghanistan","Albania","Algeria", "Andorra", "Angola", "Antigua", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burma", "Burkina", "Burundi", "Cambodia",  "Cameroon",  "Canada",  "Cape Verde",  "Central African Rep",  "Chad",  "Chile",  "China",  "Colombia",  "Comoros",  "Congo",  "Democratic Republic of Congo",  "Costa Rica",  "Croatia",  "Cuba",  "Cyprus",  "Czech Republic",  "Denmark",  "Djibouti",  "Dominica",  "Dominican Republic",  "East Timor",  "Ecuador",  "Egypt",  "El Salvador",  "Equatorial Guinea",  "Eritrea",  "Estonia",  "Ethiopia",  "Fiji",  "Finland",  "France",  "Gabon",  "Gambia",  "Georgia",  "Germany",  "Ghana",  "Greece",  "Grenada",  "Guatemala",  "Guinea",  "Guinea Bissau",  "Guyana",  "Haiti",  "Honduras",  "Hungary",  "Iceland",  "India",  "Indonesia",  "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea North", "Korea South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russian Federation", "Rwanda", "St Kitts and Nevis", "St Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_correct = 0
    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("You have already picked the letter: ", letter)
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong +=1
                    print("Sorry the letter ( ", letter, " ) is not in this word.")
                else:
                    print("Congratulations!  The letter ( ", letter, " ) is correct.")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("Choose another letter.")
            hangedman(letters_wrong)
            print("".join(clue))
            print("Guesses: ", letters_tried)

            if letters_wrong == tries:
                print("You loose SUCKER!")
                print("The word was always going to be ", word)
                computer_score += 1
                break
            if "".join(clue) == word:
                print("BRAVO ... You did it!")
                print("The word is obviously ", word)
                player_score += 1
                break
    return play_again()

def guess_letter():
    letter = raw_input("Take a guess at finding the mystery country:")
    letter.strip()
    letter.lower()
    print()
    return letter

def play_again():
    answer = raw_input("Would you like to play again? y/n: ")
    if answer in ("y","Y","yes","Yes","YES","Of course!","Please","please","Certainly","certainly","go on","Go on","OK","ok","Ok"):
        return answer
    else:
        print("Thank you for playing the COUNTRY NAME GAME. See you next time!")

def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("----------------")
    print("Player: ", player_score)
    print("Computer: ", computer_score)

    if __name__ == '__main__':
        start()
