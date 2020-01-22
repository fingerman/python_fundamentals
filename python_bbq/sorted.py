# sorted() to sort a collection’s items in ascending order. Returns new list
nums = [14, 22, 5]
sorted_nums = sorted(nums)
# [5, 14, 22]
print("--------------")

# sort a dictionary by the count of its values:

student_grades = {
    'ivan': [3, 4],
    'petar': [5, 2, 5],
    'maria': [6, 6, 5, 6],
    'gosho': [5, 6]
}

student_grades_sorted = sorted(student_grades.items(), key=lambda kvp: len(kvp[1]))
print(student_grades_sorted)
