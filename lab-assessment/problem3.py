# accepts a tuple with the names of std and their grades, and returns the highest grade

def getGrade(e):
  return e[1]

students = (("Alice", 85), ("Bob", 92), ("Charlie", 78))

def get_highest_grade(tuple_of_tuples):
  grades = [grade for name, grade in tuple_of_tuples]

  return max(grades)

print(get_highest_grade(students))