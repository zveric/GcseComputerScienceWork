import random;



# Setup

#Aim Word

# List of words
words = ["comfortable", "homeless", "jobless", "juggle", "spare", "shade", "fearless", "extra-small", "guitar", "sneaky", "structure", "equable", "voiceless", "mark", "size", "furry", "cut", "mass", "psychotic", "savory", "station", "yam", "bead", "thin", "poke", "weather", "jolly", "foamy", "needle", "exotic", "seal", "bent", "immense", "exercise", "ordinary", "laughable" ,"pause", "record", "tiny", "burly", "lock"]


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
  guess = input("Guess a letter:")
  letno=(aim_word.find(guess))

  int (wordleft)
 
  if letno < 0:
    print("That letter isnt present")
    trys = trys - 1 
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
       ------""")
    elif trys == 2:
         print("""
  |     
  |     O
  |    -|-
  |    / \\
  ------""")
    elif trys == 1:
      print("""------
  |     
  |     O
  |    -|-
  |    / \\
  ------""")

    elif trys == 0:
      print("""------
  |     |
  |     O
  |    -|-
  |    / \\
  ------""")
      exit()


  else:
    print ("Well done you guessed correctly you guessed letter no:", letno+1)
    wordleft = wordleft-1
    
    








