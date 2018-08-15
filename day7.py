import wikipedia
print("This is the synopsis of 'The screaming staircase' which is the first book of Lockwood and Co series as taken from Wikipedia.")
print(wikipedia.WikipediaPage('The Screaming Staircase').section('Synopsis'))
print("This is the synopsis of 'The Whispering Skull' which is the second book of Lockwood and Co series as taken from Wikipedia.")
print(wikipedia.WikipediaPage('The Whispering Skull').section('Synopsis'))
