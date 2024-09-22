import os
bookTxt = open("/home/shaheerfferoze/workspace/books/frankenstein.txt", "r")
fileName = os.path.basename("/home/shaheerfferoze/workspace/books/frankenstein.txt")
#print(bookTxt.read())
allTxt = bookTxt.read()
def countWords(txt):
    words = txt.split()
    wrdCount = len(words)
    return wrdCount
print(countWords(allTxt))


def character_count(string):
  string = string.lower()
  char_count = {}
  for char in string:
    char_count[char] = char_count.get(char, 0) + 1
  return char_count


count_dict = character_count(allTxt)
print(count_dict)


def print_report(dictionary):
  # Calculate the total number of words

  # Print the report header
  print(f"--- Begin report of {fileName} ---")
  print(f"{countWords(allTxt)} words found in the document")

  # Sort the dictionary by value in descending order
  sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

  # Print the character counts
  for key, value in sorted_dict:
    if key.isalpha():
        print(f"The '{key}' character was found {value} times")
    else:
       continue
  # Print the report footer
  print("--- End report ---")

print_report(count_dict)