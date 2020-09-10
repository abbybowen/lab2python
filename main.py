# Author: Abigail Bowen aeb6095@psu.edu
# Collaborator: David Orndorf dbo5077@psu.edu
# Collaborator: Sujay Kandwal sfk5645@psu.edu
# Section: 6
# Breakout: 12
def run():
  number = input("Enter your CMPSC 131 grade: ")
  number = float(number)
  grade = getLetterGrade(number)
  print(f"Your letter grade for CMPSC 131 is {grade}.")

def getLetterGrade(g):
    if g >= 93.0:
      return "A"
    elif g >= 90.0:
      return "A-"
    elif g >= 87.0:
      return "B+"
    elif g >= 83.0:
      return "B"
    elif g >= 80.0:
      return "B-"
    elif g >= 77.0:
      return "C+"
    elif g >= 70.0:
      return "C"
    elif g >= 60.0:
      return "D"
    elif g < 60.0:
      return "F"

if __name__ == "__main__":
    run()
