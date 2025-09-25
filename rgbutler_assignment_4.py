student_name = "Ryleigh"
current_gpa = 3.8 #Float between 1.0 and 4.0
study_hours = 40 #Integer (ex. 20)
social_points = 50 #Integer (ex. 40)
stress_level = 65 #Integer 1-100

#Display Welcome stats
print(f"Welcome {student_name} to your Academic Profile")
print("")
print(f"Current GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Medium (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")
A = ("Light Difficulty: (12 Credits)")
B = ("Medium Difficulty: (15 Credits)")
C = ("Hard Difficulty: (18 Credits)")

if choice == "A":
    print(f"Mode chosen: {A}")
elif choice == "B":
    print(f"Mode chosen: {B}")
elif choice == "C":
    print(f"Mode chosen: {C}")
else:
    print("Invalid Choice: Choose again.")