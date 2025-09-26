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

# Study Strategy Decision
# choose a subject of focus
study_options = ["Programming", "Math", "English", "History"]

print("Study Options:")
print("Programming, Math, English, History")

study_choice = input("Choose your subject to focus on:")

# check to make sure the choice is in the Options
if study_choice not in study_options:
    print("Invalid study choice. No changes will be made to GPA or social points")
else:
    print(f"You chose: {study_choice}")
    if study_choice == "Programming" or (study_hours == "Math"):
        current_gpa += 0.20
        social_points -= 5
    elif study_choice == "English" and (current_gpa< 3.0):
        current_gpa += 0.10
        social_points += 2
    elif study_choice == "History" or (study_choice == "English" and current_gpa >= 3.0):
        current_gpa += 0.05
        social_points += 5
    # make sure gpa doesnt go over 4.0 or below 0.0
    if current_gpa > 4.0:
        current_gpa = 4.0
    if current_gpa < 0.0:
        current_gpa

print("Updated Stats after your Study choice: ")
print(f"Current GPA: {current_gpa}")
print(f"Social Points: {social_points}")
print(f"Study Hours: {study_hours}")
print(f"Stress Level: {stress_level}")

# Study Strategy Decision
# choose a subject of focus
study_options = ["Programming", "Math", "English", "History"]

print("Study Options:")
print("Programming, Math, English, History")

study_choice = input("Choose your subject to focus on:")

# check to make sure the choice is in the Options
if study_choice not in study_options:
    print("Invalid study choice. No changes will be made to GPA or social points")
else:
    print(f"You chose: {study_choice}")
    if study_choice == "Programming" or (study_hours == "Math"):
        current_gpa += 0.20
        social_points -= 5
    elif study_choice == "English" and (current_gpa< 3.0):
        current_gpa += 0.10
        social_points += 2
    elif study_choice == "History" or (study_choice == "English" and current_gpa >= 3.0):
        current_gpa += 0.05
        social_points += 5
    # make sure gpa doesnt go over 4.0 or below 0.0
    if current_gpa > 4.0:
        current_gpa = 4.0
    if current_gpa < 0.0:
        current_gpa

print("Updated Stats after your Study choice: ")
print(f"Current GPA: {current_gpa}")
print(f"Social Points: {social_points}")
print(f"Study Hours: {study_hours}")
print(f"Stress Level: {stress_level}")

# Check if player is on track to graduate
# List of activities
activities = ["NSBE", "SGA", "IEEE"]

graduation_ready = True if current_gpa >= 2.0 and stress_level <= 85 else False

# Use Identity Operator
if graduation_ready is True:
    print("You are ready for gradution!")
    # Nested if-statements
    if current_gpa >= 3.5 and "NSBE" in activities:
        print("You are on track to graduate with Honors and Leadership in STEM!")
    elif current_gpa >= 3.0 or study_hours > 35:
        if "IEEE" in activities and stress_level < 65:
            print("You are on track to graduate with technical excellence!")
        else:
            print("You are on track to graduate, but consider more tech based involvment.")
    else: 
        print("Congrats! You are on track to graduate!")
# Use is not operator
elif graduation_ready is not True:
    print("You are not ready for graduation. Requirements not met.")
else:
    print("Error with graduation progress")
