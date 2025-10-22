subject1 = input("Enter the marks for Subject 1: ")
subject2 = input("Enter the marks for Subject 2: ")
subject3 = input("Enter the marks for Subject 3: ")
def assign_grade(m1, m2, m3):
    average = (m1 + m2 + m3) / 3
    if average >= 90:
        return "Grade: A"
    elif average >= 80:
        return "Grade: B"
    elif average >= 70:
        return "Grade: C"
    elif average >= 60:
        return "Grade: D"
    else:
        return "Grade: F"
grade = assign_grade(int(subject1), int(subject2), int(subject3))
print(grade)