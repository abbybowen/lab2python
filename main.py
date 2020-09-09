grade = input("Enter your CMPSC 131 grade: ")
grade = float(grade)
if grade >= 93.0:
  lettergrade = "A"
  print("Your letter grade for CMPSC 131 is A.")
elif grade >= 90.0:
  lettergrade = "A-"
  print("Your letter grade for CMPSC 131 is A-.")
elif grade >= 87.0:
  lettergrade = "B+"
  print("Your letter grade for CMPSC 131 is B+.")
elif grade >= 83.0:
  lettergrade = "B"
  print("Your letter grade for CMPSC 131 is B.")
elif grade >= 80.0:
  lettergrade = "B-"
  print("Your letter grade for CMPSC 131 is B-.")
elif grade >= 77.0:
  lettergrade = "C+"
  print("Your letter grade for CMPSC 131 is C+.")
elif grade >= 70.0:
  lettergrade = "C"
  print("Your letter grade for CMPSC 131 is C.")
elif grade >= 60.0:
  lettergrade = "D"
  print("Your letter grade for CMPSC 131 is D.")
elif grade < 60.0:
  lettergrade = "F"
  print("Your letter grade for CMPSC 131 is F.")
