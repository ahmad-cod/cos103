# Create a list of tuples, where each tuple contains a name and an age. Write
# a Python program to sort the list by age

def getAge(e):
  return e[1]

list_of_tuples = [
  ('Ade', 39),
  ('Ibrahim', 33),
  ('Isa', 44)
]

list_of_tuples.sort(key=getAge)
print(list_of_tuples)