import random;



# Setup

#Aim Word

# List of words
words = ["comfortable", "spare", "shade","guitar", "sneaky", "mark", "size", "cut", "savory", "station", "yam", "bead", "thin", "poke", "foamy", "exotic","champ", "seal", "bent","pause", "record", "tiny", "burly", "lock", "hot", "cat", "lamp", "monitor", "play", "big","lumberjack", "boy","republican","farsighted","motherland","dermatoglyphics","uncopyrightable"]


aim_word = (random.choice(words))

#Word Lenth Setup
wordlen = len(aim_word)
int(wordlen)
wordlen = wordlen 
wordleft = wordlen

#Trys
trys = wordlen + 4
int (trys)
  
# Program seen by user

print("Welcome to Hangman")
print ("The word is", wordlen, "letters long")


while wordleft > 0:

  correctletters = ""
  
  
  guess = input("Guess a letter:")
  print("Correctly guessed letters are: ", ''.join(guess if guess in correctletters else '-' for guess in aim_word))

  letno=(aim_word.find(guess))
  guesslen=len(guess) 
  if guesslen>1:
    print("Please Use a Single letter")
    exit()
  elif guesslen<1:
    print("Please Use a Letter")
    exit()
  int (wordleft)
 
  if letno < 0:
    trys = trys - 1 
    print("That letter isnt present")
    if trys == 4:
      print("""
      O
     -|-
     / \\
     """)
    elif trys == 3:
      print("""
        O
       -|-
       / \\
       ----""")
    elif trys == 2:
      print("""
  |     
  |     O
  |    -|-
  |    / \\
  ---------""")
    elif trys == 1:
      print("""  -------
  |     
  |     O
  |    -|-
  |    / \\
  ---------""")

    elif trys == 0:
      print("""  -------
  |     |
  |     O
  |    -|-
  |    / \\
  ---------""")
      exit()


  else:
    print ("Well done you guessed correctly you guessed letter no:", letno+1)
    wordleft = wordleft-1
    correctletters = correctletters + guess
    
    








