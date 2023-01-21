# def convert_text(n):
#     text = str(n)
#     list1 = []
#     a = 0
#     for i in range(len(text)):
#         if text[i]== "0":
#             a = "zero" 
#         elif text[i] == "1":
#             a = "one"
#         elif text[i] == "2":
#             a = "two"    
#         elif text[i] == "3":
#             a = "three"
#         elif text[i] == "4":
#             a = "four"
#         elif text[i] == "5":
#             a = "five"
#         elif text[i] == "6":
#             a = "six"
#         elif text[i] == "7":
#             a = "seven"
#         elif text[i] == "8":
#             a = "eight"
#         elif text[i] == "9":
#             a = "nine"
#         list1.append(a)
#     print(" ".join(list1))
       


# n = int(input())


# convert_text(n)

def convert_text(number):
      # Convert the number to a string
  number_str = str(number)
  
  # Initialize an empty list to store the words
  words = []
  
  # Loop through each character in the number string
  for char in number_str:
    word = {
      '0': 'zero',
      '1': 'one',
      '2': 'two',
      '3': 'three',
      '4': 'four',
      '5': 'five',
      '6': 'six',
      '7': 'seven',
      '8': 'eight',
      '9': 'nine'
    }[char]
    
    # Add the word to the list
    words.append(word)
  
  # Join the words into a single string and return it
  return ' '.join(words)


n = int(input())
print(convert_text(n))