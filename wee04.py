words = ['house', 'apartment', 'villa', 'condo', 'beachhouse', 'on'] #list of words we will be using
def longest_word(words: list[str]) -> [str]:
  longest = words[0] # we will assume the longest word is the first one on the list
  for word in words[1:]: # loop that goes through each word on the list one by one, and we put 1: because we already assumed the first word which is 0 and so we are comparing it to the words after, if we put 0: we would end up comparing in the loop house with house which makes no sense.
    if len(word) > len(longest): #here we are calculating if the length or len of the current word is the longest, so since it is a loop it will go from determining if apartment is longer than house, and then if villa is longer than apartment, and so on.
      longest = word #so here we are saying that if the len(word) is bigger than the assumed len(longest), that word will be the new longest and since it is a loop it will change if the next word is bigger than the previous.
  return longest 
print("The longest word is:", longest_word(words)) # after loop finishes it will print out the actual longest word in the list.

def shortest_word(words: list[str]) -> [str]:
  shortest = words[0] # we will assume the shortest word is the first one on the lis
  for word in words[1:]: # loop that goes through each word on the list one by one and I put 1: because we already assumed the first word which is 0 and so we are comparing it to the words after, if we put 0: we would end up comparing in the loop, house with house which makes no sense.
    if len(word) < len(shortest):  #here we are calculating if the length or len of the current word is the shortest, so since it is a loop it will go from determining if apartment is shorter than house, and then if villa is shorter than apartment, and so on.
        shortest = word #so here we are saying that if the len(word) is smaller than the assumed len(shortest), that word will be the new shortest and since it is a loop it will change if the next word is smaller than the previous.
  return shortest
print("The shortest word is:", shortest_word(words)) # after loop finishes it will print out the actual shortest word in the list.

def odd_words(words: list[str]) -> list[str]:
  odd_words_list = [] #created an empty list to store the results
  for word in words: #loop to go through each word
    if len(word) % 2 == 1: #check is number of characters is odd having a remainder of 1 when dividing by two
      odd_words_list.append(word) #if the word is odd it is added to the list
  return odd_words_list
odd = odd_words(words)
print("The list of odd words is:", odd)

def average_words(words: list[str]) -> list[str]:
  total_length = 0 # total length is zero for now
  for word in words: #loop
    total_length += len(word) #calc actual total length with each word number of characters
  average = total_length / len(words) # calc average
  result_average = []
  for word in words:
    if abs(len(word) - average) <= 1: #if absolute value of characters is within 1 of average
      result_average.append(word) #if it is within 1 of average it is added to list
  return result_average
avg_words = average_words(words)
print("Words with averages within _+1 of the avg:", avg_words)

foo = ["what", "how", "just", "when"]
bar = ["why", "whatever", "just", "people"]
def intersect(foo: list[str], bar: list[str]) -> bool:
  for word in foo:
      if word in bar: #is the current word in the loop in foo also in bar
        return True #return True if there is a word on both lists
  return False #return false if not
print("Do the lists intersect:", intersect(foo, bar))

# Reflection: 
# 1: My coding only works for odd numbers and part of it is hardcoded
# 2: my triangle leans left instead of right and printed one extra row
# 3: my solution also showed growth per year instead of just final amount
# 4: Now I get it LOL








#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Basic testing. This block validates the logic of the code. Additional 
# requirements such as single return statements are not tested here but 
# must be met anyway.
if __name__ == "__main__":
  testA = ["a", "list", "of", "nearly", "random", "words", "and", "strings"]
  testB = []
  testC = ["a", "be", "cat", "door", 
           "eagle", "galaxy", "forests", "harvests", 
           "important", "journalist"]
  testD = ["Frodo", "Gandalf", "Gollum", "Legolas", "Aragorn", "Rivendell"]
  testE = ["Saruman", "Boromir", "Faramir", "Sauron", "Gollum", "Minas Tirith"]
  testF = None

  # -------- Testing
  print("\nTesting shortest_word")
  if shortest_word(testF) is not None:
    print("shortest_word FAILS null test")
  else:
    print("shortest_word passes null test")

  if shortest_word(testB) is not None:
    print("shortest_word FAILS empty test")
  else:
    print("shortest_word passes empty test")

  if shortest_word(testA) is not testA[0]:
    print("shortest_word FAILS length test")
  else:
    print("shortest_word passes length test")

  # -------- Testing
  print("\nTesting longest_word")
  if longest_word(testF) is not None:
    print("longest_word FAILS null test")
  else:
    print("longest_word passes null test")

  if longest_word(testB) is not None:
    print("longest_word FAILS empty test")
  else:
    print("longest_word passes empty test")

  if longest_word(testA) is not testA[len(testA)-1]:
    print("longest_word FAILS length test")
  else:
    print("longest_word passes length test")
  
  # -------- Testing
  print("\nTesting odd_words")
  if odd_words(testF) is not None:
    print("odd_words FAILS null test")
  else:
    print("odd_words passes null test")
  
  if odd_words(testB) is not None:
    print("odd_words FAILS empty test")
  else:
    print("odd_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if odd_words(testC) != odd_test:
    print("odd_words FAIlS logic test")
  else:
    print("odd words passes logic test")

  # -------- Testing
  print("\nTesting average_words")
  if average_words(testF) is not None:
    print("average_words FAILS null test")
  else:
    print("average_words passes null test")
  
  if average_words(testB) is not None:
    print("average_words FAILS empty test")
  else:
    print("average_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if average_words(testC) != ['eagle', 'galaxy']:
    print("average_words FAILS logic test")
  else:
    print("average_words words passes logic test")

  # -------- Testing
  print("\nTesting intesect")
  if intersect(testF, testA):
    print("intersect FAILS first null test")
  else:
    print("intersect passes first null test")

  if intersect(testA, testF):
    print("intersect FAILS second null test")
  else:
    print("intersect passes second null test")
  
  if intersect(testB, testA):
    print("intersect FAILS first empty test")
  else:
    print("intersect passes first empty test")

  if intersect(testA, testB):
    print("intersect FAILS second empty test")
  else:
    print("intersect passes second empty test")

  if not intersect(testD, testE):
    print("intersect FAILS logic test for true")
  else:
    print("intersect words passes logic test for true")
  
  if intersect(testA, testE):
    print("intersect FAILS logic test for false")
  else:
    print("intersect words passes logic test for false")
