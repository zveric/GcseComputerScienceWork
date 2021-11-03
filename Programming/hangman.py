import random;

def Guessing(word):
  guess = input("Guess a letter:")
  word_there=(word.find(guess))
  print (word)
 
  if word_there <0:
    print("That letter isnt present")
  else:
    print ("Well done you guessed correctly you guessed letter no:", word_there+1)
    Guessing()



  

  







print("Welcome to Hangman")
words = ["comfortable", "homeless", "jobless", "juggle", "spare", "shade", "fearless", "extra-small", "guitar", "sneaky", "structure", "equable", "voiceless", "mark, size", "furry", "cut", "mass", "psychotic", "savory", "station", "yam", "bead", "thin", "poke", "weather", "jolly", "foamy", "needle", "exotic", "seal", "bent", "immense", "exercise", "ordinary", "laughable" ,"pause", "record", "tiny", "burly", "lock"]
  
aim_word = (random.choice(words))
chars = len(aim_word)
print ("word length is", chars)

Guessing(aim_word)











