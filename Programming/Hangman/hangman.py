import random;

# Function to run the guessing code
def Guessing(word,wordleft):
  guess = input("Guess a letter:")
  letno=(word.find(guess))
  print (word)
  int (wordleft)
 
  if letno <0:
    print("That letter isnt present")
  else:
    print ("Well done you guessed correctly you guessed letter no:", letno+1)
    wordleft = wordleft-1
    return wordleft

# Setup

trys = 0
int (trys)

# List of words
words = ["comfortable", "homeless", "jobless", "juggle", "spare", "shade", "fearless", "extra-small", "guitar", "sneaky", "structure", "equable", "voiceless", "mark, size", "furry", "cut", "mass", "psychotic", "savory", "station", "yam", "bead", "thin", "poke", "weather", "jolly", "foamy", "needle", "exotic", "seal", "bent", "immense", "exercise", "ordinary", "laughable" ,"pause", "record", "tiny", "burly", "lock"]


aim_word = (random.choice(words))
wordlen = len(aim_word)
int(wordlen)
wordlen = wordlen + 1
wordleft = wordlen
  
# Program seen by user

print("Welcome to Hangman")
print ("The word is", wordlen, "letters long")

Guessing(aim_word,wordleft)

while  <= wordlen:
  Guessing(aim_word,wordleft) 
  trys = trys + 1












