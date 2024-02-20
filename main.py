programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again." 
}

# Retrive items from a dictionary
print(programming_dictionary["Loop"])

# adding new items to the dictionary
programming_dictionary["New"] = "This is an added item"

# empty the dictionary 
# programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "This is an edited item"  

# Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])