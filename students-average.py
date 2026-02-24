# Student grade manager 
#     — store student names and grades in a file, calculate averages, find highest/lowest scorer.


print("----- Welcome To Student Grade Manager ------")

# A function which creates a new dictionary and returns it
def update_Dict():
  students_Dict = {}    # create a new dicionary
  try:
    with open("students.txt", "r") as f:
      lines = f.readlines()

      for line in lines:
        student = line.strip()

        # skip the empty lines
        if not student:
          continue

        parts = student.split()

        # skip malformed lines (1 name plus 5 subjects = 6 parts)
        if (len(parts) != 6):
          continue

        name, marks_Str = parts[0], parts[1:]   # splitting to name and marks which stores marks in list as string

        #Conversion of string to integer:
        marks_Int = []
        for mark in marks_Str:
          marks_Int.append(int(mark))
  
        students_Dict[name] = marks_Int

        # marks_Int = [int(mark) for mark in marks_Str]  -> this is short for the above conversion of str to int

    return students_Dict    #Returning the dictionary

  except FileNotFoundError:
    print("File not found!!!")
    return {}

def calculate_gpa(average):
  return average/100 * 4

def calculate_grade(gpa):
  if gpa >= 3.6:
    return 'A'
  elif gpa >= 3.0:
    return 'B'
  elif gpa >= 2.0:
    return 'C'
  elif gpa >= 1.0:
    return 'D'
  else:
    return 'F'
  
def calculate_average(marks):
  average = sum(marks) / len(marks)
  return average
 
def display_students():
  students_Dict = update_Dict()

  for name, marks in students_Dict.items():
    avg = calculate_average(marks)
    gpa = calculate_gpa(avg)
    grade = calculate_grade(gpa)
    print(f"Name: {name} Gpa: {gpa:.2f} Grade: {grade}")

def view_specific(name):
  students_Dict = update_Dict()

  if name not in students_Dict:
    print("Invalid student name!!!")
    return
  else:
    avg = calculate_average(students_Dict[name])
    gpa = calculate_gpa(avg)
    grade = calculate_grade(gpa)
    print(f"Name: {name}")
    print(f"Gpa: {gpa:.2f}")
    print(f"Grade: {grade}")

def highest_and_lowest():
  students_Dict = update_Dict()

  # Guarding the empty data/ if file is empty.
  if not students_Dict:
    print("No student data available.")
    return

  highest = 0
  lowest = 100

  for name, marks in students_Dict.items():
    avg = calculate_average(marks)
    if avg > highest:
      highest = avg
      highest_scorer = name

    if avg < lowest:
      lowest = avg
      lowest_scorer = name

  print("\n----- Highest scoring student ------")
  print(f"Name: {highest_scorer}")
  print(f"GPA: {calculate_gpa(highest):.2f}")

  print("\n----- Lowest scoring student ------")
  print(f"Name: {lowest_scorer}")
  print(f"GPA: {calculate_gpa(lowest):.2f}")

def class_average():
  students_Dict = update_Dict()

  total_marks = 0
  for student in students_Dict:
    for mark in students_Dict[student]:
      total_marks = total_marks + mark

  average = total_marks / (len(students_Dict) * 5)

  print(f"\nAverage score of stuents: {average:.2f}")
  print(f"Average GPA: {calculate_gpa(average):.2f}")

def show_menu():
  print("\n---- Menu -----")
  print("\n1. Add student.")
  print("2. View all student.")
  print("3. View a specific student.")
  print("4. Show highest or lowest scorer.")
  print("5. Class Average.")
  print("6. Exit")
  print("-----------------------------------")

def main():
  while True:
    show_menu()

    while True:
      try:
        choice = int(input("\nEnter your choice: "))
        break
      except ValueError:
        print("Invalid input! Please enter a number between 1-6.")
        continue

    # Adding a student to the file
    if choice == 1:
      name = input("\nEnter the name of the student: ")
      marks = input("Enter marks of 5 subjects separated by space: ").split()

      with open("students.txt", "a") as f:
        f.write(f"{name} {' '.join(marks)}\n")
      
      print("----- Student added successfully -----")

    # View all student in the file
    elif choice == 2:
      print("\n----- Here is the list of all the students: -----\n")
      display_students()
      print("-----------------------------------")

    #View a specific student
    elif choice == 3:
      name = input("\nEnter the name of the student you want to view: ")
      print("\n----- Here is the information ----")
      view_specific(name)
      print("-----------------------------------")
    
    # Show highest and Lowest Scorer
    elif choice == 4:
      highest_and_lowest()
      print("-----------------------------------")

    # Printing out the average of all the students in a class
    elif choice == 5:
      print("----- Class Average ------")
      class_average()
      print("-----------------------------------")
      
    elif choice == 6:
      print("----- Successfully Exited -----")
      break

    else:
      print("Please choose a valid option.")

if __name__ == "__main__":
  main()