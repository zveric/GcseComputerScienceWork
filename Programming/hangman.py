import random;
print("Welcome to Hangman")
words = ["comfortable", "homeless", "jobless", "juggle", "spare", "shade", "fearless", "extra-small", "guitar", "sneaky", "structure", "equable", "voiceless", "mark, size", "furry", "cut", "mass", "psychotic", "savory", "station", "yam", "bead", "thin", "poke", "weather", "jolly", "foamy", "needle", "exotic", "seal", "bent", "immense", "exercise", "ordinary", "laughable" ,"pause", "record", "tiny", "burly", "lock"]
  
aim_word = (random.choice(words))
chars = len(aim_word)
print ("word length is", chars)
