students = {
  'Zainab' : [80, 85, 90],
  'Aisha' : [70, 75, 80],
  'Fatima' : [60, 65, 70]
}

average_marks = {}
for student, marks in students.items():
    average = sum(marks) / len(marks)
    average_marks[student] = average
print(average_marks)
highest_scorer = max(average_marks, key=average_marks.get)
print(f"Highest scorer: {highest_scorer} with average marks of {average_marks[highest_scorer]}")
