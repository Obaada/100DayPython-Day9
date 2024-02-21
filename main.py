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


###################################################################################
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  grade = ""
  if student_scores[key] > 90:
    grade = "Outstanding"
  elif student_scores[key] > 80 and student_scores[key] < 91:
     grade = "Exceeds Expectations"
  elif student_scores[key] > 70 and student_scores[key] < 81:
    grade =   "Acceptable"
  elif student_scores[key] < 71:
    grade = "Fail"
  student_grades[key] = grade
# 🚨 Don't change the code below 👇
print(student_grades)

####################################
# Nesting
Capitals = {
  "France": "Paris", "Germany": "Berlin"
           }
# Nesting a list in a dictionary
travel_log = {"France" : ["Paris", "Lille", "Dijon"]}

# Nesting a dictionary in a dictionary
travel_log = {"Asia" : {"China": ["Beijing", "Shanghai", "Hong Kong"], "Japan": ["Tokyo", "Kyoto", "Osaka"]}}

# Nesting a dictionary in a list
travel_log = [
  {
    "Asia" : {"China": ["Beijing", "Shanghai", "Hong Kong"]}
  } 
  ,
  {
    "Japan": ["Tokyo", "Kyoto", "Osaka"]
  }
]

##################################################################
#You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, list_of_cities):
  NewCountry = {}
  NewCountry["country"] = country
  NewCountry["visits"] = visits
  NewCountry["cities"] = list_of_cities
  travel_log.append(NewCountry)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")