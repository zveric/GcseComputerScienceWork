import random;



# Setup

#Aim Word

# List of words
words = [ "spare", "shade","guitar", "sneaky", "mark", "size", "cut", "savory", "yam", "bead", "thin", "poke", "foamy", "exotic","champ", "seal", "bent","pause", "record", "tiny", "burly", "lock", "hot", "cat", "lamp", "monitor", "play", "big","lumberjack","boy","republican","farsighted","motherland","dermatoglyphics","uncopyrightable","mega","midget","david","smelly","amongus","ant","baboon","badger","bat","bear","beaver","camel","cat","clam","cobra","cougar","coyote","crow","deer","dog","donkey","duck","eagle","ferret","fox","frog","goat","goose","hawk","lion","lizard","llama","mole","monkey","moose","mouse","mule","newt","otter","owl","panda","parrot","pigeon","python","rabbit","ram","rat","raven","rhino","salmon","seal","shark","sheep","skunk","sloth","snake","spider","stork","swan","tiger","toad","trout","turkey","turtle","weasel","whale","wolf","wombat","zebra"]


correctlist = []
incorrectlist = []

aim_word = (random.choice(words))

#Word Lenth Setup
wordlen = len(aim_word)
int(wordlen)
wordlen = wordlen 
wordleft = wordlen

#Trys
trys = 6
int (trys)
  
# Program seen by user

print("Welcome to Hangman")
print ("The word is", wordlen, "letters long")


while wordleft > 0:

  correctletters = ""
  incorrectletters = ""
  
  guess = input("Guess a letter:")
  print("Correctly guessed letters are: ", ''.join(guess if guess 
	 in correctlist else '-' for guess in aim_word))

  letno=(aim_word.find(guess))
  guesslen=len(guess) 
  if guesslen>1:
    print("Please Use a Single letter")
    exit()
  elif guesslen<1:
    print("Please Use a Letter")
    exit()
  int (wordleft)
 
  if letno < 0 or letno > wordlen:
    trys = trys - 1 
    print("That letter isnt present")
    incorrectlist.append(guess)
    if trys == 7:
      print("""
      O
     """)
    elif trys == 6:
      print("""
      O
      |
     """)
    elif trys == 5:
      print("""
      O
     -|-
     """)
    elif trys == 4:
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
      print("You die")
      print("The right word was", aim_word)
      exit()


  else:
    print ("Well done you guessed correctly you guessed letter no:", letno+1)
    wordleft = wordleft-1
    correctlist.append(guess)
  
  print("Your incorrectly guessed letters are",incorrectlist)
  print("Correctly guessed letters are: ", ''.join(guess if guess 
	 in correctlist else '-' for guess in aim_word))
  print(""" 
        
        
        """)
print("well done you got the right word")

  








